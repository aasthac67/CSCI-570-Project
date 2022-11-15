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


def main():
   words  = read_input(sys.argv[1])
   print(words[1])
   print('ACACTGACTACTGACTGGTGACTACTGACTGG')
   print("=======================+=======================")
   print(words[2])
   print('TATTATACGCTATTATACGCGACGCGGACGCG')
   return
