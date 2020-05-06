def factorial(numb):
    if numb == 0:
        return 1
    else:
        return numb * factorial(numb-1)
numb = int(input("Enter a number: "))
print(factorial(numb))

