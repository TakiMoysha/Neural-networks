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
        def decrease(number):
            for i in range(8):
                # Возбужденный ли вход
                if int(number[i]) == 1:
                    # Уменьшаем связанный с ним вес на единицу
                    self.weight[i] -= 0.1
                    # print(self.weight)

        # Увеличение значений весов, если сеть ошиблась и выдала 0
        def increase(number):
            for i in range(8):
                # Возбужденный ли вход
                if int(number[i]) == 1:
                    # Увеличиваем связанный с ним вес на единицу
                    self.weight[i] += 0.1
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

#
# ner = Neuron()
# ner.about()
# ner.lerning(1000, 5)
# print("0", ner.work(num0))
# print("1", ner.work(num1))
# print("2", ner.work(num2))
# print("3", ner.work(num3))
# print("4", ner.work(num4))
# print("5", ner.work(num5))
# print("6", ner.work(num6))
# print("7", ner.work(num7))
# print("8", ner.work(num8))
# print("9", ner.work(num9))
# ner.about()