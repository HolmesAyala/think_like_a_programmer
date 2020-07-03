import sys

# FIXME If num is negative?
def binToDec(num:str) -> int:
	res:int = 0
	pos:int = 0

	for digit in num[::-1]:
		if digit == "1":
			res += 2 ** pos
		
		pos += 1

	return res

# FIXME If num is negative?
def decToBin(num:int) -> str:
	res:str = ""

	while num > 0:
		res += str(num % 2)
		num //= 2

	return res[::-1]


if __name__ == "__main__":
	if len(sys.argv) == 3:
		to:str = sys.argv[1].split("=")[1]
		num = sys.argv[2]

		if to == "bin":
			print(decToBin(num))
		elif to == "dec":
			print(binToDec(num))
	else:
		print(decToBin(int(sys.argv[1])))
