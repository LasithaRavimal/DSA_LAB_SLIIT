#sliit-lasitha


def Num(base,exp):
    if exp==0:
        return 1
    else:
        return base*Num(base,exp-1)

while True:
    number1=int(input("Enter numbers: "))
    number2=int(input("Enter numbers: "))
    if number1 and number2 ==-1:
        print ("Enter valid  ")
        break
    else:
        print("output: ",Num(number1,number2))
                      
