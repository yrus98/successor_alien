
def decode_alien_string(n, B):
	num = 0
	for ni in range(len(n)):
		for ci in range(len(B)):
			if n[ni]==B[ci]:
				num = (num*10) + ci 
				break
	return num

def convert_to_base10(num5):
	num10 = 0
	power = 0

	while num5!=0:
		num10 += (num5%10) * (5 ** power)
		power +=1
		num5 = num5//10
	
	return num10

def convert_to_base5_string(num10):
	num5 = ""
	while num10!=0:
		num5 = str(num10%5) + num5
		num10 = num10//5
	return num5

def succ_alien(n, B):
	num5 = decode_alien_string(n, B)

	num10 = convert_to_base10(num5)
	# Increment
	num10 += 1
	
	num5 = convert_to_base5_string(num10)

	succ = B[0] * (len(n) - len(num5))
	for ni in num5:
		succ += B[int(ni)]

	return succ


if __name__ == "__main__":

	print("n='!@^&*', B='!@^&*'' succ_alien:",succ_alien("!@^&*", "!@^&*"))