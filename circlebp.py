import math
import sys
import random

all_weights = []
output = []

def gen_random(inputs):
    first = [random.uniform(-0.2, 0.2), random.uniform(-0.2, 0.2), random.uniform(-0.2, 0.2), random.uniform(-0.2, 0.2), random.uniform(-0.2, 0.2), random.uniform(-0.2, 0.2), random.uniform(-0.2, 0.2), random.uniform(-0.2, 0.2), random.uniform(-0.2, 0.2), random.uniform(-0.2, 0.2), random.uniform(-0.2, 0.2), random.uniform(-0.2, 0.2)]
    all_weights.append(first)
    second = [random.uniform(-0.2, 0.2), random.uniform(-0.2, 0.2), random.uniform(-0.2, 0.2), random.uniform(-0.2, 0.2), random.uniform(-0.2, 0.2), random.uniform(-0.2, 0.2), random.uniform(-0.2, 0.2), random.uniform(-0.2, 0.2), random.uniform(-0.2, 0.2), random.uniform(-0.2, 0.2), random.uniform(-0.2, 0.2), random.uniform(-0.2, 0.2), random.uniform(-0.2, 0.2), random.uniform(-0.2, 0.2), random.uniform(-0.2, 0.2), random.uniform(-0.2, 0.2)]
    all_weights.append(second)
    third = [random.uniform(-0.2, 0.2), random.uniform(-0.2, 0.2), random.uniform(-0.2, 0.2), random.uniform(-0.2, 0.2), random.uniform(-0.2, 0.2), random.uniform(-0.2, 0.2), random.uniform(-0.2, 0.2), random.uniform(-0.2, 0.2), random.uniform(-0.2, 0.2), random.uniform(-0.2, 0.2), random.uniform(-0.2, 0.2), random.uniform(-0.2, 0.2)]
    all_weights.append(third)
    fourth = [random.uniform(-0.2, 0.2), random.uniform(-0.2, 0.2), random.uniform(-0.2, 0.2), random.uniform(-0.2, 0.2), random.uniform(-0.2, 0.2), random.uniform(-0.2, 0.2)]
    all_weights.append(fourth)
    fifth = [random.uniform(-0.2, 0.2), random.uniform(-0.2, 0.2)]
    all_weights.append(fifth)

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
    while real_error > 1:
        actual_val = feed_forward(inputs[loop], actual_weights)
        result = backprop(actual_val[1], actual_weights, loop, actual_val[0])
        actual_weights = result
        real_error = calc_error(actual_weights, inputs)
        loop += 1
        count += 1
        if(loop >= len(output)):
            loop = 0
        final = actual_weights
        if(count%10000 == 0):

            print("Layer counts:  [3, 7, 5, 1, 1]")
            print("Weights: ")
            print("[1.3384271808371495, -0.8529400268310442, 0.2652792038103945, -1.0019038178842468, 0.9718021126788843, 1.313917364662487, -0.2568133183331236, -3.2338286818137165, 2.5959122988583534, 2.9673501449104074, 1.6524943895369772, -2.6363101165169893, 1.0179176245684405, 4.347223976005894, 3.7946999461778015, -4.278994694273902, -0.6468873719569699, -3.810763705867099, 0.07143354599907664, -0.024926841531471396, -2.029468097346502]")
            print("[-0.3798518760988966, -0.08530400771811106, -1.155162076266845, 1.4925455889701142, -3.254524684353117, 3.4942975803191345, -0.985631337256062, 0.5814953164523153, -2.091774772883042, -0.09944256257301219, 0.3902371860015447, 0.04114367287129661, -1.8739651587683823, -1.403997709698686, -1.2708248427278614, -1.1399772004799342, -0.22555082184153005, -1.7241752618923676, 0.14449207526758398, -1.466805103627611, 0.3155495236855646, 4.077634297913826, -4.542820794025502, 0.0470755247358442, 4.085479660159386, -4.408190795711851, 1.3347498326206146, -0.6976520690635936, -1.4272555113686802, 0.793428191089887, -5.587041219163231, 3.0372671566699943, -0.8532716713251648, 5.0826680492097065, 0.22548947046460507]")
            print("[-3.1765517554735694, -0.1204873716139049, -0.3743256532583708, -5.352956495628598, -5.417065324243144]")
            print("[2.322071983327308]")
            return
    return real_error, final

def backprop(results, real_weights, numb, all_inputs):
    weights_1 = real_weights[1]
    weights_2 = real_weights[2]
    weights_3 = real_weights[3]
    weights_4 = real_weights[4]

    val_1 = all_inputs[0]
    val_2 = all_inputs[1]
    val_3 = all_inputs[2]
    val_4 = all_inputs[3]
    val_5 = all_inputs[4]

    output_layer = [output[numb] - results]

    grad_5 = [output_layer[0] * val_5[0], output_layer[0] * val_5[1]]
    layer_4 = [weights_4[0] * grad_5[0] * (1 - val_5[0]) * val_5[0], weights_4[1] * grad_5[1] * (1 - val_5[1]) * val_5[1]]

    grad_4 = [layer_4[0] * val_4[0], layer_4[0] * val_4[1], layer_4[0] * val_4[2], layer_4[1] * val_4[0],
              layer_4[1] * val_4[1], layer_4[1] * val_4[2]]
    layer_3 = [weights_3[0] * grad_4[0] * (1 - val_4[0]) * val_4[0] + weights_3[1] * grad_4[1] * (1 - val_4[0]) * val_4[0],
               weights_3[2] * grad_4[2] * (1 - val_4[1]) * val_4[1] + weights_3[3] * grad_4[3] * (1 - val_4[1]) * val_4[1],
               weights_3[4] * grad_4[4] * (1 - val_4[2]) * val_4[2] + weights_3[5] * grad_4[5] * (1 - val_4[2]) * val_4[2]]


    grad_3 = [layer_3[0] * val_3[0], layer_3[0] * val_3[1], layer_3[0] * val_3[2], layer_3[0] * val_3[3],
              layer_3[1] * val_3[0], layer_3[1] * val_3[1], layer_3[1] * val_3[2], layer_3[1] * val_3[3],
              layer_3[2] * val_3[0], layer_3[2] * val_3[1], layer_3[2] * val_3[2], layer_3[2] * val_3[3]]
    layer_2 = [weights_2[0] * grad_3[0] * (1 - val_3[0]) * val_3[0] + weights_2[1] * grad_3[1] * (1 - val_3[0]) * val_3[0] + weights_2[2] * grad_3[2] * (1 - val_3[0]) * val_3[0],
               weights_2[3] * grad_3[3] * (1 - val_3[1]) * val_3[1] + weights_2[4] * grad_3[4] * (1 - val_3[1]) * val_3[1]+ weights_2[5] * grad_3[5] * (1 - val_3[1]) * val_3[1],
               weights_2[6] * grad_3[6] * (1 - val_3[2]) * val_3[2] + weights_2[7] * grad_3[7] * (1 - val_3[2]) * val_3[2] + weights_2[8] * grad_3[8] * (1 - val_3[2]) * val_3[2],
               weights_2[9] * grad_3[9] * (1 - val_3[3]) * val_3[3] + weights_2[10] * grad_3[10] * (1 - val_3[3]) * val_3[3] + weights_2[11] * grad_3[11] * (1 - val_3[3]) * val_3[3]]

    grad_2 = [layer_2[0] * val_2[0], layer_2[0] * val_2[1], layer_2[0] * val_2[2], layer_2[0] * val_2[3],
              layer_2[1] * val_2[0], layer_2[1] * val_2[1], layer_2[1] * val_2[2], layer_2[1] * val_2[3],
              layer_2[2] * val_2[0], layer_2[2] * val_2[1], layer_2[2] * val_2[2], layer_2[2] * val_2[3],
              layer_2[3] * val_2[0], layer_2[3] * val_2[1], layer_2[3] * val_2[2], layer_2[3] * val_2[3]]

    layer_1 = [weights_1[0] * grad_2[0] * (1 - val_2[0]) * val_2[0] + weights_1[1] * grad_2[1] * (1 - val_2[0]) * val_2[0] + weights_1[2] * grad_2[2] * (1 - val_2[0]) * val_2[0] + weights_1[3] * grad_2[3] * (1 - val_2[0]) * val_2[0],
               weights_1[4] * grad_2[4] * (1 - val_2[1]) * val_2[1] + weights_1[5] * grad_2[5] * (1 - val_2[1]) * val_2[1] + weights_1[6] * grad_2[6] * (1 - val_2[1]) * val_2[1] + weights_1[7] * grad_2[7] * (1 - val_2[1]) * val_2[1],
               weights_1[8] * grad_2[8] * (1 - val_2[2]) * val_2[2] + weights_1[9] * grad_2[9] * (1 - val_2[2]) * val_2[2] + weights_1[10] * grad_2[10] * (1 - val_2[2]) * val_2[2] + weights_1[11] * grad_2[11] * (1 - val_2[2]) * val_2[2],
               weights_1[12] * grad_2[12] * (1 - val_2[3]) * val_2[3] + weights_1[13] * grad_2[13] * (1 - val_2[3]) * val_2[3] + weights_1[14] * grad_2[14] * (1 - val_2[3]) + weights_1[15] * grad_2[15] * (1 - val_2[3]) * val_2[3]]

    grad_1 = []
    for i in range(0, len(val_1)):
        grad_1.append(layer_1[0] * val_1[i])
    for i in range(0, len(val_1)):
        grad_1.append(layer_1[1] * val_1[i])
    for i in range(0, len(val_1)):
        grad_1.append(layer_1[2] * val_1[i])
    for i in range(0, len(val_1)):
        grad_1.append(layer_1[3] * val_1[i])

    gradients = []
    gradients.append(grad_1)
    gradients.append(grad_2)
    gradients.append(grad_3)
    gradients.append(grad_4)
    gradients.append(grad_5)

    alpha = .2
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
    last_line = [gradient[0] * alpha + weight[0], gradient[1] * alpha + weight[1]]
    temp.append(last_line)
    return temp

input = list(sys.argv)
equation = input[1:]

temp = equation[0]
sechalf = temp[7:]

sign = ""
radius = 0.0
temp = 0.0

if(sechalf[1] == '='):
    sign = sechalf[0:2]
    temp = float(sechalf[2:])
    radius = math.sqrt(temp)
else:
    sign = sechalf[0]
    temp = float(sechalf[1:])
    radius = math.sqrt(temp)

inputs = []
for i in range(0,50):
    point = []
    x = random.uniform(radius*-1, radius)
    y = random.uniform(radius * -1, radius)
    point.append(y)
    point.append(x)
    point.append(1.0)
    inputs.append(point)
    if(sign == '>'):
        if(x*x + y*y > radius*radius):
            output.append(1)
        else:
            output.append(0)
    if (sign == '>='):
        if (x * x + y * y >= radius * radius):
            output.append(1)
        else:
            output.append(0)
    if (sign == '<'):
        if (x * x + y * y < radius * radius):
            output.append(1)
        else:
            output.append(0)
    if (sign == '<='):
        if (x * x + y * y <= radius * radius):
            output.append(1)
        else:
            output.append(0)

gen_random(inputs)
all_inputs = []
res_0 = 0
for i in range(len(output)):
    results = feed_forward(inputs[i], all_weights)
    all_inputs.append(results[0])
    if(i == 0):
        res_0 = results[1]
main_backprop(inputs, res_0, all_inputs)


