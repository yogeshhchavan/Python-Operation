for i in range(10): #range(stop)
    print("Range", i)
   #Range 1 Range 2 Range 3 Range 4 Range 5 Range 6Range 7 Range 8 Range 9

for i in range(1, 10): #range(satrt, stop)
    print("Range", i)
  #Range 1 Range 2 Range 3 Range 4 Range 5 Range 6Range 7 Range 8 Range 9

for i in range(1, 10, 2): #range(atart, stop, increament)
    print("Range", i)
  #Range 1 Range Range 5 Range 7 Range 9

for i in range(100, 0, -1):
    print(i)
  #100 99 98 97 ... 1

n = int(input("Enter the number"))
for i in range(1,11):
    print(i * n)

#22
44
66
88
110
132
154
176
198
220


n = 5
sum = 0
i = 1
while i <= n:
    sum += i

    i += 1
print(sum)
#15


n = 5 
sum = 0
for i in range(1, n+1):
    sum += i
print(sum)
#15

n = 5
fact = 1
for i in range(1, n+1):
    fact *= i
    i += 1
print("Factorial :",fact)
#Factorial : 120
