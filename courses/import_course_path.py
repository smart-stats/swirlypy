# import folder_trial

def test():
	import pathlib
	return pathlib.Path(__file__).parent.absolute()

if __name__== "__main__":
	print("Hello trial")
