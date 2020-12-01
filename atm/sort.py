from itertools import combinations

def subset_sum(numbers, target, partial=[], partial_sum=0):
    if partial_sum == target:
        yield partial
    if partial_sum >= target:
        return
    for i, n in enumerate(numbers):
        remaining = numbers[i + 1:]
        yield from subset_sum(remaining, target, partial + [n], partial_sum + n)
#list(subset_sum([1, 2, 3, 7, 7, 9, 10], 10)) yields [[1, 2, 7], [1, 2, 7], [1, 9], [3, 7], [3, 7], [10]].

# big processing time 
def find_sum_in_list(numbers, target):
    results = []
    for x in range(len(numbers)):
        # results.extend(
        #     [combo for combo in combinations(numbers ,x) if sum(combo) == target]   
        # ) 
        for combo in combinations(numbers ,x):
        	if sum(combo) == target:
        		results.extend(combo)
    return results



targ = 12
# get banknote stack
comb = {1: 2, 2: 2, 5: 2, 10: 2, 20: 1}
list_s = []
for key,val in comb.items():
	print(key,val)
	for i in range(0, val):
		if key * val != 0:
			list_s.append(key)
# list_m.append(list_s)
# list_s = []
for rec in list_s:
	print('rec', rec)

# print(list(subset_sum(list_s, targ)))

print(find_sum_in_list(list_s, targ))
