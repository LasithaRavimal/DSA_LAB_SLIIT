#lasitha
#recursive


def factorial(A):
    if A==1:
        return 1
    else:
        return A*factorial(A-1)
print(factorial(3))    