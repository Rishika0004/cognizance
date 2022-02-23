a=int(input("enter the number: "))

rem=0
original_number= a
reversed_number=0

while(a>0):
    rem=a%10
    reversed_number= (reversed_number*10)+ rem
    a=a//10

if(original_number==reversed_number):
    print("palindrome")
else:
    print("not palindrome")
