one = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
tenp = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
tenp2 = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']


def once(num):
    global one
    word = ''
    word = one[int(num)]
    word = word.strip()
    return word


def ten(num):
    global tenp
    global tenp2
    word = ''
    if num[0] == '1':
        word = tenp[int(num[1])]
    else:
        text = once(num[1])
        word = tenp2[int(num[0])]
        word = word + " " + text
    word = word.strip()
    return word


def hundred(num):
    global one
    word = ''
    text = ten(num[1:])
    word = one[int(num[0])]
    if num[0] != '0':
        word = word + " Hundred "
    word = word + text
    word = word.strip()
    return word


def thousand(num):
    word = ''
    pref = ''
    text = ''
    length = len(num)
    if length == 6:
        text = hundred(num[3:])
        pref = hundred(num[:3])
    if length == 5:
        text = hundred(num[2:])
        pref = ten(num[:2])
    if length == 4:
        text = hundred(num[1:])
        word = one[int(num[0])]
    if num[0] != '0' or num[1] != '0' or num[2] != '0':
        word = word + " Thousand "
    word = word + text
    if length == 6 or length == 5:
        word = pref + word
    word = word.strip()
    return word

test = int(input())
a = str(test)
leng = len(a)
if leng == 1:
    if a == '0':
        num = 'Zero'
    else:
        num = once(a)
if leng == 2:
    num = ten(a)
if leng == 3:
    num = hundred(a)
if leng > 3 and leng < 7:
    num = thousand(a)
if leng > 6 and leng < 10:
    num = million(a)
if leng > 9 and leng < 13:
    num = billion(a)
words = num.split();
words_count = 0
print(num)
for i in words:
    for j in i:
        words_count+=1
        print(j,': ',words_count)

print('numbers of letter:',words_count)
