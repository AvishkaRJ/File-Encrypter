import os, random

from Crypto.Cipher import AES

from Crypto.Hash import SHA256

import getpass


#encrypt Function
def encrypt(key, filename):

	blocksize = 64*1024

	Ofilename = "encrypted-"+filename #Set Output File Name
	
	#Zfill pads left in the string with zeros to complete the width 
	filesize = str(os.path.getsize(filename)).zfill(16)
	
	#Initialization Vector
	InitVector = ''



	for i in range(16):

		InitVector += chr(random.randint(0, 0xFF))



	encryptor = AES.new(key, AES.MODE_CBC, InitVector)

	
	#open the file(rb-It reads the file in binary mode)
	with open(filename, 'rb') as infile:

		with open(Ofilename, 'wb') as outfile: #write the file in binary mode

			outfile.write(filesize)

			outfile.write(InitVector)

			while True:

				size = infile.read(blocksize)

				

				if len(size) == 0:

					break

				elif len(size) % 16 != 0:

					size += ' ' * (16 - (len(size) % 16))

				outfile.write(encryptor.encrypt(size))





def decrypt(key, filename):

	blocksize = 64*1024

	Ofilename = "Decrypted-"+filename #Set Output File Name

	
	#open the file(rb-It reads the file in binary mode)
	with open(filename, 'rb') as infile:

		filesize = long(infile.read(16))

		InitVector = infile.read(16)



		decryptor = AES.new(key, AES.MODE_CBC, InitVector)



		with open(Ofilename, 'wb') as outfile:

			while True:

				size = infile.read(blocksize)



				if len(size) == 0:

					break



				outfile.write(decryptor.decrypt(size))

			outfile.truncate(filesize)





def getKey(password):

	hasher = SHA256.new(password)

	return hasher.digest()



def Main():
	print "***Advanced Encryption Standard (AES) is use to encrypt all files in this program***"
	print "*Enter E to Encrypt the File"
	print "*Enter D to Decrypt the File"
	choice = raw_input("Do you want to Encrypt or Decrypt?: ")



	if choice == 'E':

		filename = raw_input("Enter the File name: ")
		#print "Password :"
		
		#getting password without showing characters entered to the program
		password = getpass.getpass()
		print "Encrypting ..."

		encrypt(getKey(password), filename)

		print "Encryption Done."

	elif choice == 'D':

		filename = raw_input("Enter the File name: ")

		password = getpass.getpass()

		decrypt(getKey(password), filename)

		print "Decryption Done."

	else:

		print "Wrong Input!!!"



if __name__ == '__main__':

	Main()






