import sys
import exercise_2_1

def exercise(width:int = 8) -> None:
	"""
		Print a diamond

		Params:

			width -> The max width of the diamond

		Example

			> exercise(8)
			   ##
			  ####
			 ######
			########
			########
			 ######
			  ####
			   ##
	"""
	spaces:int = (width // 2) - 1
	characters = 2

	while characters <= width:
		print(f"{spaces * ' '}{characters * '#'}")
		spaces -= 1
		characters += 2

	exercise_2_1.exercise(width)


if __name__ == "__main__":
	if len(sys.argv) <= 1:
		exercise()
	else:
		exercise(int(sys.argv[1]))
