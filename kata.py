def digital_root(n):
    n_string=str(n)
    n_temp=n
    while(n_temp>9):
        n_temp=0
        for digit in n_string:
            n_temp+=int(digit)
        n_string=str(n_temp)
    return n_temp

def validate_pin(pin):
    check=True
    banned=[',',';','.','-','_','+','#',' ']
    for item in banned:
       if item in pin:
           check=False
    if check==True:
        try:
            int(pin)
            check=len(pin)==4 or len(pin)==6
        except ValueError:
            check=False
            print('Your pin should contain numbers only')
    return check

def rgb(r,g,b):
    if isinstance(r,int) and isinstance(g,int) and isinstance(b,int):
        temp=[]
        for c in [r,g,b]:
            c=max(0,c)
            c=min(255,c)
            
            C=hex(c).replace('0x','').upper()
            if len(C)<2:
                C='0'+C
            temp.append(C)
            
        return "".join(temp)    
    else :
        print("Input must be integers")

def anagrams(word,words):
    anagrams=[]
    for anagram in words:
        if dict_compare(word_decompose(anagram),word_decompose(word)):
            anagrams.append(anagram)
    return anagrams

def word_decompose(word):
    letter_count={letter:0 for letter in word}
    for letter in word:
        letter_count[letter]+=1
    return letter_count

def dict_compare(dictA,dictB):
    if set(dictA)==set(dictB):
        matches=[]
        for key in dictA:
            if dictA[key]==dictB[key]:
                matches.append(1)
            else:
                matches.append(0)
        if sum(matches)==len(dictA):
            return True
        else:
            return False
    else:
        return False