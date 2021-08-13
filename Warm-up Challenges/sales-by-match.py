import math

def sockMerchant(n, arr):
    count = 0
    unique_socks = list(set(arr))
    for sock in unique_socks:
        # pairing
        count += math.floor( arr.count(sock) / 2 )
    return count

n = 9
arr = [10, 20, 20, 10, 10, 30, 50, 10, 20]
result = sockMerchant(n, arr)
print(result)