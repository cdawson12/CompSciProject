import re
import maintest
import numpy as np


problemType = "simultaneousEquations"
input_string = maintest.response_text


def replace_double_minus(input_string):
    return re.sub(r'—', '-', input_string)


if problemType == "complexNumberAddition":

    def to_one_line(input_string):
        return " ".join(input_string.splitlines())


    input_string = to_one_line(input_string)

    input_string = replace_double_minus(input_string)

    print(input_string)


    def extract_complex_numbers(input_string):
        pattern = r'\((-?\d+\.?\d*)\s*([+-])\s*(-?\d+\.?\d*)i\)'
        matches = re.findall(pattern, input_string)
        print(f"The matches are {matches}")
        complex_numbers = []
        for j in range(0, len(matches)):
            for i in range(0, len(matches[0])):
                if matches[j][i] == "-":
                    matches[j][i + 1] = "-" + matches[j][i + 1]

            complex_numbers.append(complex(float(matches[j][0]), float(matches[j][2])))
        print(complex_numbers)
        return complex_numbers


    complex_number_list = extract_complex_numbers(input_string)
    print(f"The correct answer is {complex_number_list[0] + complex_number_list[1]}")

if problemType == "simultaneousEquations":

    input_string = replace_double_minus(input_string)
    input_string = input_string.replace(" ", "")
    equations = input_string.splitlines()
    print(equations)
    # print(input_string)

    newList = re.findall(r'[-+]?(?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d+)?', input_string)

    for num in newList:
        num = float(num)

    print(newList)
    numArray = np.array([[newList[0], newList[1]],
                        [newList[3], newList[4]]])
    answerArray = np.array([newList[2], newList[5]])
    numArray = numArray.astype('float64')
    answerArray = answerArray.astype('float64')
    numArrayInverse = np.linalg.inv(numArray)
    answer = np.matmul(numArrayInverse, answerArray)
    print(f"X is {answer[0]} and Y is {answer[1]}")