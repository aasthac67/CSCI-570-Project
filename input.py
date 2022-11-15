import sys

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
    return words

def get_alpha():
    
    DNA = {}
    DNA['A'], DNA['C'], DNA['T'], DNA['G'] = 0, 1, 2, 3
    
    return [[0,110,48,94], [110,0,118,48], [48,118,0,110], [94,48,110,0]], DNA

def main():
   words  = read_input(sys.argv[1])
   alpha, DNA = get_alpha()

   return 

main()


            
            
            
            
            
        