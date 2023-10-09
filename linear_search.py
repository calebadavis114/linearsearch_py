def linear_search(value_to_find, array_to_search_through):
   num = 0
   for item in array_to_search_through:
       if(value_to_find == item):
        return num
       num += 1
    
print(linear_search(1, [2,3,4,5,6,0,7,8]))

def linear_search_global(value_to_find, array_to_search_through):
    arr = []
    num = 0
    for item in array_to_search_through:
       if(value_to_find == item):
        arr.append(num)
       num += 1
    return arr
    
