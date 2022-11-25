import sys
'''
from resource import *
import time
import psutil
'''

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
            if x[i-1] == y[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                key = x[i-1] + y [j-1]
                dp[i][j] = min(dp[i-1][j-1] + alpha[key],
                                    dp[i-1][j] + delta,
                                    dp[i][j-1] + delta)
                
    print("Penalty cost: " + str(dp[m][n]))
    return dp

def form_sequence(dp, s1, s2, alpha, delta):
    m = len(s1)
    n = len(s2)
    
    i, j = m, n
    newx = ''
    newy = ''
    
    while i > 0 and j > 0:
        if s1[i-1] == s2[j-1] :
            newx += s1[i-1]
            newy += s2[j-1]
            i -= 1
            j -= 1
        else:
            key = s1[i-1] + s2[j-1]
            if dp[i][j] == dp[i-1][j-1] + alpha[key]:  # Mismatch
                newx += s1[i-1]
                newy += s2[j-1]
                i -= 1
                j -= 1
            elif dp[i][j] == dp[i][j-1] + delta:        # Gap
                newx += '_'
                newy += s2[j-1]
                j -= 1
            elif dp[i][j] == dp[i-1][j] + delta:        # Gap
                newx += s1[i-1]
                newy += '_'
                i -= 1
    
    while i > 0:
        newx += s1[i-1]
        newy += '_'
        i -= 1
    
    while j > 0:
       newx += '_'
       newy += s2[j-1]
       j -= 1
    
    return newx[::-1], newy[::-1]

def get_penalty():
    delta = 30
    
    alpha = {'AA': 0, 'CC': 0, 'GG': 0, 'TT': 0, 'AC': 110, 'CA': 110, 'AG': 48, 'GA': 48, 'AT': 94, 'TA': 94,
             'CG': 118, 'GC': 118, 'CT': 48, 'TC': 48, 'GT': 110, 'TG': 110}
    
    return alpha, delta

def read_input(f):
    DNA = ['A', 'C', 'T', 'G']
    words = []
    with open(f) as file:
        lines = file.read().splitlines()
        word = ''
        for line in lines:
            if line[0] in DNA:
                words.append(word)
                word = line
            else:
                s = 0
                s = int(line)
                word = word[:s+1] + word + word[s+1:]
        file.close()
        
    words.append(word)
    return words[1:]

'''
def process_memory():
    process = psutil.Process()
    memory_info = process.memory_info()
    memory_consumed = int(memory_info.rss/1024)
    return memory_consumed
'''

def time_wrapper(s1, s2):
    # start_time = time.time()

    #Call algorithms
    alpha, delta = get_penalty()
    dp = sequence_alignment(s1, s2, alpha, delta)
    newx, newy = form_sequence(dp, s1, s2, alpha, delta)
    print(newx)
    print(newy)
    
    '''
    end_time = time.time()
    time_taken = (end_time - start_time)*1000
    return time_taken
    '''
    return newx, newy

def main():
    words = read_input(sys.argv[1])
    # words = read_input("UploadedProject\SampleTestCases\input1.txt")
    
    s1, s2 = words[0], words[1]
    
    newx, newy = time_wrapper(s1, s2)
    
    # print("The time taken by the algorithm is: " + str(time_wrapper(s1, s2)))
    # print("The process memory for the algorithm is: " + str(process_memory()))
    
    return newx, newy

main()
