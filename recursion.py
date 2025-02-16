#recursion

# when a function calls itself repeatedly

# prints end to backwards

def show(n):
    if(n==0): # base case
        return
    print (n)
    show(n-1)

print(show(4))

def fact(n):
    if(n==1 or n==0):
        return 1
    return fact(n-1) * n

factorial=fact(2)
print(factorial)