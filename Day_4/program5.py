def Summation(No):

	Difference = 0
	Sum_Factors = 0
	Sum_NonFactors = 0
	for i in range(1,No):
		if No % i == 0:
			Sum_Factors = Sum_Factors + i
		else:
			Sum_NonFactors = Sum_NonFactors + i
			
	return  Sum_Factors - Sum_NonFactors 
			
	
		
			
			
			
	


def main():
	
	print("Enter the numbr:")
	No = int(input())
	
	Ret = Summation(No)
	print("Difference will Be :",Ret)
	
	
if __name__ == "__main__":
	main()
