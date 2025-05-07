#print 1 to 100 numbers
 i = 1
while i<=100:
    print(i)
    i+=1

#print 100 to 1 number
i= 100
while i>=1:
    print(i)
    i-=1

#print the multiplication of table n.
n = int(input("enter number"))
i = 1
while i<=10:
    print(n*i)
    i+=1

#print the element of the following list using a loop:
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
n=[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

id= 0
while id < len(n):
    print(n[id])
    id += 1

#search for a number x in this tuple using loop:
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
nums = (1, 4, 9, 16, 25, 36, 64, 81, 100)
x = 36
i = 0
while i < len(nums):
    if(nums[i] == x):
        print("Found",i)
    else:
        print("finding...")
    i += 1
