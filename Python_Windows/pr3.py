def sum_recursive(n):
    if n == 0 :
        return 0
    elif n == 1 :
        return 1
    else:
        return (sum_recursive(n-1)+n)

s = sum_recursive(20)
print(s)

#By anonymous function

sum_recur = lambda n : 0 if (n==0) else (sum_recur(n-1)+n)
result = sum_recur(10)
print(result)

#Factorial
factl = lambda r : 1 if (r==0) else (factl(r-1)*r)
reslt = factl(5)
print(reslt)