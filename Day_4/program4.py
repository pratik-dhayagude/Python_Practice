def Display_NonFactor(No):

	Sum = 0
	for i in range(1,No):
		if No % i != 0:
			Sum += i
			
	return Sum
			
			
	


def main():
	
	print("Enter the numbr:")
	No = int(input())
	
	Ret = Display_NonFactor(No)
	print("Summation of the all non factors will be :",Ret)
	
	
if __name__ == "__main__":
	main()
