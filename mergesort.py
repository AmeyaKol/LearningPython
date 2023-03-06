def merge(arr,s,m,e):
    temp = []
    l = s
    r = m+1
    while(l<=m and r<=e):
        if arr[l]<=arr[r]:
            temp.append(arr[l])
            l+=1
        else:
            temp.append(arr[r])
            r+=1
    while(l<=m):
        temp.append(arr[l])
        l+=1
    while(r<=e):
        temp.append(arr[r])
        r+=1
    for i in range(s,e+1):
        arr[i]=temp[i-s]    
    return

def mergesort(arr,l,h):
    if l==h:
        return
    m = l + (h-l)//2
    mergesort(arr,l,m)
    mergesort(arr,m+1,h)
    merge(arr,l,m,h)
    return

arr = [3,7,8,4,1,9]
mergesort(arr,0,len(arr)-1)
print(arr)

myarr=[1,2,3]
def func(arr):
    for i,v in enumerate(arr):
        arr[i]=v*v
    print(arr)
    return
func(myarr)
print(myarr)