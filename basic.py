import sys
from resource import *
import time
import psutil

def sequence_alignment(x, y, alpha, delta):
    m = len(x)
    n = len(y)

    dp = [[0 for i in range(n+1)] for j in range(m+1)]

    for i in range(1, m+1):
        dp[i][0] = i * delta
    
    for i in range(1, n+1):
        dp[0][i] = i * delta

    for i in range(1, m+1):
        for j in range(1, n+1):
            string = x[i-1] + y [j-1]
            dp[i][j] = min(dp[i-1][j-1] + alpha[string],
                                dp[i-1][j] + delta,
                                dp[i][j-1] + delta)
                
    print(dp[m][n])
    return dp

def form_sequence(dp):
    return ""

def get_penalty():
    delta = 30
    
    alpha = {'AA': 0, 'CC': 0, 'GG': 0, 'TT': 0, 'AC': 110, 'CA': 110, 'AG': 48, 'GA': 48, 'AT': 94, 'TA': 94,
             'CG': 118, 'GC': 118, 'CT': 48, 'TC': 48, 'GT': 110, 'TG': 110}
    
    return alpha, delta

def process_memory():
    process = psutil.Process()
    memory_info = process.memory_info()
    memory_consumed = int(memory_info.rss/1024)
    return memory_consumed

def time_wrapper(s1, s2):
    start_time = time.time()

    #Call algorithms
    alpha, delta = get_penalty()
    dp = sequence_alignment(s1, s2, alpha, delta)
    form_sequence(dp)
    
    end_time = time.time()
    time_taken = (end_time - start_time)*1000
    return time_taken

def main():
    s1 = "ACACACTGACTACTGACTGGTGACTACTGACTGGACTGACTACTGACTGGTGACTACTGACTGG"
    s2 = "TATTATTATACGCTATTATACGCGACGCGGACGCGTATACGCTATTATACGCGACGCGGACGCG"
    
    #time_wrapper(s1, s2)
    
    print("The time taken by the algorithm is: " + str(time_wrapper(s1, s2)))
    print("The process memory for the algorithm is: " + str(process_memory()))
    
    return

main()
