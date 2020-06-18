#Suppose you have a string representing a sentence (ex. “We all are eager to learn Python and become good developers!”).
#Please make a script that would read this script and print only the words that have at least 3 consonants in it.
#Also this scrit when run must print the number of words of this kind he has found.

#function detertminate is consonants or no.

def isConsonants(str):

    con = str.lower()
    lists_of_consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'y', 'z']
    
    if (con in lists_of_consonants):
        return 1

sentence = 'We all are eager to learn Python and become good developers!'
a = sentence.split()

print('Our sentence:', sentence)

for i in a:
    nr = 0
    for x in i:
        if(isConsonants(x)):
            nr += 1
    if nr >= 3: print('In word', i, 'have at least 3 consonants exactly:', nr )


    
    




