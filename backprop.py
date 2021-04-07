import math
import sys
import random

all_weights = []
output = []

def gen_random(inputs):
    num = (len(inputs[0])) * 2
    #first = []
    #for i in range(num):
    #   first.append(random.uniform(-0.2, 0.2))
    #all_weights.append(first)
    #second = [random.uniform(-0.2, 0.2), random.uniform(-0.2, 0.2)]
    #all_weights.append(second)
    #third = [random.uniform(-0.2, 0.2)]
    #all_weights.append(third)
    print(all_weights)
    all_weights.append([1.35, -1.34, -1.66, -0.55, -0.9, -0.58, -1.0, 1.78])
    all_weights.append([-1.08, -0.7])
    all_weights.append([-0.6])
def transfer3(val):
    denom = 1 + math.exp(-val)
    return (1 / denom)

def feed_forward(inputs, my_weights):
    all_inputs = []
    all_inputs.append(inputs)
    for i in range(len(my_weights) - 1):
        weights = my_weights[i]
        new_input = []
        count = 0
        temp_sum = 0
        for i in range(0, len(weights)):
            temp_sum += inputs[count] * weights[i]
            count += 1
            if(count >= len(inputs)):
                new_input.append(transfer3(temp_sum))
                count = 0
                temp_sum = 0
        all_inputs.append(new_input)
        inputs = new_input
    result = 0.0
    last_line = my_weights[len(my_weights)-1]
    for i in range(0, len(new_input)):
        all_inputs.append([new_input[i] * last_line[i]])
        result = new_input[i] * last_line[i]
    return all_inputs, result

def format_result(result):
    for i in result:
        print(i, end = " ")
    print()

def calc_error(weights, inputs):
    error = 0
    for i in range(len(output)):
        val_1 = feed_forward(inputs[i], weights)
        error += (output[i] - val_1[1]) * (output[i] - val_1[1]) * 0.5
    return error

def main_backprop(inputs, results, all_inputs):
    final = []
    loop = 0
    count = 0
    result = backprop(results, all_weights, 0, all_inputs[0])
    real_error = calc_error(result, inputs)
    actual_weights = result
    #while real_error > 0.01:
     #   actual_val = feed_forward(inputs[loop], actual_weights)
     #   result = backprop(actual_val[1], actual_weights, loop, actual_val[0])
     #   actual_weights = result
     #   real_error = calc_error(actual_weights, inputs)
     #   print(real_error)
     #   loop += 1
     #   count += 1
     #   if(loop >= len(output)):
     #       loop = 0
        #final = actual_weights
    return real_error, final

def backprop(results, real_weights, numb, all_inputs):
    weights_1 = real_weights[1]
    weights_2 = real_weights[2]
    val_1 = all_inputs[0]
    val_2 = all_inputs[1]
    val_3 = all_inputs[2]

    output_layer = [output[numb] - results]
    grad_3 = [output_layer[0] * val_3[0]]
    layer_2 = [weights_2[0] * grad_3[0] * (1 - val_3[0])]
    grad_2 = [layer_2[0] * val_2[0], layer_2[0] * val_2[1]]
    layer_1 = [weights_1[0] * grad_2[0] * (1 - val_2[0]), weights_1[1] * grad_2[1] * (1 - val_2[1])]
    grad_1 = []
    for i in range(0, len(val_1)):
        grad_1.append(layer_1[0] * val_1[i])
    for i in range(0, len(val_1)):
        grad_1.append(layer_1[1] * val_1[i])
    gradients = []
    gradients.append(grad_1)
    gradients.append(grad_2)
    gradients.append(grad_3)

    alpha = 0.2
    temp = []
    for i in range(len(gradients) - 1):
        weights = []
        gradient = gradients[i]
        weight = real_weights[i]
        for j in range(len(gradient)):
            weights.append(gradient[j] * alpha + weight[j])
        temp.append(weights)
    gradient = gradients[len(gradients)-1]
    weight = real_weights[len(real_weights)-1]
    last_line = [gradient[0] * alpha + weight[0]]
    temp.append(last_line)
    return temp

input = list(sys.argv)
input = input[1:]
filename = input[0]


file = open(filename, "r")
inputs = []
for line in file:
    line = line.split("=>")
    input = (list(map(float, line[0].split())))
    input.append(1.0)
    inputs.append(input)
    output.append(float(line[1].strip()))


gen_random(inputs)
all_inputs = []
res_0 = 0
for i in range(len(output)):
    results = feed_forward(inputs[i], all_weights)
    all_inputs.append(results[0])
    if(i == 0):
        res_0 = results[1]

final = main_backprop(inputs, res_0, all_inputs)

final_weights = final[1]

layers = []
layers.append(int(len(final_weights[0])/2))
layers.append(2)
layers.append(1)
layers.append(1)

print("Layer counts: " + str(layers))
print("Weights: ")
print(final_weights[0])
print(final_weights[1])
print(final_weights[2])


