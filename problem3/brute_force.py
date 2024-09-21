from itertools import combinations
from problem3.tester import is_good_secuence

def brute_force(B):
    
    N = len(B)
    best_sequence = []
    for k in range(1,N + 2):
        for seq in combinations(range(1,N + 2),k):
            if is_good_secuence(B,seq):
                if len(best_sequence) == 0 or len(seq) > len(best_sequence[0]):
                   best_sequence = []
                   best_sequence.append(list(seq))
                   pass
                elif len(seq) == len(best_sequence[0]):
                   best_sequence.append(list(seq))
                   pass
                pass
            pass
        pass
    return best_sequence