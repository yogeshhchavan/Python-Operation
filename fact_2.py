#factorial using function
def fact(n):
    if(n == 1  or n == 0):
        return 1
    return fact(n - 1) * n
fact(5)  
#output : 120
