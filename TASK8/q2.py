n1 = int(input("Enter number of elements in array 1: "))
print("Enter {0} elements of array 1 one by one".format(n1))
array1 = []
for i in range (n1):
    array1.append(int(input()))

n2 = int(input("Enter number of elements in array 2: "))

if(n1 != n2):
    print("False")
    quit()


print("Enter {0} elements of array 2 one by one".format(n2))
array2 = []
for i in range (n2):
    array2.append(int(input()))


array1.sort()
array2.sort()
for i in range (n1):
    if(array1[i] != array2[i]):
        print("False")
        quit()

print("True")