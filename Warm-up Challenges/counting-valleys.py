def countingValleys(steps, path):
    position = 0 # sea level
    valley_count = 0
    for i in range(len(path)):
        if path[i] == 'U':
            position += 1
        else:
            position -= 1
        # if position is stepping up the sea level
        if position == 0 and path[i] == 'U':
            valley_count += 1
    return valley_count

steps = 12
path = "DDUUDDUDUUUD"
result = countingValleys(steps, path)
print(result)