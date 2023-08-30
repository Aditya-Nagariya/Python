#Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8

#Collecting Information

print("Welcome To The Tip Calculator")
Bill = float(input("What Was Your Total Bill? $"))
Tip = int(input("What Pecentage Of Tip Would You Like To Give 10 12 15? "))
NoOfPeoples = int(input("How Many People You Want To Split The Bill? "))

#Calculating

result = ((Bill*Tip)/100)/NoOfPeoples

#Display Result

print(result)