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
    if(len(a) <= 1):
        return a
    else:
        m = len(a)//2
        a1 = a[:m]
        a2 = a[m:]
        a1 = mergeSort(a1)
        a2 = mergeSort(a2)

        result = []
        i = 0
        j = 0
        while i < len(a1) and j < len(a2):
            if a1[i]<=a2[j]:
                result.append(a1[i])
                i += 1
        
            else:
                result.append(a2[j])
                j += 1

        result += a1[i:]
        result += a2[j:]
        return result


def bucketSort(list):
    m = max(list)
    buckets = [0]*(m+1)
    for i in list:
        buckets[i] +=1
    result = []
    for i in range(len(buckets)):
        if buckets[i]!= 0:
            result.append(i)
    return result  



def quickSort(list,left,right):
    
    if(right<=left):
        return list
    p = partition(list,left,right)
    quickSort(list,left,p-1)
    quickSort(list,p+1,right)
    return list

def partition(list,l,r):
    x = list[r]
    i = l-1
    for j in range(l,r):
        if list[j]<= x:
            i += 1
            list[i],list[j] = list[j],list[i]
    list[i+1],list[r] = list[r],list[i+1]
    return i+1