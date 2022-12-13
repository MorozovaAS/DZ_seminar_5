#Для натурального n создать словарь индекс-значение,
# состоящий из элементов последовательности 3n + 1


a = [x for x in range(1,6)]
b = map(lambda i: 3*i+1, [x for x in range(1,6)])
print(dict(zip(a,b)))
