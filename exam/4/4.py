def recursive(A):
    if A==1:
        return 1
    else:
        return recursive(A-1)*2+1


while True:
    num=int(input("enter number : "))
    if num==-1:
            print("out put : finshed")
            break
    else:
        print("output : ",recursive(num))
 
