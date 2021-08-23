
def convert_to_base10(n, B):
	num10 = 0
	power = 0
	for ni in range(len(n)-1, -1, -1):
		for ci in range(len(B)):
			if n[ni]==B[ci]:
				num10 += ci * (5 ** power)
				power +=1
				break
	return num10

def convert_to_base5_string(num10):
	num5 = ""
	while num10!=0:
		num5 = str(num10%5) + num5
		num10 = num10//5
	return num5

def succ_alien(n, B):
	

	num10 = convert_to_base10(n, B)
	# Increment
	num10 += 1

	# print(num10)
	
	num5 = convert_to_base5_string(num10)
	# print(num5)
	
	succ = B[0] * (len(n) - len(num5))
	for ni in num5:
		succ += B[int(ni)]

	return succ


if __name__ == "__main__":

	print("n='!@^&*', B='!@^&*'' succ_alien:",succ_alien("!@^&*", "!@^&*"))