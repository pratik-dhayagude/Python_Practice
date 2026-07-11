def Cheak_Positive_Negative_Zero(No):
	if No > 0:return 1
	elif No <0 : return 2
	else :return 3


def main():
	
	print("Enter the Number:")
	No = int(input())
	
	Ret = Cheak_Positive_Negative_Zero(No)
	if Ret == 1 : print("Number is positive")
	elif Ret == 2 : print("Number is negative")
	else:print("Number is Zero")

if __name__ == "__main__":
	main()
