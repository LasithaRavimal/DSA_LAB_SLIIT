def recrusive(A):
    if A==1:
        return 1
    else:
        return recrusive(A-1)+A

while True:
    num=int(input("Enter number : "))
    if num==-1:
        print("Finished")
        break

    else:
        print("output : ",recrusive(num))
