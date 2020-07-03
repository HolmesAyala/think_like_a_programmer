import sys

def exercise(diameter:int = 8) -> None:
	"""
		Print a square according to diameter given

		Params:

			diameter -> Diameter of circle

		Example:

			> exercise(8)
			  ####
			########
			########
			  ####
	"""
	character:str = "#"
	change:int = 4
	n_characters:int = diameter
	increase = True

	while n_characters > 0:
		n_characters -= change

	n_characters += change

	while True:
		spaces:str = " " * ((diameter - n_characters) // 2)
		characters:str = character * n_characters

		print(f"{spaces}{characters}")

		if increase:
			n_characters += change

			if n_characters > diameter:
				increase = False
				n_characters -= change
		else:
			n_characters -= change

			if n_characters <= 0:
				break


if __name__ == "__main__":
	if len(sys.argv) <= 1:
		exercise()
	else:
		exercise(int(sys.argv[1]))
