# Copyright 2018 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)
#
import platform
import os
# import sys
from PyKCS11 import PyKCS11, CKA_CLASS, CKO_DATA, CKA_LABEL, CKA_VALUE

SETUP_INFO = {}
fn = os.path.join(os.path.dirname(__file__), 'setup_info.py')
exec(compile(open(fn, "rb").read(), fn, 'exec'))

def eid2dict():
    if 'PYKCS11LIB' not in os.environ:
        if platform.system().lower() == 'linux':
            os.environ['PYKCS11LIB'] = 'libbeidpkcs11.so.0'
        else:
            os.environ['PYKCS11LIB'] = 'beidpkcs11.dll'

    pkcs11 = PyKCS11.PyKCS11Lib()
    pkcs11.load()

    slots = pkcs11.getSlotList()
    
    data = dict(version=SETUP_INFO['version'], country="BE")
    
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


