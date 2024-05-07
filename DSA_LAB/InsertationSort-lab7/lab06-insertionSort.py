
A=[]

for i in range(0,9):
    numbers=int(input("Enter a number:"))
    if(numbers>10 and numbers<20):
        
      A.append(numbers)

    else:
        print("invalid number")
    i=i+1    
    
print(A)    


def insertionsort(A):

   for j in range(1,len(A)):
    key=A[j]
    i=j-1
    while i>=0 and A[i]<=key:
      A[i+1]=A[i]
      i=i-1
    A[i+1]=key

insertionsort(A)
print("sorted Array",A)
