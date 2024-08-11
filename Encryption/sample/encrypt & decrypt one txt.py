from cryptography.fernet import Fernet

key = Fernet.generate_key()

key2 = Fernet(key)
 #if replace key and kod(mr vampire) -> decrypt

encrypted_txt = key2.encrypt(b"Test.txt") 

print(encrypted_txt)

decrypted_txt=key2.decrypt(encrypted_txt)

print(decrypted_txt)