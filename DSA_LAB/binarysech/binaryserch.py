#lasitha -Sliit-2y2s-dsa

#A=Array
#low=start Index
#high=end_index
#x=serch value
#mid=mid_index

A=[]

for v in range(4):
    A.append(int(input("Enter a number : ")))
print(A)


x=int(input("Enter serch value:"))

def binary_Serch(A,low,high,x):
    #check base case

    if high>=low:
        mid=(high+low)//2

        if A[mid]==x:
            return mid

        elif A[mid]>x:
            return binary_Serch(A,low,mid-1,x)
        else:
            return binary_Serch(A,mid+1,high,x)
    else:
        return -1
#function call

result=binary_Serch(A,0,len(A)-1,x)    

if result!=-1:
    print("element is present at index",str(result))
else:
    print("element is present at index")
    
            
