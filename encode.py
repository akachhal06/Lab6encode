#Aadish Kachhal's encode function
def encode(password):
	res = ""
	for i in password:
		res += str((int(i) + 3) % 10)
	return res

#Aadish Kachhal's main function
if __name__ == "__main__":
	while True:
		print("Menu")
		print("-------------")
		print("1. Encode")
		print("2. Decode")
		print("3. Quit")
		print("")
		print("Please enter an option:")
		op1 = int(input())
		encode_password = ""
		if op1 == 1:
			print("Please enter your password to encode:")
			op2 = str(input())
			encode_password = encode(op2)
			print("Your password has been encoded and stored!")
		elif op1 == 2:
			pass
		elif op1 == 3:
			break
