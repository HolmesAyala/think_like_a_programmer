import sys

def exercise(width:int = 8) -> None:
	"""
		Print one figure

		Params:

			width -> The width of the convergence point (is even)

		Example:

			> exercise(8)
			#            #
			 ##        ##
			  ###    ###
			   ########
			   ########
			  ###    ###
			 ##        ##
			#            #
	"""
	total_width = width + 2 * ((width // 2) - 1)

	increase = True
	n_characters:int = 1
	n_spaces:int = 0

	while True:
		left_spaces:str = n_spaces * " "
		characters:str = n_characters * '#'
		middle_spaces:str = (total_width - 2 * n_spaces - 2 * n_characters) * " "

		print(f"{left_spaces}{characters}{(middle_spaces)}{characters}")

		if increase:
			n_spaces += 1
			n_characters += 1

			if n_characters > width // 2:
				increase = False
				n_spaces -= 1
				n_characters -= 1
		else:
			n_spaces -= 1
			n_characters -= 1

			if n_characters <= 0:
				break


if __name__ == "__main__":
	if len(sys.argv) <= 1:
		exercise()
	else:
		exercise(int(sys.argv[1]))
