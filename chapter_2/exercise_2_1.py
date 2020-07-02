import sys

def exercise(base=8):
	"""
		Print an invert triangle

		Params:

			base -> The size of the base

		Example

			> exercise(base=8)
			########
			 ######
			  ####
			   ##
	"""
	spaces = 0

	while base != 0:
		print(f"{' ' * spaces}{'#' * base}")

		spaces += 1
		base -= 2


if __name__ == "__main__":
	if(len(sys.argv) <= 1):
		exercise()
	else:
		exercise(int(sys.argv[1]))
