import sys, string, random

def main():

    # use `with open()` for automatic closing 
    with open(sys.argv[1]) as f:
        full = f.read()

        # not ignoring case can give more natural results, but needs a larger 
        # dataset 
        full = full.lower()

        # replacing . with TERM allows punctuation to be safely removed.
        # TERM will never be confused with a word in the text because it is 
        # uppercase
        full = full.replace(".", " TERM")

        # when maketrans is called with three arguments, functions normally
        # (translating arg0 to arg1), but also removes all characters in arg2
        full = full.translate(str.maketrans('', '', string.punctuation))

        # we have no punctuation to worry about (and TERM has a leading space)
        # so we can just split on whitespace
        words = full.split()

    # 'chain' is a data structure consisting of a {word: array} dict where keys
    # are each word in the dataset and values are lists of words that may follow
    # the key word
    chain = makeChain(words)

    # get a result beginning with an arbitrary word (this may be replaced by
    # `random.choice(words)` for random seeding
    print(getRes(chain, "she"))

def makeChain(text):

    # initialize chain as a dictionary of {word: empty array}. 
    #an empty array is pre-set so we don't have to worry about checking later 
    # and can just append
    chain = {}
    for word in text:
        chain[word] = []

    # we loop by index instead of item because multiple items are used at once.
    # the loop goes up to the second-to-last word because there is no word after
    # the final word
    for idx in range(len(text)-1):

        # append the next word to the current word's array
        # duplicates are kept to preserve proportionality
        chain[text[idx]].append(text[idx+1])

    return chain
    
# a function to query a given chain, starting at initial and continuing for 
# l words
def getRes(chain, initial, l = 100):

    curWord = initial
    res = initial + " "
    for i in range(l):
    
        # chain[curWord] is an array of the possible words that may follow
        # curWord. proportionality is preserved by including duplicates
        # multiple times, so random.choice will pick words with correct 
        # frequency
        curWord = random.choice(chain[curWord])
        
        res += curWord + " "

    # undo the TERM substitution to give more readable results
    # note that the leading space is removed
    res = res.replace(" TERM", ".")
    
    return res


    
    
if __name__ == "__main__":
    main()