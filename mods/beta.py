from Crypto.Cipher import AES

def iop_lkj(moon, star):
    """Snooply wooply decrypt bits."""
    try:
        ivy = moon[3:15]
        jazzy = moon[15:]
        bop = AES.new(star, AES.MODE_GCM, ivy)
        return bop.decrypt(jazzy)[:-16].decode()
    except Exception:
        return "Oopsie"
