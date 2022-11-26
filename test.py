#import bharat_basic as bb
import basic as b
import sys
#import bharat_efficient as be

#bharat_ans = bb.bharat_main()

#m,n = bharat_ans[0], bharat_ans[1]

#m1, n1 = b.main()
#ans = be.main()

#print(ans)
f = sys.argv[1]
o = sys.argv[2]
def check_string(m,n):
    for i in range(len(m)):
        if m[i] != n[i]:
            return False
        else:
            continue
    return True
        
with open(o, 'r') as file:

    m, n = b.main(f)
    lines = file.readlines()
    print("Line 1")
    print(m)
    print(lines[1])
    print("############################################################")
    print("Line 2")
    print(n)
    print(lines[2])
    
    print(check_string(m,lines[1]))
    print(check_string(n,lines[2]))


    file.close()
