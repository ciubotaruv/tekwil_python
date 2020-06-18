#Suppose you have a list of 10 tuples where each tuple is a pair of 2 elements – first is an integer number, the second one is
#the string representation of its roman literal representation ( ex. L = [ (1, “I”), (2, “II”), (3, “III”), (4, “IV”) … (10, “X”) ] ). Make a
#script that would print out each Arabic number its with its Roman equivalent. Use string formating for print syntax. For example
#you should see at the prompt for integer 1: “Arabic number 1 is represented in Roman character I”

l = [ (1, 'I'), (2, 'II'), (3, 'III'), (4, 'IV'), (5, 'V'), (6, 'VI'), (7, 'VII'), (8, 'VII'), (9, 'IX'), (10, 'X') ] 


number = int(input('Enter interge number: '))

if number <= 10:
    for (t1,t2) in l:
        if number == t1:
            print('Arabic number',number,'is represented in Roman character:',t2)
else:
    print('cant represent this number in arabic nr')


    
