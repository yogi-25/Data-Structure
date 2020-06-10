
def linear(arr,x,n):
   for i in range(0,n):
       if(arr[i]==x):
           return i

   return -1
arr=[2,34,4,5,3,3,4,5,3,4,5,3,34,3,443,67]
x=443
n=len(arr)
a=linear(arr,x,n)
if(a==-1):
    print("Not found")
else:
    print("present at index",a)