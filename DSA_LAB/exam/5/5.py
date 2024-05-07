def s(n):
    if n==1:
        return 1
    else:
        return s(n-1)+n
   



while True:
        num = int(input("Enter a non-negative integer (or -1 to exit): "))
        if num == -1:
            print("Exiting...")
            break
        elif num < 0:
            print("Please enter a non-negative integer.")
        else:
            result = s(num)
            print("Sum of integers from 1 to {} is: {}",s(num))
