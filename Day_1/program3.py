def Display_Reverse(No):
	while(No>0):
		print(No)
		
		No = No-1
def main():
	print("Enter the Number :")
	No = int(input())

	Display_Reverse(No)

if __name__ == "__main__":
	main()
