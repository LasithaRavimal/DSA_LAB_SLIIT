#lasitha

def F(n):
    if n<=1:
        return n
    else:
        return F(n-1)+F(n-2)


while True:
    num=int(input("Enter number: "))
    if num==-1:
            print("invalid,Finish")
            break
    else:
        print("output:",F(num))
