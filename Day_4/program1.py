def Product_Factors(No):

	Sum = 1
	for i in range(1,No):
		if No % i ==0:
			Sum = Sum * i
			
	return Sum


def main():
	
	print("Enter the numbr:")
	No = int(input())
	
	Ret = Product_Factors(No)
	print("The Sum will be:",Ret)
	
if __name__ == "__main__":
	main()
