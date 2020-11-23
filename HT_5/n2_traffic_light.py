# 2. traffic light control
import time

def sequencer(light_set):
	cycle = 1
	while cycle < 10: # avoid uncontinious cycling
		for mode in range(1, len(light_set)+1):
			yield light_set[mode] [0]
			time.sleep(light_set[mode] [1])
			cycle += 1

# car and walker traffic light parameters sets 
car_light = {1:['red',4], 2:['red-yellow',1], 3:['green',4], 4:['green-blink',1], 5:['yellow',2]}
walk_light = {1:['red',2], 2:['green',2]}
cw_light = {'red':'green', 'red-yellow':'red', 'green':'red', 'green-blink':'red', 'yellow':'red'}

# car trafic light itself
# print("-"*5, 'car traffic light', "-"*5)
# for c_light in sequencer(car_light):
# 	print(c_light)

# # walker trafic light itself
# print("-"*5, 'walker traffic light', "-"*5)
# for w_light in sequencer(walk_light):
# 	print(w_light)

# combined mode (car traffic light is master)
print("-"*5, 'combined car and walker traffic lights', "-"*5)
for c_light in sequencer(car_light):
	w_light = cw_light[c_light]
	# tabulation calculation, 1 tab = 8 spaces
	t_num = len(c_light) // 8
	print(c_light,'\t'*(3-t_num), w_light)
