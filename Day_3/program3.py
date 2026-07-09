def Display_EvenFactor(No):
	for i in range(1,No):
		if i % 2 == 0 and No % i ==0:print(i,end = " ")
		
	print()
		
		


def main():

	print("Enter the number:")
	No = int(input())
	Display_EvenFactor(No)
	
	

if __name__ == "__main__":
	main()
