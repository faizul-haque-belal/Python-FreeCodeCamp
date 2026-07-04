def arithmetic_arranger(problems, show_answers=False):

    if len(problems)>5:
        return "Error: Too many problems."
    top=[]
    bottom=[]
    dash=[]
    answer=[]

    for problem in problems:
        first,operator,second=problem.split()
        if operator not in ["+","-"]:
            return "Error: Operator must be '+' or '-'."
        if not first.isdigit() or not second.isdigit():
            return "Error: Numbers must only contain digits."
        if len(first) > 4 or len(second) > 4:
            return "Error: Numbers cannot be more than four digits."
        width=max(len(first),len(second)) + 2
            
        top.append(first.rjust(width))
        bottom.append(operator + second.rjust(width-1))
        dash.append('-' * width)
        if operator == "+":
            result = int(first) + int(second)
        else:
            result = int(first) - int(second)

        answer.append(str(result).rjust(width))
    line1 = "    ".join(top)
    line2 = "    ".join(bottom)
    line3 = "    ".join(dash)

    if show_answers:
        line4 = "    ".join(answer)
        return line1 + "\n" + line2 + "\n" + line3 + "\n" + line4

    return line1 + "\n" + line2 + "\n" + line3
print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')