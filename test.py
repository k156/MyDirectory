seconds_per_hour = 60 * 60
seconds_per_day = seconds_per_hour * 24
# print( seconds_per_day/seconds_per_hour )
# print( seconds_per_day//seconds_per_hour )

year_list = []

things_list = ['mozzarella', 'cinderella', 'salmonella']
# print( things_list[1].title() )
# print(things_list[0].upper() )
# things_list.remove('salmonella')
# del things_list[2]
# things_list.pop(2)
# print(things_list)

# surprise = ['Groucho', 'Chico', 'Harpo']
# print(surprise[2].lower()[::-1].title())
e2f = {'dog':'chien', 'walrus': 'morse'}
# print(e2f)
# print(e2f['walrus'])
f2e = {}
for i, j in e2f.items():
    f2e[j] = i
# print(f2e['chien'])
# print(e2f.keys())

otherdict = {'cats': 'Henri', 'octopi': 'Grumpy', 'emus': 'Lucy'}
dict2 = {}
dict3 = {}
life = {'animals' : otherdict, 'plants': dict2 , 'others': dict3}
# print(life.keys())
# print(life['animals'])
# print(life['animals']['cats'])


####################
# def knights(saying):
#     def inner(quote):
#         return "We are the knights who say: '%s'" % saying
#     return inner

# knights('Ni!')
########################

# guess_me = 7
# if guess_me < 7:
#     print("too low")
# elif guess_me > 7:
#     print("too high")
# else:
#     print("just right")

# start = 1

# while True:
#     if start < guess_me:
#         print(start)
#         print("too low")
#     elif start == guess_me:
#         print(start)
#         print("found it!")
#     elif start > guess_me:
#         print(start)
#         print("oops")
#         break
#     start += 1



# for i in [3, 2, 1, 0]:
#     print(i)


# for x in range(2, 11, 2):
#     print(x)


# numbers = [number for number in range(10) if number%2==0]
# # print(numbers)
# square = {i:i*i for i in range(10)}
# # print(square)
# a_set = {number for number in range(10) if number%2 ==1}
# # print(a_set)
# got_it = ( "Got"+ str(x) for x in range(10) )
# for got in got_it:
#     print(got)
# def good():
#     lst = ['Harry', 'Ron', 'Hermione']
#     return lst
# good()
# def get_odds():
#     lst = list (x for x in range(10) if x%2==1)
#     return lst[2]
# get_odds()
# def test(func):
#     def new_function(*args):
#         print("start")
#         result = func(*args)
#         print("end")
#         return result
#     return new_function
# @test
# def add(a, b):
#     c = a + b
#     print(c)
#     return c
# add(3,4)
# @test
# def multiply(a):
#     c = a * a
#     print(c)
#     return c
# multiply(7)
# @test
# def subtract(a, b):
#     c = a - b
#     print(c)
#     return c
# subtract(7, 4)
# class OopsException(Exception):
#     print ("Caught an oops")
# words = ['hello', 'jello', 'mello', 'bello', 'hello']
# if set(words) != words:
#     raise OopsException(words)
# titles = ['Creature of Habit', 'Crewel Fate']
# plots = ['A nun turns into a mon ster', 'A hunted yarn shop']
# a = list(zip(titles, plots))
# print(a)


# from collections import defaultdict, OrderedDict
# # food_counter =  defaultdict(int)
# # for food in ['spam', 'spam', 'eggs', 'spam']:
# #     food_counter[food] += 1

# # for food, count in food_counter.items():
# #     print(food, count)

# plain = {'a': 1 , 'b': 2, 'c': 3}
# print(plain)
# fancy = OrderedDict(plain)
# print(fancy)
# dict_of_lists = defaultdict(list)
# dict_of_lists['a'] = 'something for a'
# print(dict_of_lists['a'])

el_dict = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1 }
