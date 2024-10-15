#def avg(data):
    #assert not(len(data) == 0), 'No data'
    #return sum(data) / len(data)
#foo = []
#print(avg(foo))
def even(n):
    if n <= 3:
        n = False
    else:
        n = True
    return n

a = 3
b = 4
c = -1

assert even(a) == False, 'Your code fails!'
assert even(b) == True, 'Your code fails!' 
assert even(c) == False, 'Your code fails!'
print('Success!')

