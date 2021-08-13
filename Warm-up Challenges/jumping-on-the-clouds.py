def jumpingOnClouds(c):
    cloud_number = min_count_jumps = 0
    n = len(c)

    while cloud_number < n - 1:
        if cloud_number < n - 2 and c[cloud_number + 2] == 0:
            cloud_number += 2
        else:
            cloud_number += 1
        min_count_jumps += 1

    return min_count_jumps

c = [0, 0, 1, 0, 0, 1, 0]
n = 7
print(jumpingOnClouds(c))