#insetaionsort-try1

A=[]

for v in range(6):
          
          A.append(int(input("Enter number: ")))
print(A)                      


def insertaion_sort(A):

    for j in range(1,len(A)):
        key=A[j]
        i=j-1
        while i>=0 and A[i]>key:
            A[i+1]=A[i]
            i=i-1
        

        A[i+1]=key

insertaion_sort(A)
print("sorted")
print(A)
