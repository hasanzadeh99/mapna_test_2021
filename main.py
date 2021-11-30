import time


old_input_value = False
flag_falling_edge = None
start = None
flag_output_mask = False
DELAY_CONST = 10            # delay time from falling edge ... .
output = None


def response_function():
    global old_input_value, flag_falling_edge, start, flag_output_mask, output

    if flag_falling_edge:
        output = True
        end = time.perf_counter()
        if end - start > DELAY_CONST:
            output = 0
            flag_falling_edge = 0
            flag_output_mask = False

    input_value = bool(int(input('Please Enter your Input Value: ')))

    if old_input_value == False and input_value == True:
        if not flag_output_mask: output = input_value
        old_input_value = input_value
        print('Input Rising Edge detected ... ')
        print(f'output is: {output}')

    elif old_input_value == False and input_value == False:
        if not flag_output_mask: output = input_value
        old_input_value = input_value
        print(f'output is: {output}')

    elif old_input_value == True and input_value == True:
        old_input_value = input_value
        if not flag_output_mask: output = input_value
        print(f'output is: {output}')

    elif old_input_value == True and input_value == False:
        start = time.perf_counter()
        print('Input Falling Edge detected ... ')
        flag_falling_edge = True
        flag_output_mask = True
        old_input_value = input_value
        print(f'output is: {output}')


if __name__ == '__main__':

    DELAY_CONST=int(input("Hello \nPlease Enter Your delay value here :"))
    while True:
        response_function()











