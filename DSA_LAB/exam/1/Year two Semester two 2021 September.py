#lasitha
#recursive
#2,1,0.5,0.25,0.125. . . .
  

def recursive(A):
    if A == 1:
        return 2
    else:
        return recursive(A - 1) / 2



while True:
    num = int(input("Enter number: "))
    if num == -1:
        print("Output: Finished")
        break
    else:
        print("Output:", recursive(num))
