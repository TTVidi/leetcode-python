import random


def partition(a, begin, end):
    if begin < end:
        i = begin
        j = end
        middle = a[i]
        while i < j:
            while a[j] >= middle and i < j:
                j -= 1
            a[i] = a[j]
            while a[i] <= middle and i < j:
                i += 1
            a[j] = a[i]
        a[i] = middle
        partition(a, begin, i - 1)
        partition(a, i + 1, end)


if __name__ == '__main__':
    i = 1
    a = []
    while i < 5:
        a.append(random.randint(0, 5))
        i += 1
    partition(a, 0, a.__len__() - 1)
    print('result is : ', a)
