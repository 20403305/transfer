import numpy as np
num = 199
part = 6
input = num//part
print(input)



def ceil_to_ten_multiple(input, integer=2) -> int:
    """
    input 为输入的数字
    interger 为想要第几位向上取整，从个位开始
    """
    if isinstance(input, int) and isinstance(integer, int) and input > 0 and len(str(input)) >= integer:
        input_list = [int(digit) for digit in str(input)]
        # input_list = list(map(int, str(input)))
        if input_list[-1] == 0:
            output = convert(input_list)
        if len(input_list) == 1:
            input_list[-1] = 10
            output = convert(input_list)
        else:
            for i in range(1,integer):
                input_list[-i] = 0 
            for i in range(len(input_list)-integer+1):
                if input_list[-integer-i] +1 != 10:
                    input_list[-integer-i] = input_list[-integer-i] + 1
                    output = convert(input_list)
                    break
                else:
                    # 如果要判断的字数和输入数字的长度
                    if i == (len(input_list)-integer):
                        input_list[-integer-i] = 10
                        output = convert(input_list)
                    else:
                        input_list[-integer-i] = 0
        return output
                
            # if input_list[-integer] + 1 != 10:
            #     input_list[-integer] = input_list[-integer] + 1
            #     output = convert(input_list)
            # else:
            #     input_list[-integer] =  0
            #     if input_list[-integer-1] + 1 != 10:
            #         input_list[-integer-1] = input_list[-integer-1] + 1
            #         output = convert(input_list)
            #     else:
            #         input_list[-integer-1] = 0

    else:
        print("Invalid input")

def convert(input_list) -> int:
    if isinstance(input_list, list) and all([str(x).isdigit() for x in input_list]):
        output = ""
        for input in input_list:
            output += str(input)
        return int(output)
    else:
        print("Invalid input")

a = ceil_to_ten_multiple(9991)
print(a)

