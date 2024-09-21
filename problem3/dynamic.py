from problem3.tester import is_good_secuence

def dynamic_solve(array):
    
    dp = [[] for _ in range(len(array) + 2)]
    for i in range(1,len(dp) + 2):
        dp[i] = [i]
        for j in range(1,i):
            temp_seq = dp[i] + [j]
            if is_good_secuence(array,temp_seq) and len(temp_seq) > len(dp[i]):
                dp[i] = temp_seq
                pass
            pass
        pass
    
    longest_seq = []
    for seq in dp:
        if len(seq) > longest_seq:
            longest_seq = seq
            pass
        pass
    return longest_seq