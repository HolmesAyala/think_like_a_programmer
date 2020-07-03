import sys

def exercise(identification:str = '79927398713') -> bool:
	"""
		Verify if the identification number
		pass the verification Luhn algorithm
		https://es.wikipedia.org/wiki/Algoritmo_de_Luhn

		Parameters:

			identification_number:str -> Number to validate
		
		Example:

			> exercise("79927398713")
			True
	"""
	accum:int = 0
	multiplicator = 1

	for digit in identification:
		n:int = int(digit) * multiplicator

		if n >= 10:
			n = ((n // 10) % 10) + (n % 10)

		accum += n
		multiplicator = 2 if multiplicator == 1 else 1

	return accum % 10 == 0


if __name__ == "__main__":
	if len(sys.argv) <= 1:
		print(exercise())
	else:
		print(exercise(sys.argv[1]))
