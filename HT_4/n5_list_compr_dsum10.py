# 5. List comprehension 
# generate list in range 0..100, where each element have in digit`s sum 10

lst_1 = [elm for elm in range(0,100) if sum(map(int, str(elm))) == 10]
print(lst_1)
