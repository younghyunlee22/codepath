

def maxDifference(px):
    # Write your code here
    findMax = []
    for i in range(len(px)):
        for j in range(len(px)):
            if px[i+1] > px[i]:
                differ = px[i+1] - px[j]
                j+=1
                findMax.append(differ)
                i+=1
            else:
                return -1
    differ.sort()
    return differ[0]

px = [3, 1, 4]
maxDifference(px)
