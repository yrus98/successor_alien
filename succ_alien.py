
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

def increment_n(n, base, step=1):
	succ = ""
	carry = step
	while n!=0:
		last_digit = n%10
		last_digit += carry
		if last_digit >= base:
			succ = str(last_digit%base) + succ
			carry = last_digit//base
		else:
			succ = str(last_digit) + succ
			carry = 0
		n = n//10
	while carry > 0:
		if carry >= base:
			succ = str(carry%base) + succ
			carry = carry//base
		else:
			succ = str(carry) + succ
			break
	return succ

def succ_alien(n, B, step=1):
	dict_B_to_digit = create_dict_B_to_digit(B)

	base = len(B)

	numB = decode_alien_string(n, dict_B_to_digit)

	numB = increment_n(numB, base, step)

	succ = encode_to_alien_string(numB, len(n)-len(numB), B)

	return succ


if __name__ == "__main__":

	print("n='!@^&*', B='!@^&*' succ_alien:",succ_alien("!@^&*", "!@^&*"))
	print("n='!!!***', B='!@^&*' succ_alien:",succ_alien("!!!***", "!@^&*"))
	print("n='!@^&*#', B='!@^&*#' succ_alien:",succ_alien("!@^&*#", "!@^&*#"))
	print("n='!!!***', B='!@^&*', step=3 succ_alien:",succ_alien("!!!***", "!@^&*", 3))
