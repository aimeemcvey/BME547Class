a = 5


def function_one():
	global a
	print("In function_one, a starts as {}" .format(a))
	a = 13
	print("In function_one, a ends as {}" .format(a))
	return


def function_two():
	print("In function_two, a is {}" .format(a))


def main():
	function_one()
	function_two()
	print("a in the main function is {}" .format(a))


if __name__ == "__main__":
	main()
