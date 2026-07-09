def Display_NonFactor(No):

	
	for i in range(1,No):
		if No % i != 0:
			print(i)
			
			
	


def main():
	
	print("Enter the numbr:")
	No = int(input())
	
	Display_NonFactor(No)
	
	
if __name__ == "__main__":
	main()
