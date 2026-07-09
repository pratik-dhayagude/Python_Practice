def Cheak_Divisible(No):
	if No %5 ==0:return True
	else:
		return False


def main():
	print("Enter the Number:")
	No = int(input())
	
	Ret = Cheak_Divisible(No)
	if(Ret):
		print("Number is Divisible by 5")
		
	else:
		
		print("Number is not Divisible by 5")
		
		

if __name__ == "__main__":
	main()
