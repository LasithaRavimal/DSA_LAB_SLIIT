A=[]
for i in range(9):
   numbers=int(input("Enter Number : "))
   if numbers>10 and numbers<20:
       A.append(numbers)

   else:
       print("enter valid input")
print(A)    

def sort(A):
    for j in range (1,len(A)):
        key=A[j]
        i=j-1
        while i>=0 and A[i]>key:
            A[i+1]=A[i]
            i=i-1
            A[i+1]=key

sort(A)
print(A)
