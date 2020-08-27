adhar = {123456:{'name':'xyz','mob_num':7219676535,'acc':False},1234567:{'name':'abc','mob_num':7219676535,'acc':True}}
print("\n\n1.Register\n2.Login\n\n")

ch = input("Enter - ")

def file_open(file):
	key_file = open(file,'rb')
	key_data = key_file.read()
	return key_data

if ch == '1':
	ad = int(input('Enter adh - '))
	name = input('Enter name - ')
	mob = int(input('Enter num - '))
	
	if adhar[ad]['name'] == name and adhar[ad]['mob_num'] == mob and adhar[ad]['acc'] != True:

	
		from gen_key import key
		print(key)
	else:
		print("You Already have an account try Login!!")
	
elif ch == '2':
	from login import c
	
	if c:
		print("\n\n1.View Doc\n2.Create Doc\n3.Upload\n4.Apply Doc\n")
		
		ch = input()
		
		if ch == '1':
			print("We have shown only Driving Licence for the example")
			li = input("Enterr your licence num - ")
			from bigchaindb_driver import BigchainDB
			bd = BigchainDB('http://localhost:9984/')

			res = bd.assets.get(search=li)			
			
			if res:
				res = res[0]
				print("L No - " + res['data']['License No'])
				print("Name - " + res['data']['Name'])
				print("Auth to Drive - " + res['data']['Auth to Drive'])
			else:
				print("No entry present")
				
		elif ch == '2':
			from bigchaindb_driver import BigchainDB
			bd = BigchainDB('http://localhost:9984/')
			print("We can create a Document of various document\n Here we are creating a form of appreciation for eg")
			name  = input("Enter name of Docv -")
			data = input("Enter what you want to write in the form- ")
			receiver = input("Enter name of the receiver - ")
			unique_id = input("Enter unique id - ")
			data = {
					'data':{
					'Form Name':name,
					'data':data,
					'receiver':receiver,
					'unique id':unique_id
					}
				}
			metadata = {'time':'Monday'}
			
			pubKey = input("Enter Your Public key which is in .txt file ")
			privKey = input("Enter Your Privtae key which is in .txt file ")
			prepar = bd.transactions.prepare(
							operation = 'CREATE',
							signers = pubKey,
							asset = data,
							metadata = metadata)
			fullfil = bd.transactions.fulfill(prepar,private_keys = privKey)
			c = fullfil
			import json

			#print(json.dumps(c,indent=4))
			bd.transactions.send_commit(fullfil)
			print("This just for showing how the file can be seen")
			
			res = bd.assets.get(search=unique_id)
			
			if res:
				res = res[0]
				
				print("\t\t\t"+res['data']['Form Name']+"\t\t\t")
				print(res['data']['data'])
				print("To-" + res['data']['receiver'])
				print(res['data']['unique id'])
				
		elif ch == '3':
			from bigchaindb_driver import BigchainDB
			bd = BigchainDB('http://localhost:9984/')
			import ipfsApi
			import rsa
			api = ipfsApi.Client('127.0.0.1', 5001)
			res = api.add('a1.pdf')
			
			#print(res)	
			hash_ = res['Hash'].encode()
			pubkey = rsa.PublicKey.load_pkcs1(file_open('a.key'))
			crypto = rsa.encrypt(hash_,pubkey)
			
			name = input("Enter Doc name - ")
			data = {
					'data':{
					'Doc name':name,
					'Hash' : str(crypto)
					}
				}
			metadata = {'time':'Monday'}
			prepar = bd.transactions.prepare(
							operation = 'CREATE',
							signers = '5by6PRMQGhP9DkgRPDn6dpS9abhcS9tiUcM6eC7Phkax',
							asset = data,
							metadata = metadata)
			fullfil = bd.transactions.fulfill(prepar,private_keys = 'Dd7XQLwv8774zzyb22BVReH23mUXFDugXmwkDT9NGjFe')
			c = fullfil
			import json

			print(json.dumps(c,indent=4))
			bd.transactions.send_commit(fullfil)
			
		elif ch == '4':
			print("Send us the hash of all the document required your document signed by Our Public Key")
			
		else:
			print("Thanks!!!!")
			
			
			
			
				
			

	
	
