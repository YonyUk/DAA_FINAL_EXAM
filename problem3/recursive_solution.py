from problem3.tester import is_good_secuence

def solve(array):
    return find_longest_good_sequence(array,[],1)

def find_longest_good_sequence(array,current_seq,index):
    if index == len(array) + 2:
        return current_seq if is_good_secuence(array,current_seq) else []
    
    include_seq = find_longest_good_sequence(array,current_seq + [index],index + 1)
    exclude_seq = find_longest_good_sequence(array,current_seq,index + 1)
    
    return include_seq if len(include_seq) > len(exclude_seq) else exclude_seq
    