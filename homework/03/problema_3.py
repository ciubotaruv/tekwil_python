#Suppose that you have a dict (ex. D = dict(key1=1, key2=2, key3=3, key4=4)). Each key is mapped to an integer value.
#Make a script that would iterate through all the values of the dictionary and would print only the even numbers.

d = dict(key1=1, key2=2, key3=3, key4=4)

for k,v in d.items():
    if v%2 == 0:
        print(v, 'its even number') 

