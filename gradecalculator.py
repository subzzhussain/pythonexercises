def grade_calc():
    mathmark = int(input("Enter math mark:"))
    chemmark = int(input("Enter chemistry mark:"))
    physmark = int(input("Enter physics mark:"))


    average_mark = round(mathmark + chemmark + physmark) / 3
    print("Your percentage score is", average_mark)

    if average_mark >=70:
        print("You scored grade A")
    elif average_mark >=60:
        print("You scored grade B")
    elif average_mark >50:
        print("You scored grade C")
    elif average_mark >=40:
        print("You scored grade D")
    else:
        print("You failed")

grade_calc()