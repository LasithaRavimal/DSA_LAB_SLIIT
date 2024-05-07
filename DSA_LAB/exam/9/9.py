def Multiply(M,n):
    if n==1:
        return M
    else:
        return (M + Multiply(M, n-1))
print(Multiply(2,5))


while True:
          num1=int(input("Enter Number 1: "))
          num2=int(input("Enter Number 2: "))
          if num1 or num2 == -1:
              print("finsh,invalid numbers")
              break
          else:
              print("out put :",Multiply(num1,num2))
