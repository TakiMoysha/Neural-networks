import random


#       1
#      ====
#     |    |
#   2 |    | 3
#      ====
#     | 4  |
#   5 |    | 6
#      ====
#       7
# 0 - мнимый


# входящий сигнал
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


number = random.choice(nums) # Ссылка на одно из чисел указанных чисел, подающихся на нейросеть


class Neuron(object):
    def __init__(self):
        self.weight = [round(random.random(), 4) for i in range(8)]

    def about(self):
        print(self.weight)

    def work(self, num):
        bias = 5  # Пороговое значение

        # Рассчитываем взвешенную сумму
        net = 0
        for i in range(len(num)):
            net += int(num[i])*self.weight[i]
        # Превышен ли порог? (Да - сеть думает, что это 5. Нет - сеть думает, что это другая цифра)
        return net >= bias

    def lerning(self, N, lerNumber):
        # Уменьшение значений весов, если сеть ошиблась и вернула 1
        def decrease(number, weight=0.2):
            for i in range(8):
                # Возбужденный ли вход
                if int(number[i]) == 1:
                    # Уменьшаем связанный с ним вес на единицу
                    self.weight[i] -= weight
                    # print(self.weight)

        # Увеличение значений весов, если сеть ошиблась и выдала 0
        def increase(number, weight=0.2):
            for i in range(8):
                # Возбужденный ли вход
                if int(number[i]) == 1:
                    # Увеличиваем связанный с ним вес на единицу
                    self.weight[i] += weight
                    # print(self.weight)


        # N - кол-во циклов обучения
        for i in range(N):
            option = random.randint(0, 9)
            # Если получилось НЕ число 5
            if option != lerNumber:
                # Если сеть выдала True/Да/1, то наказываем ее
                if self.work(nums[option]):
                    decrease(nums[option])
            # Если получилось число 5
            else:
                # Если сеть выдала False/Нет/0, то показываем, что эта цифра - то, что нам нужно
                if not self.work(nums[lerNumber]):
                    increase(nums[lerNumber])



# Проверка нейрона, правильно ли он работает
def test(Neuron):
    Neuron.about()
    print("0", Neuron.work(num0))
    print("1", Neuron.work(num1))
    print("2", Neuron.work(num2))
    print("3", Neuron.work(num3))
    print("4", Neuron.work(num4))
    print("5", Neuron.work(num5))
    print("6", Neuron.work(num6))
    print("7", Neuron.work(num7))
    print("8", Neuron.work(num8))
    print("9", Neuron.work(num9))

# ф-ция выдает результат, что это за число
def net(neurons, number):
    sum = 0*int(neurons[0].work(number)) + 1*int(neurons[1].work(number)) + \
            2*int(neurons[2].work(number)) + 3*int(neurons[3].work(number)) + \
            4*int(neurons[4].work(number)) + 5*int(neurons[5].work(number)) + \
            6*int(neurons[6].work(number)) + 7*int(neurons[7].work(number)) + \
            8*int(neurons[8].work(number)) + 9*int(neurons[9].work(number))
    print(number, "\nДумаю это: " + str(sum))

# --------------------------------------------------------------------------------

#  Обучение нейронов
neurons = [Neuron() for i in range(10)] # Слой из 10 нейронов
for i in range(len(neurons)):
    neurons[i].lerning(1000, i)
    # test(neurons[i])  # проверка каждого нейрона


# Проверка сети
for i in range(len(nums)):
    print("\nОтвет:", i)
    net(neurons, nums[i])

print("\n\n---------на вход подается------------")
net(neurons, number)
