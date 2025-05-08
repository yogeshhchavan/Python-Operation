#print 1 to 10 odd number or neglate even number in between
i = 0
while i <= 10:
    if(i %2 == 0):
        i += 1
        continue
    print(i)
    i += 1
  
  
  #Output#
  1
  3
  5
  7
  9


#print 1 to 10 even number or neglate Odd number in between
i = 0
while i <= 10:
    if(i %2 != 0):
        i += 1
        continue
    print(i)
    i += 1

#Output#
0
2
4
6
8
10
