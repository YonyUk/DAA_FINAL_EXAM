import random

def is_good_secuence(B,sequence):
    for i in range(len(sequence)):
        for j in range(i + 1,len(sequence)):
            x_i = sequence[i]
            x_j = sequence[j]
            subarray = B[x_i - 1:x_j - 1]
            c1 = subarray.count(1)
            c0 = subarray.count(0)
            if not c1 - c0 == j - i: return False
            pass
        pass
    return True

def generate(min_size,max_size,tests_cases=100):
    for _ in range(tests_cases):
        yield [random.randint(0,1) for _ in range(random.randint(min_size,max_size))]
    pass