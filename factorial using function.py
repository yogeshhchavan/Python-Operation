#factorial of n number
def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print("Factorial Number",n,"=",fact)
cal_fact(5)

#output : Factorial Number 5 = 120
