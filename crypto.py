from cryptography.fernet import Fernet
#symmetric encryption in which key is used to encrypt and deccrypt the data


key=Fernet.generate_key()
print(key)
msg="Welcome to channel".encode()
f_obj=Fernet(key)
encryptedmsg=f_obj.encrypt(msg)
print(encryptedmsg)

decryptedmsg=f_obj.decrypt(encryptedmsg)
print(decryptedmsg)

