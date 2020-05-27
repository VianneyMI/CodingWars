"""
Sum of Digits/Digital Root

Instructions : In this kata, you must create a digital root function.
A digital root is the recursive sum of all the digits in a number. 
Given n, take the sum of the digits of n. 
If that value has more than one digit, continue reducing in this way until a single-digit number is produced. 
This is only applicable to the natural numbers.
"""
def digital_root(n):
    n_string=str(n)
    n_temp=n
    while(n_temp>9):
        n_temp=0
        for digit in n_string:
            n_temp+=int(digit)
        n_string=str(n_temp)
    return n_temp

"""
Bit Counting

Instructions : Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. 
You can guarantee that input is non-negative.

Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case
"""
def countBits(n):
    n_binary='{0:b}'.format(n) #converting input number into his binary representation as a string
    bit_count=0                #Initializing the variable that will count the number of bits equal to 1
    for c in n_binary:         #Loop checking all characters making up the binary representation of the input number
        if c=='1':
            bit_count+=1
    return bit_count

"""
Regex validate PIN code

Instructions : ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.
If the function is passed a valid PIN string, return true, else return false
"""
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
    if isinstance(r,int) and isinstance(g,int) and isinstance(b,int): #Checking the inputs are integers
        temp=[]
        for c in [r,g,b]:#Processing out of bonds values
            c=max(0,c)
            c=min(255,c)
            
            C=hex(c).replace('0x','').upper()#Converting each color its hexadecimal string representation
            if len(C)<2:
                C='0'+C
            temp.append(C)
            
        return "".join(temp)    
    else :
        print("Input must be integers")
    
""" Where my anagrams at?
Instructions : Write a function that will find all the anagrams of a word from a list. 
You will be given two inputs a word and an array with words. 
You should return an array of all the anagrams or an empty array if there are none. 
"""
def anagrams(word,words):
    anagrams=[]
    for anagram in words:
        if dict_compare(word_decompose(anagram),word_decompose(word)):
            anagrams.append(anagram)
    return anagrams

def word_decompose(word):
### Return a dictionary where the keys are the letters of the word passed as input parameter and the values are the number of instance
    letter_count={letter:0 for letter in word}
    for letter in word:
        letter_count[letter]+=1
    return letter_count

def dict_compare(dictA,dictB):
###Compare if two dictionaries exactly the same (key,value) pairs
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

"""
Convert string to camel case

Instructions : Complete the method/function so that it converts dash/underscore delimited words into camel casing. 
The first word within the output should be capitalized only if the original word was capitalized 
(known as Upper Camel Case, also often referred to as Pascal case). 
"""

def to_camel_case(text):
    new_text=list(text) #Converting string to list which are easier to manipulate
    for i,letter in enumerate(new_text):#Iterating through the characthers to find the hypen/underscores
        if letter in ['_','-']:
            new_text[i+1]=new_text[i+1].upper()#Replacing the letter following the underscore with an Uppercase
    new_text="".join(new_text)
    new_text=new_text.replace('_','')#Removing the hypens/underscore
    new_text=new_text.replace('-','')
    return new_text     

