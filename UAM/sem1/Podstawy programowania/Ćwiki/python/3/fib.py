fib=[0,1]
x=int(input())
i=0
print(fib[0])
print(fib[1])
while i<x:
    fib.append(fib[i]+fib[i+1])
    print(fib[-1])
    i+=1
