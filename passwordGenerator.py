import random
capital_letters=["A","B","C","D","E","F","G","I","H","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
mi_letters=["a","b","c","d","e","f","g","i","h","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
password=""
question=input("Pres x to generate a password else pres something else ")

if question=="x":

	for q in range(10):
		what_add= random.randint(1,3)
		if what_add == 1:
			add_letter=capital_letters[random.randint(1,25)]
			password = password + str(add_letter)
		elif what_add == 2:
			add=mi_letters[random.randint(1,25)]
			password = password + str(add)
		else:
			ad = random.randint(1,9)
			password = password + str(ad)
	print(password)
else:
	print("bye")

