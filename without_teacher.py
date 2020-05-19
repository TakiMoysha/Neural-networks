import numpy
import math
import scipy.special
import random

def vector_generator():
    # SPoint = [random.randint(-1, 1) for i in range(2)]
    # EPoint = [random.randint(-1, 1) for i in range(2)]
    # while SPoint == EPoint:
    #     SPoint = [random.randint(-1, 1) for i in range(2)]
    #     EPoint = [random.randint(-1, 1) for i in range(2)]
    result = [random.randint(-1, 1) for i in range(4)]
    return result

class neuralNetwork(object):

    def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate):
        # self.weight = round(random.random(), 4)
        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outputnodes
        self.lr = learningrate
        # Создание весов как матриц с нормализованными значениями
        self.wih = numpy.random.normal(0.0, pow(self.hnodes, -0.5), (self.hnodes, self.inodes))
        print(self.wih)
        self.who = numpy.random.normal(0.0, pow(self.onodes, -0.5), (self.onodes, self.hnodes))
        print(self.who)
        # Ф-ция активации
        self.activation_function = lambda x: scipy.special.expit(x)

    def about(self, inputs_list):
        # преобразовать список входных значений
        # в двухмерный массив
        inputs = numpy.array(inputs_list, ndmin=2).T
        # рассчитать входящие сигналы для скрытого слоя
        hidden_inputs = numpy.dot(self.wih, inputs)
        # рассчитать исходящие сигналы для скрытого слоя
        hidden_outputs = self.activation_function(hidden_inputs)
        # рассчитать входящие сигналы для выходного слоя
        final_inputs = numpy.dot(self.who, hidden_outputs)
        # рассчитать исходящие сигналы для выходного слоя
        final_outputs = self.activation_function(final_inputs)
        return final_outputs

    def train(self, inputs_list) :
        # преобразовать список входных значений в двухмерный массив
        inputs = numpy.array(inputs_list, ndmin=2).T
        print("1\n", inputs)
        # рассчитать входящие сигналы для скрытого слоя
        hidden_inputs = numpy.dot(self.wih, inputs)
        print("2\n", hidden_inputs)
        # рассчитать исходящие сигналы для скрытого слоя
        hidden_outputs = self.activation_function(hidden_inputs)
        print("3\n", hidden_outputs)
        # рассчитать входящие сигналы для выходного слоя
        final_inputs = numpy.dot(self.who, hidden_outputs)
        print("4\n", final_inputs)
        # рассчитать исходящие сигналы для выходного слоя
        final_outputs = self.activation_function(final_inputs)
        print("5\n", final_outputs)
        # Метод Хебба. Изменение весов скрытого и выходного слоя
        self.who += self.lr * numpy.dot(final_outputs, numpy.transpose(hidden_outputs))
        # Изменение весов входного и скрытого слоя
        self.wih += self.lr * numpy.dot(hidden_outputs, numpy.transpose(inputs))
        self.lr -= 0.05
        # Метод Кохонена
        # 
        # # рассчитать входящие сигналы для выходного слоя
        # final_inputs = numpy.dot(self.who, hidden_outputs)
        # # print("4\n", final_inputs)
        # # рассчитать исходящие сигналы для выходного слоя
        # final_outputs = self.activation_function(final_inputs)
        # # print("5\n", final_inputs)
        # 
        # корректировка шага обучения
        # self.lr -= 0.05
        # # ошибки выходного слоя =
        # # (целевое значение - фактическое значение)
        # output_errors = targets - final_outputs
        # # ошибки скрытого слоя - это ошибки output_errors,
        # # распределенные пропорционально весовым коэффициентам связей
        # # и рекомбинированные на скрытых узлах
        # hidden_errors = numpy.dot(self.who.T, output_errors)
        # # обновить весовые коэффициенты для связей между
        # # скрытым и выходным слоями
        # self.who += self.lr * numpy.dot((output_errors * final_outputs * (1.0 - final_outputs)), numpy.transpose(hidden_outputs))
        # # обновить весовые коэффициенты для связей между
        # # входным и скрытым слоями
        # self.wih += self.lr * numpy.dot((hidden_errors * hidden_outputs * (1.0 - hidden_outputs)), numpy.transpose(inputs))


input_nodes = 4
hidden_nodes = 4
output_nodes = 4
learning_rate = 0.3

input_data = vector_generator()
print(input_data)

# targets_list = [i for i in range(3)]
# rand_example = math.sqrt(sum(()**2))

neo = neuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)
print(neo.about([1, 1, 1, 1]))
print("-------------\n", input_data)
# neo.train(input_data)

# Тренировка
series = 50
data_list = [vector_generator() for i in range(0, series)]
for i in data_list:
    neo.train(i)
    print("\n", neo.about([1.0, -1.0, 1, 1]))

# вывод итоговых весов
print("Итоговые веса:\n", neo.about([1.0, -1.0, 1, 1]))

set1 = [-1, -1, 1, 1]
set2 = [1, -1, -1, 1]
set3 = [1, 1, -1, -1]
set4 = [-1, 1, 1, -1]

test_data = [set1, set2, set3, set4]

# test = random.choice(test_data)
# print("\n\n", test)

print("\n\nset1\n", neo.about(set1))
print(numpy.argmax(neo.about(set1)) + 1)
# print(neo.about(set1))

print("\n\nset2\n", neo.about(set2))
print(numpy.argmax(neo.about(set2)) + 1)
# print(neo.about(set2))

print("\n\nset3\n", neo.about(set3))
print(numpy.argmax(neo.about(set3)) + 1)
# print(neo.about(set3))

print("\n\nset4\n", neo.about(set4))
print(numpy.argmax(neo.about(set4)) + 1)
# print(neo.about(set4))

# print(neo.about(random.choice(test_data)))
# neo.about([1, 1, 1, 1])
# print(numpy.argmax(neo.about(set4)) + 1)
