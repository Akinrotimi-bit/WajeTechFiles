def maxSteal(nhouse,n):
 
    # initial case
    if (n <= 0):
        return 0
 
    if (n == 0):
        return nhouse[0]
     
    # if current house is robbed then previous cannot be
    # robbed
    robbed = nhouse[n] + maxSteal(nhouse, n - 2)
    # if current house is not robbed then previous
    # house is robbed
    notrobbed = maxSteal(nhouse, n - 1)
 
    # return max of robbed and not robbed
   
    return max(robbed, notrobbed)
 
# Array to get result
nhouse = [2, 5, 1, 3, 6, 2, 4]
n = len(nhouse)
print("Max money stolen is -:",maxSteal(nhouse, n - 1));

