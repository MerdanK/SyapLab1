from random import randint
import numpy

a = [0 for i in range(10)]
i = 0;

for i in range(10):
    a[i] = [randint(100,300) for i in range(10)]

for i in range(10):
    print(a[i], "среднего ар число : ",numpy.mean(a[i]))