def Display(No1,No2):
	while(No2!=0):
		print(No1)
		No2 = No2-1
		

def main():
	
	print("Enter the Number that you want to Display:")
	No1 = int(input())
	
	print("Enter the Number which tells how many times Display:")
	No2 = int(input())
	Display(No1,No2)
	
	
if __name__ == "__main__":
	main()
