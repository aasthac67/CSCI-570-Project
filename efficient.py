import time 
import timeit
import sys
from resource import *
import time
import psutil

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


def sequence_alignment(x, y):
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
                
    #print(dp[m][n])
    return  form_sequence(dp, x, y)

def form_sequence(dp, s1, s2):
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
    
    return [newx[::-1], newy[::-1], dp[m][n]]

def sequence_alignment_forward(x, y, d=30):
    m = len(y)
    n = len(x)
    dp = [[0]*(m+1) for j in range(2)]

    for i in range(m+1):
        dp[0][i] = i*d


    for i in range(1,n+1):
        dp[1][0] = dp[0][0] + d

        for j in range(1, m+1):
            dp[1][j] = min(alpha[x[i-1]+y[j-1]] + dp[0][j-1], d + dp[1][j-1], d +dp[0][j])

        for i in range(0,m+1):
                dp[0][i] = dp[1][i]
    #print(dp[1])
    return dp[1] 

def sequence_alignment_backward(x, y, d=30): 
	m = len(y)
	n = len(x)
	dp = [[0]*(m+1) for j in range(2)]

	for i in range(m+1):
		dp[0][i] = i*d


	for i in range(1,n+1):
		dp[1][0] = dp[0][0] + d

		for j in range(1, m+1):
			dp[1][j] = min(alpha[x[n-i]+y[m-j]] + dp[0][j-1], d + dp[1][j-1], d+ dp[0][j])

		for i in range(0, m+1):
			dp[0][i] = dp[1][i]

	return dp[1]


def divandconq(x, y): 
    m=len(y)
    n=len(x)
    if m<2 or n<2:
        return sequence_alignment(x, y)
    
    x_prefix = sequence_alignment_forward(x[:n//2], y)
    
    x_suffix = sequence_alignment_backward(x[n//2:], y)
    #print("X")
    #print(x_prefix)

    partition = []

    for j in range(m+1):
        partition.append(x_prefix[j] + x_suffix[m-j])
    min_element = min(partition)

	# find min partition index
    idx = -1
    for j in range(len(partition)):
        if partition[j] == min_element:
            idx = j
            break
    point= idx
    x_prefix = [] 
    x_suffix = []
    partition = []

    left_side = divandconq(x[:n//2], y[:point])
    right_side  = divandconq(x[n//2:], y[point:])
    ans = []
 
    for i in range(3):
        key = left_side[i] + right_side[i]
        ans.append(key)

    return ans


'''
def write_output(filename, ans):

	f = open(filename, "w+")

	
	f.write(ans[0][:50]+" "+ ans[0][-50:]+'\n')
	f.write(ans[1][:50]+" "+ ans[1][-50:]+'\n')
	f.write(str(ans[2])+'\n')

	
	f.write(str(h.heap().size/10**3)+'\n')
	f.write(str(time.time()- start_time)+'\n')

	f.close()
'''


def process_memory():
    process = psutil.Process()
    memory_info = process.memory_info()
    memory_consumed = int(memory_info.rss/1024)
    return memory_consumed

def get_penalty():
    delta = 30
    
    alpha = {'AA': 0, 'CC': 0, 'GG': 0, 'TT': 0, 'AC': 110, 'CA': 110, 'AG': 48, 'GA': 48, 'AT': 94, 'TA': 94,
             'CG': 118, 'GC': 118, 'CT': 48, 'TC': 48, 'GT': 110, 'TG': 110}
    
    return alpha, delta

def time_wrapper(s1, s2):
    start_time = time.time()

    #Call algorithms
    global alpha
    global delta
    alpha, delta = get_penalty()
    
    ans = divandconq(s1,s2)
    #newx, newy = form_sequence(dp, s1, s2, alpha, delta)
    end_time = time.time()
    time_taken = (end_time - start_time)*1000
    print(time_taken)
    return ans

def main():
    words = read_input(sys.argv[1])
    
    s1, s2 = words[0], words[1]
    
    print(time_wrapper(s1, s2))
    print(process_memory())
    #ans = divandconq(s1, s2)
	#print(ans)
    return 
	#write_output('output.txt', ans)

main()
