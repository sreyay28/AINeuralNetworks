import math
import sys

def transfer1(val):
    return val

def transfer2(val):
    if val > 0:
        return val
    return 0

def transfer3(val):
    denom = 1 + math.exp(-val)
    return (1 / denom)

def transfer4(val):
    denom = 1 + math.exp(-val)
    frac = 2 / denom
    return frac - 1

def do_function(inputs, file, transfer):
    lines = file.readlines()
    new_input = []
    if(len(lines) == 1):
        line = lines[0]
        line = line.rstrip('\n')
        weights = list(map(float, line.split()))
        new_input = []
        count = 0
        temp_sum = 0
        for i in range(0, len(weights)):
            temp_sum += inputs[count] * weights[i]
            new_input.append(temp_sum)
        return new_input
    for i in range(len(lines)-1):
        line = lines[i]
        line = line.rstrip('\n')
        weights = list(map(float, line.split()))
        new_input = []
        count = 0
        temp_sum = 0
        for i in range(0, len(weights)):
            temp_sum += inputs[count] * weights[i]
            count += 1
            if(count >= len(inputs)):
                if(transfer == "T1"):
                    new_input.append(transfer1(temp_sum))
                if (transfer == "T2"):
                    new_input.append(transfer2(temp_sum))
                if (transfer == "T3"):
                    new_input.append(transfer3(temp_sum))
                if (transfer == "T4"):
                    new_input.append(transfer4(temp_sum))
                count = 0
                temp_sum = 0
        inputs = new_input
    result = []
    last_line = lines[len(lines)-1]
    last_line = list(map(float, last_line.split()))
    for i in range(0, len(new_input)):
        result.append(new_input[i] * last_line[i])
    return result

def format_result(result):
    for i in result:
        print(i, end = " ")
    print()

input = list(sys.argv)
input = input[1:]
filename = input[0]
transfer = input[1]
inputs = []

for i in range(len(input)):
    if (i > 1):
        inputs.append(float(input[i]))

file = open(filename, "r")
answer = do_function(inputs, file, transfer)
format_result(answer)

