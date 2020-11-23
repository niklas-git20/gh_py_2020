# 13. Write a script to get the maximum and minimum value in a dictionary

# sample input data
dic1 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60, 7: 20, 8: 40, 9: 60}

min_key = min(dic1, key=dic1.get)
min_val = dic1[min_key]
max_key = max(dic1, key=dic1.get)
max_val = dic1[max_key]

print("minimal: ", min_key, min_val)
print("maximal: ", max_key, max_val)