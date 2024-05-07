#R.M.L.R.Dissanayaka
#Sliit-2Y2S-DSA-Bubblesort


A=[]

for i in range(1,8):
    numbers=int(input("Enter a Number :"))
    if(numbers>0 and numbers<20):
        A.append(numbers)
         

    else:

        print("invalid numbers")

print(A)              

              
def bubblesort(A):
    n=len(A)
    for j in range(1,n) :
        for k in range(1,n-j+1):
            if A[k]< A[k-1]:
                 A[k],A[k-1]=A[k-1], A[k]
bubblesort(A)
print("sorted array :")
print(A)
