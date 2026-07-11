def Cheak_LeepYear(No):
	if No % 4 == 0:return True
	
	else: return False


def main():
	print("Enter the year:")
	No = int(input())
	
	Ret = Cheak_LeepYear(No)
	if Ret : print("The year is leep year")
	else: print("The year is not leep year")
	

if __name__ == "__main__":
	main()
