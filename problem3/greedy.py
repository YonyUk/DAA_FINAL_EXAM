def kadane(array):
    current_max = 0
    global_max = 0
    start = 0
    temp_start = 0
    end = 0

    for i in range(len(array)):
        if array[i] > current_max + array[i]:
            temp_start = i
            current_max = array[i]
        else:
            current_max += array[i]

        if current_max > global_max:
            global_max = current_max
            start = temp_start
            end = i
        
    return start,end

def get_diference(array):
    return array.count(1) - array.count(0)

def longest_good_sequence(array):
    
    def transform(val):
        if val == 0:
            return -1
        return 1
    
    start,end = kadane(list(map(transform,array)))
    k0,k1 = start,start + 1
    S = [k0]
    while True:
        if get_diference(array[k0:k1]) == 1:
            S.append(k1)
            if k1 == end + 1: break
            k0 = k1
            k1 += 1
            pass
        else:
            k1 += 1
            pass
        pass
    return list(map(lambda val: val + 1,S))
