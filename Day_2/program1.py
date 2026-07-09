def Display_Stars(No):
	while(No>0):
		print("*")
		
		No = No-1


def main():

	print("Enter the Number:")
	No = int(input())
	Display_Stars(No)

if __name__ == "__main__":
	main()
