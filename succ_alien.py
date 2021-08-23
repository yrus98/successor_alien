

def succ_alien(n, B):
	num10 = 0
	power = 0
	for ni in range(len(n)-1, -1, -1):
		for ci in range(len(B)):
			if n[ni]==B[ci]:
				num10 += ci * (5 ** power)
				power +=1
				break

	num10 += 1
	# print(num10)
	num5 = ""
	while num10!=0:
		num5 = str(num10%5) + num5
		num10 = num10//5
	# print(num5)
	succ = ""
	for ni in num5:
		succ += B[int(ni)]

	return succ


if __name__ == "__main__":

	print("n='!@^&*', B='!@^&*'' succ_alien:",succ_alien("!@^&*", "!@^&*"))