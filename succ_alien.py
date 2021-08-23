
def create_dict_B_to_digit(B):
	dict_B_to_digit = dict()
	value = 0
	for char in B:
		dict_B_to_digit[char] = value
		value += 1
	return dict_B_to_digit

def encode_to_alien_string(num, leading_zeros, B):
	succ = B[0] * leading_zeros
	for ni in num:
		succ += B[int(ni)]
	return succ

def decode_alien_string(n, dict_B_to_digit):
	num = 0
	for char in n:
		if char in dict_B_to_digit:
			num = (num * 10) + dict_B_to_digit[char]
		else:
			raise Exception("Input Error: Number n contains characters not defined in the character set B!")
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
	dict_B_to_digit = create_dict_B_to_digit(B)

	num5 = decode_alien_string(n, dict_B_to_digit)

	num10 = convert_to_base10(num5)
	# Increment
	num10 += 1
	
	num5 = convert_to_base5_string(num10)

	succ = encode_to_alien_string(num5, len(n)-len(num5), B)

	return succ


if __name__ == "__main__":

	print("n='!@^&*', B='!@^&*'' succ_alien:",succ_alien("!@^&*", "!@^&*"))