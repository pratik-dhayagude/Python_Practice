def FindSecondLargest(No):

	Max = No[0]
	Second_Largest = No[0]
	
	for i in range(len(No)):
		if(No[i] > Max):
			Second_Largest = Max
			Max = No[i]
		elif No[i] > Second_Largest and No[i] != Max:
			Second_Largest = No[i]
			
		
	return Second_Largest
	
			
	

def main():

	print("Enter the numbers that you want to add into they list:")
	No = int(input())
	
	
	Value = []
	
	print("Enter the elements into array:")
	
	for i in range(No):
		num = int(input())
		Value.append(num)
		
	Ret = FindSecondLargest(Value)
	print("Second Largest 	 Number will be:",Ret)
		 

if __name__ == "__main__":
	main()
