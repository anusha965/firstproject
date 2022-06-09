#To find factorial of a number using recursive function
def factorial(x):
        if x==0:
                return 1
        else:
                return(x*factorial(x-1))
n=int(input("Enter the number"))
print("Factorial of {} is {}".format(n,factorial(n)))
