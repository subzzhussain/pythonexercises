student_name = str(input("Enter name: "))
hwork = int(input("Enter homework mark: "))
assess = int(input("Enter assessment mark: "))
fexam = int(input("Enter exam mark: "))


def ict_grade(hwork, assess, fexam):
    totalm = hwork + assess + fexam
    avg = str(totalm / 3)
    return avg

final_mark = ict_grade(hwork, assess, fexam)
print(student_name + " " + "scored" + " " + final_mark)


