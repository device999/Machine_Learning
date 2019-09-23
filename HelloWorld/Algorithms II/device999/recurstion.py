
def geom_progress(n):
    q = 3
    if n==1:
        return 1
    else:
        return geom_progress(1)*(q**(n-1))

def fib_seq(n):
    if n==1:
        return 1
    elif n==0:
        return 1
    else:
        return fib_seq(n-1)+fib_seq(n-2)

if __name__=="__main__":
    step = int(input("Enter the step = "))
    print(fib_seq(step))
    print("--------------------------")
    print(geom_progress(step))