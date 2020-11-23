# 7. sequental generator
import types

def generator_wrapper(function=None, *args, **kwargs):
    assert function is not None, "Please supply a function"
    def inner_func(function=function, **kwargs):
        generator = function(**kwargs)
        assert isinstance(generator, types.GeneratorType), "Invalid function"
        try:
            yield next(generator)
        except StopIteration:
            generator = function(**kwargs)
            yield next(generator)
    return inner_func

@generator_wrapper
def func_gen(*args):
	for elm in lst:
		yield elm
			
			 

str1, str2 = '123','abc'
lst1,lst2 = [1,2,3], ['a','b','c']
tup1,tup2 = (1,2,3), ('a','b','c')
dic1,dic2 = {1: 1, 2: 2, 3: 3}, {'a':'a', 'b':'b', 'c':'c'}

print("-"*5, 'string', "-"*5)
[print(elm) for elm in str1]
[print(elm) for elm in func_gen(str2)]
str_gen = func_gen(str1)
print('1st element: ', next(str_gen))
print('2st element: ', next(str_gen))
print('3st element: ', next(str_gen))
print('1st element: ', next(str_gen))
# print("-"*5, 'list', "-"*5)
# [print(elm) for elm in lst1]
# [print(elm) for elm in func_gen(lst2)]
# print("-"*5, 'tuple', "-"*5)
# [print(elm) for elm in tup1]
# [print(elm) for elm in func_gen(tup2)]
# print("-"*5, 'dict', "-"*5)
# {print({k: v}) for (k, v) in dic1.items()}
# {print({k: v}) for (k, v) in func_gen(dic2.items())}




