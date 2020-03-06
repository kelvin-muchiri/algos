"""
Time complexity: O(nw)
"""

def knapsack(W, wt, val, n):
    # Create a matrix
    # Items are in rows and weight at columns
    K = [[0 for i in range(W+1)] for j in range(n+1)] 

    # Build K[][] in a bottom up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or W == 0:
                # If there are no items at home or the knapsack
                # capacity is 0
                K[i][w] = 0

            elif wt[i - 1] <= w:
                # If the current item's weight is less than or equal to the
                # running weight

                # Get the max value between 1 and 2
                # 1. Max value of the same weight without current item
                # 2. Value of the current item + value that we could accomodate
                # with the remaining weight
                K[i][w] = max(K[i-1][w], val[i-1] + K[i-1][w-wt[i-1]])
            
            else:
                # Item is greater than the running weight

                # Get the max value of the same weight without the current item
                K[i][w] = K[i-1][w]
    
    return K[n][W]

val = [60, 100, 120] 
wt = [10, 20, 30] 
W = 50
n = len(val) 
print(knapsack(W, wt, val, n))
