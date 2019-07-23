def divide(arr,low,high):
    i=low-1
    pivot=arr[high]
    for j in range(low,high):
        if arr[j]<pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1

def quicksort(arr,low,high):
    if low<high:
        crt=divide(arr,low,high)
        quicksort(arr,low,crt-1)
        quicksort(arr,crt+1,high)

N=int(input())
array=[int(i) for i in input().split()]
quicksort(array,0,N-1)
for i in array:
    print (i,end=" ")
