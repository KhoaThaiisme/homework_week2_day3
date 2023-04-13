letter = 'asdfa;sdfkjasd;f'

def is_pangram(letters):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(len(letters)):
        if letters[i] in alphabet:
            return True
        
    return False
is_pangram(letter)    

def find_pangram(astring):
    alph_set = set(letter for letter in 'abcdefghijklmnopqrstuvwxyz')
    return len(alph_set.difference(set(astring.lower())) < 1