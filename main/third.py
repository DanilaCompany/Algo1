import numpy as np


def numpy_fizzbuzz(N: int) -> str:
    integers = np.arange(1, N)
    result = np.arange(1, N).astype(str)

    mod_3 = np.argwhere(integers % 3 == 0)
    mod_5 = np.argwhere(integers % 5 == 0)

    mod_15 = np.intersect1d(mod_3, mod_5, assume_unique=True)

    result[mod_3] = 'fizz'
    result[mod_5] = 'buzz'
    result[mod_15] = 'fizzbuzz'

    return " ".join(result)


print(numpy_fizzbuzz(100))