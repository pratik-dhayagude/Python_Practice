def Cheak_Even(No):
	if No % 2 ==0: return True
	else:return False
def main():
	print("Enter the number")
	No = int(input())
	Ret = Cheak_Even(No)
	if(Ret):print("The Number is Even Number")
	else:print("The Number is Odd Number")
if __name__ == "__main__":
	main()
