
mark = 10
Max = 350


def calc_grade(p_Mark):
    grades = [["U", 0], ["E", 72], ["D", 111], ["C", 150], ["B", 189], ["A", 229], ["A*", 264]]
    p_Mark = f"{p_Mark}"
    Max = 350
    grade = ""
    if p_Mark.lstrip('-').isdigit():
        p_Mark = int(p_Mark)
        if p_Mark <= Max:
            if p_Mark >= 0:
                for para in grades:
                    if p_Mark >= int(para[1]):
                       grade = para[0]
            else:
                raise ValueError("Input Must Be 0 Or More")
        else:
            raise ValueError("Input Must Be Less Than 351")
    else:
        raise TypeError("Input Must Be Integer")
    return grade

if __name__ == '__main__':
    print(calc_grade(mark))
            
    