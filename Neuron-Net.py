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

def test(ner):
    ner.about()
    print("0", ner.work(num0))
    print("1", ner.work(num1))
    print("2", ner.work(num2))
    print("3", ner.work(num3))
    print("4", ner.work(num4))
    print("5", ner.work(num5))
    print("6", ner.work(num6))
    print("7", ner.work(num7))
    print("8", ner.work(num8))
    print("9", ner.work(num9))


neurons = [neuron.Neuron() for i in range(10)]
for i in range(len(neurons)):
    neurons[i].lerning(1000, i)
    test(neurons[i])


