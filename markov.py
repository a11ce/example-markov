import sys, string, random

def main():
    with open(sys.argv[1]) as f:
        full = f.read()
        full = full.lower()
        full = full.replace(".", " TERM")
        full = full.translate(str.maketrans('', '', string.punctuation))
        words = full.split()
    chain = makeChain(words)
    #print(chain)
    print(getRes(chain, "it"))
    
def getRes(chain, initial, l = 100):
    curWord = initial
    res = initial + " "
    for i in range(l):
        curWord = random.choice(chain[curWord])
        res += curWord + " "

    res = res.replace(" TERM", ".")
    return res

def makeChain(text):
    chain = {}
    
    for word in text:
        chain[word] = []
        
    for idx in  range(len(text)-1):
        chain[text[idx]].append(text[idx+1])

    return chain
    
    
if __name__ == "__main__":
    main()