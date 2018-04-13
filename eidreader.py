#!/usr/bin/env python

# Copyright 2018 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)
#
# Thanks to Vincent Hardy (vincent.hardy.be@gmail.com)
#
"""

Examples::

  $ python -m eidreader

  Read the Belgian eid card in reader and display the data to stdout.

  $ python -m eidreader https://my.server.com/123
  $ python -m eidreader beid://https://my.server.com/123

  Send the data to https://my.server.com/123

If url is a string of type "beid://https://foo.bar.hjk", remove the
first scheme.  This is to support calling this directly as a protocol
handler.

"""

import platform
import os
# import sys
import argparse
import requests
from PyKCS11 import PyKCS11, CKA_CLASS, CKO_DATA, CKA_LABEL, CKA_VALUE

SETUP_INFO = {}
fn = os.path.join(os.path.dirname(__file__), 'setup_info.py')
exec(compile(open(fn, "rb").read(), fn, 'exec'))

SCHEMASEP = '://'

def readdata():
    if 'PYKCS11LIB' not in os.environ:
        if platform.system().lower() == 'linux':
            os.environ['PYKCS11LIB'] = 'libbeidpkcs11.so.0'
        else:
            os.environ['PYKCS11LIB'] = 'beidpkcs11.dll'

    pkcs11 = PyKCS11.PyKCS11Lib()
    pkcs11.load()

    slots = pkcs11.getSlotList()
    
    data = dict(version=SETUP_INFO['version'])
    
    # if len(slots) == 0:
    #     quit("No slot available")

    fields = [
        'surname',
        'firstnames',
        'other_names',
        'gender',
        'nationality',
        'document_type',
        'address_municipality',
        'address_zip',
        'date_of_birth',
        'national_id',
        'card_id',
        'valid_until',
        'location_of_birth',
        'date_issued',
        'address_street_and_number',
        'date_and_country_of_protection']

    images = ['PHOTO_FILE', 'SIGN_DATA_FILE']

    for slot in slots:
        card_data = {}
        try:
            # sess = eid.open_session(slot)
            sess = pkcs11.openSession(slot)
            # print(dir(sess))
            objs = sess.findObjects([(CKA_CLASS, CKO_DATA)])
            # print(len(objs))
            # print(type(objs[0]), dir( objs[0]), objs[0].to_dict())
            for o in objs:
                label = sess.getAttributeValue(o, [CKA_LABEL])[0]
                value = sess.getAttributeValue(o, [CKA_VALUE])
                if len(value) == 1:
                    value = bytes(value[0])
                    # value = ''.join(chr(i) for i in value[0])
                    if label in fields:
                        value = value.decode('utf-8')
                    # try:
                        # value = value.decode('utf-8')
                    # except UnicodeDecodeError:
                    #     pass
                        card_data[label] = value
                    elif label in images:
                        card_data[label] = value
                # print("{}: {}".format(label, value))
                # d = o.to_dict()
                # print(o['CKA_LABEL'])
            #     d['TLV'] = ''.join(chr(i) for i in d['CKA_VALUE']) if 'CKA_VALUE' in d else ''
            #     print("%(CKA_CLASS)s %(CKA_LABEL)s %(TLV)r" % d )
            # for o in objs:
            #     print(o, dir( o ))
            data.update(card_data=card_data)
            data.update(success=True)
            
        except PyKCS11.PyKCS11Error as e:
            data.update(error=str(e))
            # quit("Error: {}".format(e))
            
    return data


def main():
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("url", default=None, nargs='?')
    args = parser.parse_args()
    url = args.url
    
    if url:
        lst = url.split(SCHEMASEP, 2)
        if len(lst) == 3:
            url = lst[1] + SCHEMASEP + lst[2]
        elif len(lst) == 2:
            url = lst[1]
        else:
            quit("Invalid URL {}".format(url))

        data = readdata()
        print("POST to {}: {}".format(url, data))
        r = requests.post(url, data=data)
        print(r)
    else:
        print(readdata())

if __name__ == '__main__':    
    main()
