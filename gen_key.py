import rsa

pubkey, privkey = rsa.newkeys(2048)

from bigchaindb_driver.crypto import generate_keypair

pu_file = input("Enter public key file name (For Login) - ")
pr_file = input("Enter private key file name (For Login) - ")


def keys(pu_file,pr_file):
	user = generate_keypair()
	with open('publicKey.txt','w') as kf:
		kf.write(user.public_key)
		
	with open('privateKey.txt','w') as kf:
		kf.write(user.private_key)
			
	with open(pu_file + '.key','wb') as kf:
		kf.write(pubkey.save_pkcs1('PEM'))



	with open(pr_file + '.key','wb') as kf:
		kf.write(privkey.save_pkcs1('PEM'))
	
	return "SUCCESS 2 Key Pair stored"
key = keys(pu_file,pr_file)
