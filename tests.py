from kata import anagrams, word_decompose, dict_compare

#print(digital_root(10))
#print(validate_pin('09876 '))
#print(rgb(1,2,3))
#print(word_decompose('word'))
#print(dict_compare(word_decompose('word'),word_decompose('word2')))

word='abba'
words=['aabb', 'bbaa', 'abab', 'baba', 'baab', 'baaab', 'abbaa', 'babaa']
print(anagrams(word,words))