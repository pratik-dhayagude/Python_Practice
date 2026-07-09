def printEven(No):
	if No <= 0:return 
	
	for i in range(1,No +1):
		print(i*2,end =" ")
		
	print()
			




def main():

	print("Enter the number:")
	No = int(input())
	
	printEven(No)
	
	


if __name__ == "__main__":
	main()
