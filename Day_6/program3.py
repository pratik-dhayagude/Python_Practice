def CheakArraySorted(No):
	
	
	for i in range(len(No)):
		if(No[i]>No[i+1]):
			return False
		else:
			return True
			
		


def main():

	print("Enter the number:")
	No = int(input())
	
	Value = []
	
	for i in range(No):
		Num = int(input())
		Value.append(Num)
	Ret = CheakArraySorted(Value)
	if Ret:
		print("The array is sorted")
	else:
		print("The Array is not sorted")
	
	
if __name__ == "__main__":
	main()
