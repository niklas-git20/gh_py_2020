# 4. List comprehension 
# generate list in range 0..100, where each element is divisible by 5 and not by 3

lst_1 = [elm for elm in range(0,100) if elm % 5 == 0 and elm % 3 != 0]
print(lst_1)