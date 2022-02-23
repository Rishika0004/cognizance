student_info=[["roll no","name","marks"]]

n=int(input("enter the number of records "))

for i in range (1,n+1):
    rollno=int(input("enter the roll no: "))
    name=input("enter the name: ")
    marks= int(input("enter the marks: "))
    l1=[rollno,name,marks]
    student_info.append(l1)

print("\r")

for column in student_info:
    for item in column:
        print(item, end=" ")
    print(" ")
    print("\r")

print("the second row is: ")
print(student_info[2])

