def InsertSort(a):
    for i in range(1,len(a)):
        tmp = a[i]
        j = i-1
        while j>=0 and a[j]>tmp:
            a[j+1] = a[j]
            j -=1
        a[j+1] = tmp
    return a


def mergeSort(a):
    if(len(a) == 1):
        return a[0]
    else:
        m = len(a)//2
        a1 = a[0:m]
        a2 = a[m+1:len(a)]
        a1 = mergeSort(a1)
        a2 = mergeSort(a2)

        