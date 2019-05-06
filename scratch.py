def valid(n,k,j):
    """"Calculate number of valid sequences with n numbers, each number is no larger than k, and sequence ends with j"""
    if n==4 and j == 1:
        num = (k-1) * (k-2)
    else:
        num = ((k-1)**(n-2) - (k-2) * (k-1)**(n-4)) % (10**10 + 7)
    print num
    return num

valid(4,4,2)
valid(4,100,1)
valid(100,100,1)
valid(347,2281,829)
valid(1.26*10**6, 1.7*10**6, 1)
valid(10**7, 10**12, 829)