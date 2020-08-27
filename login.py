def file_open(file):
	key_file = open(file,'rb')
	key_data = key_file.read()
	key_file.close()
	
	return key_data
	
	
import rsa
import string
import random

res = ''.join(random.choices(string.ascii_uppercase + string.digits, k = random.randint(5,15))).encode() 



#res = bytes(c,'utf-8')
##res = c
pubkey = rsa.PublicKey.load_pkcs1(file_open('a.key'))

crypto = rsa.encrypt(res,pubkey)

#print(crypto)

privkey = rsa.PrivateKey.load_pkcs1(file_open('b.key'))
try:
	decrypt = rsa.decrypt(crypto,privkey)
except:
	decrypt = b"HIIIIIIIIIIII"
	#print("WRONG")
	
#print(decrypt.decode())
c = False
if(res.decode() == decrypt.decode()):
	c = True
else:
	print("\n\nYOU ARE WRONG\n\n")
