def dd (_list, number):
    c = len(_list)
    for i in _list:
        if number == i:
            return True
        
    return False
print(dd([1, 2, 33, 45], 2))
print(dd([1, 2, 33, 45], 33))
