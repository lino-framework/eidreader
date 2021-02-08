# Copyright 2018-2021 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)
"""
Read the Belgian eID card from reader and display the data to
stdout or post it to a web server.

Details see http://eidreader.lino-framework.org/usage.html
"""

import logging
import time
import os
from os.path import expanduser, join, dirname
import sys
import argparse
import base64
import platform
import json
import configparser
import requests
from urllib.request import getproxies
from requests.exceptions import ConnectionError
from eidreader.setup_info import SETUP_INFO
from PyKCS11 import PyKCS11, CKA_CLASS, CKO_DATA, CKA_LABEL, CKA_VALUE, PyKCS11Error

SCHEMESEP = '://'

images = set("""
PHOTO_FILE
""".split())
# ignored:
# DATA_FILE
# CERT_RN_FILE
# SIGN_DATA_FILE
# SIGN_ADDRESS_FILE
# ADDRESS_FILE

fields = set("""
carddata_os_number
carddata_os_version
carddata_soft_mask_number
carddata_soft_mask_version
carddata_appl_version
carddata_glob_os_version
carddata_appl_int_version
carddata_pkcs1_support
carddata_key_exchange_version
carddata_appl_lifecycle
card_number
validity_begin_date
validity_end_date
issuing_municipality
national_number
surname
firstnames
first_letter_of_third_given_name
nationality
location_of_birth
date_of_birth
gender
nobility
document_type
special_status
duplicata
special_organization
member_of_family
date_and_country_of_protection
address_street_and_number
address_zip
address_municipality
""".split())

# the following fields caused encoding problems, so we ignore them for
# now:
# carddata_serialnumber
# carddata_comp_code
# chip_number
# photo_hash

class EIDReader:

    url = None
    proxies = None
    logger = None
    sent_card_number = None

    def startup(self):

        if 'PYKCS11LIB' not in os.environ:
            if platform.system().lower() == 'linux':
                os.environ['PYKCS11LIB'] = 'libbeidpkcs11.so.0'
            elif platform.system().lower() == 'darwin':
                os.environ['PYKCS11LIB'] = 'libbeidpkcs11.dylib'
            else:
                os.environ['PYKCS11LIB'] = 'beidpkcs11.dll'

        pkcs11 = PyKCS11.PyKCS11Lib()
        pkcs11.load()
        return pkcs11

        # slots = pkcs11.getSlotList()
        # for slot in slots:
        #     try:
        #         # sess = eid.open_session(slot)
        #         self.session = pkcs11.openSession(slot)
        #         return True
        #
        #     except PyKCS11Error:
        #         continue
        #         # data.update(error=str(e))
        #         # quit("Error: {}".format(e))
        # return False

    def read_data(self):
        data = dict(
            eidreader_version=SETUP_INFO['version'], success=False,
            message="Could not find any reader with a card inserted")

        # print(dir(sess))
        try:
            objs = self.session.findObjects([(CKA_CLASS, CKO_DATA)])
        except PyKCS11Error as e:
            data.update(message=str(e))
            return data
            # print(len(objs))

        # print(type(objs[0]), dir( objs[0]), objs[0].to_dict())
        for o in objs:
            label = self.session.getAttributeValue(o, [CKA_LABEL])[0]
            value = self.session.getAttributeValue(o, [CKA_VALUE])
            if len(value) == 1:
                # value = ''.join(chr(i) for i in value[0])
                value = bytes(value[0])
                if label in fields:
                    # value = value.decode('utf-8')
                    try:
                        value = value.decode('utf-8')
                    except UnicodeDecodeError:
                        print("20180414 {} : {!r}".format(label, value))
                    data[label] = value
                elif label in images:
                    value = base64.b64encode(value)
                    data[label] = value.decode('ascii')
            # print("{}: {}".format(label, value))
            # d = o.to_dict()
            # print(o['CKA_LABEL'])
        #     d['TLV'] = ''.join(chr(i) for i in d['CKA_VALUE']) if 'CKA_VALUE' in d else ''
        #     print("%(CKA_CLASS)s %(CKA_LABEL)s %(TLV)r" % d )
        # for o in objs:
        #     print(o, dir( o ))
        # data.update(card_data=card_data)
        data.update(success=True)
        data.update(message="OK")
        data.update(eidreader_country="BE")
        # del data['error']
        return data

    def send_data(self, data):
        if self.sent_card_number == data['card_number']:
            return
        self.logger.info("Found new card data %s", data)
        if self.url:
            self.logger.info("POST data to %s", url)
            post_data = dict(card_data=json.dumps(data))
            try:
                r = requests.post(self.url, data=post_data, proxies=self.proxies)
                self.logger.info("POST returned {}".format(r))
            except ConnectionError as e:
                self.logger.info("ConnectionError %s", e)
                return
        else:
            print(json.dumps(data))

        self.sent_card_number = data['card_number']


    def poll_forever(self):
        self.logger.info("Waiting for eid cards (Ctrl-C to terminate) ...")
        while True:
            pkcs11 = self.startup()
            slot = pkcs11.wait_for_slot_event()
            self.session = pkcs11.openSession(slot)
            # if not self.startup():
            #     print("No slot available")
            #     return
            # self.logger.info("Reading data...")
            data = self.read_data()  # 20180521 fix 2393
            if data['success']:
                self.send_data(data)
            else:
                # self.logger.info("Forget last card number")
                if self.sent_card_number:
                    print("Forget last card number")
                    self.sent_card_number = None
            # time.sleep(1)

    def main(self):
        parser = argparse.ArgumentParser(description=__doc__)
        parser.add_argument("url", default=None, nargs='?')
        parser.add_argument("-l", "--logfile", default=None)
        parser.add_argument("-c", "--cfgfile", default=None)
        args = parser.parse_args()
        url = args.url

        if url:
            lst = url.split(SCHEMESEP, 2)
            if len(lst) == 3:
                url = lst[1] + SCHEMESEP + lst[2]
            elif len(lst) == 2:
                pass
                # url = lst[1]
            else:
                quit("Invalid URL {}".format(url))
            self.url = url

        cfg_files = ["eidreader.ini", expanduser("~/eidreader.ini"),
                     join(dirname(__file__), "eidreader.ini")]
        if args.cfgfile:
            cfg_files = [args.cfgfile]
        if args.logfile:
            logging.basicConfig(filename=args.logfile, level=logging.INFO,
                                format='[%(asctime)s] %(levelname)s %(message)s')
        self.logger = logging.getLogger('eidreader')
        self.logger.info("Invoked as %s", ' '.join(sys.argv))

        proxies = getproxies()
        self.logger.info("getproxies() returned %s", proxies)
        cp = configparser.ConfigParser()
        self.logger.info("Load config from %s", cfg_files)
        cp.read(cfg_files)
        if cp.has_option('eidreader', 'http_proxy'):
            proxies['http'] = cp.get('eidreader', 'http_proxy')
        if cp.has_option('eidreader', 'https_proxy'):
            proxies['https'] = cp.get('eidreader', 'https_proxy')
        self.logger.info("Using proxies: %s", proxies)

        self.proxies = proxies
        self.poll_forever()

def main():
    EIDReader().main()

if __name__ == '__main__':
    main()
