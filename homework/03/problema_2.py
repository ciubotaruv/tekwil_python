#Suppose you have a list of str (ex. l = [‘test1’, ‘Ion’, “Python”, ‘pisca’]).
#Make a script that can count the number of vowels from all the strings out of this list and print it. 

I = ['abca','Ion',"Python",'pisca']
number_of_vowels = 0;

#version one
def isVowel( str ):
    vowel = str.upper()
    if (vowel  == 'A' or vowel  == 'E' or vowel  == 'I' or vowel  == 'O' or vowel  == 'U' ):
        return 1
    else:
        return 0

print (isVowel('a'))


for i in I:
    for x in i:
        if (isVowel(x)):
            number_of_vowels += 1

print('V1.Number of vowel in this array its:',number_of_vowels)

#version two

for i in I:
    for x in i:
        vowel = i.upper()
        if (i  == 'A' or vowel  == 'E' or vowel  == 'I' or vowel  == 'O' or vowel  == 'U' ):
            number_of_vowels += 1

print("V2.Number of vowel in",I,'its:',number_of_vowels)

nr = 'one, two, three, four, five'
len(nr)
