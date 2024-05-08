def recrusive(A):
    if A==1:
        return 1

    else:
        return recrusive(A-1)+A-1

while True:
     num=int(input("enter numbe: "))
     if num==-1:
         print("finished")
         break
         
     else:
          print("output:",recrusive(num))
