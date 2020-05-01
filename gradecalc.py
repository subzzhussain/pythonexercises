def average_score(mathmath, chemmark, physmark):
    average = ( mathmath + chemmark + physmark ) / 3
    print(average)

def grade_calc(userMark):
    if(userMark < 40):
        print("You have failed")
    elif(userMark >=40):
        print("D")
    elif(userMark >=50):
        print("C")
    elif(userMark >=60):
        print("B")
    else:
        print("A")

def inp_mark():
    mathmark = int(input("Enter math mark: "))
    chemmark = int(input("Enter chemistry mark: "))
    physmark = int(input("Enter physics mark: "))

    return mathmark, chemmark, physmark

def results_table(mathmark, chemmark, physmark):
    print("Mark\tGrade")
    print(str(mathmark) + "\t", grade_calc(mathmark))

def main():
    inp_mark()

