A=[]
for i in range(10):
    numbers=int(input("Enter number : "))
    if numbers==-1:
        print("invalid")
        break
    else:
        A.append(numbers)
print(A)       
              
def partition(A,p,r):
    x=A[r]
    i=p-1
    for j in range (p,r):
        if A[j]<=x:
            i=i+1
            A[i],A[j]=A[j],A[i]
    A[i+1],A[r]= A[r], A[i+1]     
    return (i+1)

def quicksort(A,p,r):
    if p<r:
        q=partition(A,p,r)
        quicksort(A,q,q-1)
        quicksort(A,q+1,r)

quicksort(A,0,len(A)-1)
print(A)
