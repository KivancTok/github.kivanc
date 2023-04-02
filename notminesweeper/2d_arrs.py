from arr2D import Array2D

array = Array2D.zero(13, 17, '2D array')


def lsrepr(slc):
    start = '' if slc.start is None else str(slc.start)
    stop = '' if slc.stop is None else str(slc.stop)
    step = '' if slc.step is None else str(slc.step)
    return f'{start}:{stop}:{step}'


for i in range(13):
    for j in range(17):
        array[i, j] = i * j
print(array)

print(array[::2, ::3])
print(array[5, ::2])
print(array[::3, 2])
print(array.get_neighbors(1, 1, 16, 0))
