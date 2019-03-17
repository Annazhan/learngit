#! /etc/bin/python3

import sort

List1 = [1,2,46,26,357,15]

result1 = sort.InsertSort(List1)
print(result1)

result2 = sort.mergeSort(List1)
print(result2)

result3 = sort.bucketSort(List1)
print(result3)

result4 = sort.quickSort(List1,0,len(List1)-1)
print(result4)