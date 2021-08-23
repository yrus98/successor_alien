
def create_dict_B_to_digit(B):
	dict_B_to_digit = dict()
	value = 0
	for char in B:
		if char in dict_B_to_digit:
			raise Exception("Input Error: Duplicate characters in character set B !")
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

def convert_to_base10(num, base):
	num10 = 0
	power = 0

	while num!=0:
		num10 += (num%10) * (base ** power)
		power +=1
		num = num//10
	
	return num10

def convert_to_base_B_string(num10, base):
	numB = ""
	while num10!=0:
		numB = str(num10%base) + numB
		num10 = num10//base
	return numB

def succ_alien(n, B):
	dict_B_to_digit = create_dict_B_to_digit(B)

	base = len(B)

	numB = decode_alien_string(n, dict_B_to_digit)

	num10 = convert_to_base10(numB, base)
	# Increment
	num10 += 1
	
	numB = convert_to_base_B_string(num10, base)

	succ = encode_to_alien_string(numB, len(n)-len(numB), B)

	return succ


if __name__ == "__main__":

	print("n='!@^&*', B='!@^&*' succ_alien:",succ_alien("!@^&*", "!@^&*"))
	print("n='!!!***', B='!@^&*' succ_alien:",succ_alien("!!!***", "!@^&*"))
	print("n='!@^&*#', B='!@^&*#' succ_alien:",succ_alien("!@^&*#", "!@^&*#"))