def FindMax(No):
	Max = No[0]
	for i in range(len(No)):
		if(No[i]>Max):
			Max = No[i]
			
	return Max

def main():

	print("Enter the numbers that you want to add into they list:")
	No = int(input())
	
	
	Value = []
	
	print("Enter the elements into array:")
	
	for i in range(No):
		num = int(input())
		Value.append(num)
		
	Ret = FindMax(Value)
	print("Maximum Number will be:",Ret)
		 
	
if __name__ == "__main__":
	main()
