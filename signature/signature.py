from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
import base64
from signature.encryption import AESGCMCipher
from signature.signature_model import SingatureModel

AES_KEY = b'2WXhLeDTClYFMvItgWbNRQ=='
RSA_PUBLIC_KEY = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAsqMFxt3sKYkyp3zpnrHX
tJgwgv3iqgVacq9HMaNQTYsf6WeIQpC+Qh25XVUZqvkaX+j1j7nm9BuVZQPS1hwQ
awG/GFsW+wk2SRd2swsnB51c9DjtQgAcW3tXIjHJ+ctDgC8o3xEdnjxSU7cwyBTI
Ws8oS6OuNOdQ59XEpZzKLAGi7jQhiUtsZv8kzpwipehRNGyDXjHKJ5zWFQ2OcPFj
u2Abiad08GvssGiR6OoooOiAnl+zOZ8HLyuXAxScqayU9GUcF5kESlgKTttgDP0k
mmUq7UhLxEXrHOrSkq58JKsLtwycM11cvQ5Lgpkv+bsC+TiyqYPCo3G5PfFvM9bV
dwIDAQAB
-----END PUBLIC KEY-----"""

def decrypt_and_verify(encrypted_message):
    try:
        de = AESGCMCipher("2WXhLeDTClYFMvItgWbNRQ==")
        text = de.decrypt(encrypted_message)
        print(text)
        object = SingatureModel(text)
        is_valid = verify_signature(object.data, object.signature)
        return object.data,is_valid
    except Exception as e:
            print(f"Decryption failed: {e}")
            return None,False

def decrypt(encrypted_message):
    encrypted_bytes = base64.b64decode(encrypted_message)
    cipher = AES.new(AES_KEY, AES.MODE_ECB)  # Changed to ECB mode
    decrypted_padded = cipher.decrypt(encrypted_bytes)
    return unpad(decrypted_padded, AES.block_size).decode('utf-8')

def verify_signature(message, signature):
    public_key = RSA.import_key(RSA_PUBLIC_KEY)
    h = SHA256.new(message.encode('utf-8'))
    try:
        pkcs1_15.new(public_key).verify(h, base64.b64decode(signature))
        return True
    except (ValueError, TypeError):
        return False

if __name__ == "__main__":
    message = "UYsDP09N5LP_nRa6u3a6-pGg7z4xHqRpKGeiVbNxV8WFxqo1FI8rMXaSfJJstkEhy4JpD0-MVBZkiUJk9OxwIBwjatPO2NHdzOBtiC4e6sEIN99pfvya3B9ph1TSjLerUMlUtyI3qsSQwXi1KFklqXi5eth60Ox5jqGmVxB9"
    signature = "ehkGoNPGOV9KTlRRtJl+0ETkJ8Thca5Xpu8u7+twojKtSOuk6OSs5vhzZZfrtxfnqhB4bjeWLW5+q46q++N5jGCiqmIKEyw3UlxvskUYRWoVfL1rfjmC18mXxOVL98u2YeC4b+Fsr5+OspEEDYlSfvsWcLy1JMZFBg5Feq+q8RacqEOJnp/rvZ4Z+oJ9dieemlN4GZuvu5iye0ZsSi0MPgFhSigebukmGWqhbgfWtlEowYUg5hz9OEton3dBBD/m1Hs8LMM+S8oBAjP2utg9wXkZLjysSr6hQkIVz6KzPOL9EXh37zdn4+jFWWhaiwbpDDkaphkjbGqsUBHExB3JBQ=="
    de = AESGCMCipher("2WXhLeDTClYFMvItgWbNRQ==")
    text = de.decrypt("xOT2ro4a3Qu4f6OEHrJTEKRiwadMOLOo-0tu-fJCsVxwoTz6nt3aw5gtlXO_8r9mCyc-SZec6lSvNT1uorwsIbFw8HXxET_ykS-is8GKuUGuSR2FWWzZ8Pn6EUrSR6EMF9iQPyIwKtl6c2-DxG5jhZ1KBONJ6UH7E2OFOp6N4uCoF2r0Uhn6PvZDhjvfJiNSY6Tsk3apVbIBmVvmmysy_TcHk8iRUnc253GTaEmwZwI13J1Ui5kBGTb6ikJDlbYRBeh0-eTPo2avb03x1WxMf7mTz1uRvaEXQ282a59DBxmHkuPZ-np384tamu1e3Wnitf5XfHltiTuWvPrd_nJTCH_mFKMXSnP9Sm9NIM0bfxIc8rJVXvqSCBkQXqpvdNoY7F2EQE3Z5zeNghDGrZjTK0LUFRrbNmmRUza-smKf8DpXntSxmFaLKnioMzy5d4aaaNUkq5Ebf0HfE3HCZ1DrAn2dTvPnlOBwS0kt8bVO7ZDnyoXyX56alFVFY0ChL_giOx3EqGKTgqbIny6UxVD57gkHQonVhS-ymtRPMEmEH0M27q7BgUbaJusUvoPSiAW5rMJvdPL135fdRFu3gnoF2cMhueyL4Nka6v-8fp0kaEKKrX3vzlRc67sm9mdXEGxX_aqC4T6t_PkfjHgMbtG0cw6K3D-jXXwd0gvYjjf4rx5KXYCyCBT4ip4uoLR1HWlVL-hAKANeDqyH5r-Ftp4npFsJjWYo6gYgWnYwJWV5SJeppQvQ6_I=")
    object = SingatureModel(text)
    bo = verify_signature(object.data, object.signature)
    print(message.encode('utf-8'))
    print(object.signature)

    print(bo)
