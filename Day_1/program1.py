def Division_Numbers(No1,No2):
	return No1/No2


def main():

	print("Enter the first Number:")
	No1 = int(input())
	
	print("Enter the Second Number:")
	No2 = int(input())
	
	Ret = Division_Numbers(No1,No2)
	print("The Division of Two numbers will be :",Ret)

if __name__ == "__main__":
	main()
