from cryptography.fernet import Fernet

f_obj=Fernet(b'G3oAnMM793hnMUpJnm6sClhuv65RcgzP0TLNa7OCi7c=')
decryptedmsg=f_obj.decrypt(b'gAAAAABiVFWmf0nQsuz6oHO2RtGb8NYPEj09GOgG57j7MHBc2wY--t1QPG8kLl-rsjWUmE434C3-o0BloiJ1j8JbqIOlsh-tmw==')
print(decryptedmsg)