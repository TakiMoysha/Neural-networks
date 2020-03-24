import neuron

num0 = list('11110111')  # должен вернуть 0
num1 = list('10100100')  # должен вернуть 1
num2 = list('11011101')  # должен вернуть 2
num3 = list('11101101')  # должен вернуть 3
num4 = list('10101110')  # должен вернуть 4
num5 = list('11101011')  # должен вернуть 5
num6 = list('11111011')  # должен вернуть 6
num7 = list('10100101')  # должен вернуть 7
num8 = list('11111111')  # должен вернуть 8
num9 = list('11101111')  # должен вернуть 9
nums = [num0, num1, num2, num3, num4, num5, num6, num7, num8, num9]

# Проверка нейрона, правильно ли он работает
def test(neuron):
    neuron.about()
    print("0", neuron.work(num0))
    print("1", neuron.work(num1))
    print("2", neuron.work(num2))
    print("3", neuron.work(num3))
    print("4", neuron.work(num4))
    print("5", neuron.work(num5))
    print("6", neuron.work(num6))
    print("7", neuron.work(num7))
    print("8", neuron.work(num8))
    print("9", neuron.work(num9))

# ф-ция выдает результат, что это за число
def net(neurons, number):
    sum = 0*int(neurons[0].work(number)) + 1*int(neurons[1].work(number)) + \
            2*int(neurons[2].work(number)) + 3*int(neurons[3].work(number)) + \
            4*int(neurons[4].work(number)) + 5*int(neurons[5].work(number)) + \
            6*int(neurons[6].work(number)) + 7*int(neurons[7].work(number)) + \
            8*int(neurons[8].work(number)) + 9*int(neurons[9].work(number))
    print(number, "\nЭто: " + str(sum))

#  Обучение нейронов
neurons = [neuron.Neuron() for i in range(10)]
for i in range(len(neurons)):
    neurons[i].lerning(1000, i)
    # test(neurons[i])  # проверка каждого нейрона


# Проверка сети
for i in range(len(nums)):
    print("\nОтвет:", i)
    net(neurons, nums[i])