import unitest

def fib(n):
    if n == 0:
        return 0
    
    if n == 1:
        return 1
    
    return fib(n - 1) + fib(n - 2)

F = []
def fib_dynamic(n):
    """Solve fib in a top down approach. Uses memoization"""
    if n not in F:
        if n == 0:
            F[n] = 0
        elif n == 1:
            F[n] = 1
        
        else:
            F[n] = fib_dynamic(n - 1) + fib_dynamic(n - 2)

    return F[n]

bottomUpLookUp = []
def fib_dynamic_bottom_up(n):
    """Solve fib in a bottom up approach. Uses tabulation"""
    bottomUpLookUp[0] = 0
    bottomUpLookUp[1] = 1

    for i in range(2, n):
        bottomUpLookUp[i] = bottomUpLookUp[i - 1] + bottomUpLookUp[i - 2]
    
    return bottomUpLookUp[n]

