def S(n):
    if n==1:
        return 1
    else:
        return S(n-1)+n*n*n
while True:
     
     n=int(input("enter number: "))
     if n==-1:
               print (" finish")
               break
     else:
           print("output ",S(n))
