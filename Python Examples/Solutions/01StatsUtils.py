def getMinimum1(L):
    min=L[0]
    L1 = L[1:len(L)]
    for i in L1:
        if i < min:
            min=i
    return min

def getMinimum2(L):
    return min(L)

def getMaximum1(L):
    max=L[0]
    L1 = L[1:len(L)]
    for i in L1:
        if i > max:
            max=i
    return max

def getMaximum2(L):
    return max(L)

def getAverage1(L):
    sum=0
    for i in L:
        sum=sum+i
    return sum/float(len(L))

def getAverage2(L):
    return sum(L)/float(len(L))

test = range(20,30)
print ("Min Test Ans 1", getMinimum1(test))
print ("Min Test Ans 2", getMinimum2(test))

print ("Max Test Ans 1", getMaximum1(test))
print ("Max Test Ans 2", getMaximum2(test))

print ("Average Test Ans 1", getAverage1(test))
print ("Average Test Ans 2", getAverage2(test))
