a = "apple"
even_list = [i for i in range(11) if i % 2 == 0]
print(even_list)
even_list2= [i for i in a if i == "p"]
def minimum(numbers):
    res = float ('inf')
    for i in numbers:
        res = i if i < res else res
    return res

minimum ([1,2-3,0])
print(minimum)
#gregmalcolm.py