


# def fibonacci(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 1
#     elif n> 2:
#             return fibonacci(n-1) + fibonacci(n-2)

# for n in range(1, 501):
#     print(n , ":", fibonacci(n))
    
# square = []

# for i in range(1, 101):
#     square.append(i**2)
# print(square)

# square_2 = [i**2 for i in range(1,101)]
# print(square_2)

# remainder = [x**2 % 5 for x in range(1,102)]
# print(remainder)

# remainder_2 = [x**2 % 11 for x in range(1,101)]
# print(remainder_2)

# movies = ["a","b","c","d","e","f","g","h","i","j","k","k","l","m"]

# a_movies = []
# for title in movies:
#     if title.startswith("g"):
#         a_movies.append(title)
# print(a_movies)

# b_movies = [title for title in movies if title.startswith("g")]
# print(b_movies)

# v = [2,3,4,5,6,7,8]
# w = [4*x for x in v]
# print(w)

# a = [1,3,5,7]
# b = [2,4,6,8]
# cartesian_product = [(i,j) for i in a for j in b ]
# print(cartesian_product)

# class User:
#     pass
# user1 = User()
# user1.first_name = "Rahul"

# user1.last_name = "Sen"

# print(user1.first_name)
# print(user1.last_name)

# user2 = User()
# user2.first_name = "Frank"
# user2.last_name = "Poole"
# print(user2.first_name, user2.last_name)

# class User:

#     def __init__(self,full_name, birthday):

#         self.name = full_name
#         self.birthday = birthday

#         name_pieces = full_name.split(" ")
#         self.first_name = name_pieces[0]
#         self.last_name = name_pieces[-1]

# user = User("Rahul Sen","05..01..1999")
# print(user.name)
# print(user.first_name)
# print(user.birthday)

# a = lambda x: 3*x +1
# b = a(2)
# print(b)
# full_name = lambda fn,ln: fn.split().title() + " " + ln.split().title()
# c = list(full_name("  leonhard", "EULER"))
# print(c)

# def build_quadratis_function(a,b,c):
#     return lambda x: a*x**2 + b*x + c
# f = build_quadratis_function(2,3,-5)
# f(0)
# f(1)
# f(2)

# import math

# def area(r):
#     return math.pi * (r**2)

# radii = [2,5,7.1,0.3,10]

# areas = []
# for r in radii:
#     a = area(r)
#     areas.append(a)

# print(areas)


# ###### Map

# a = list(map(area,radii))
# print(a)

# temp = [("Berlin", 29),("Cairo",36),("Buenos Aires", 19),("Los Angeles", 26), ("Tokyo", 27),("New York",28),("London",22),("Beijing",32)]

# c_to_f = lambda data : (data[0], (9/5)*data[1] + 32)

# a = list(map(c_to_f, temp))
# print(a)

# import statistics
# data = [1.3,2.7,0.8,4.1,4.3,-0.1]
# avg = statistics.mean(data)
# print(avg)

# b = list(filter(lambda x: x> avg, data))
# print(b)

# c = list(filter(lambda  y: y< avg, data))
# print(c)

# countries = ["","Argentina","","Brazil","chile","","Colombia","","Ecuaor","","","Venezuela"]

# a = list(filter(None,countries))
# print(a)

# from functools import reduce

# data = [2,3,5,7,11,13,17,19,23,29]
# multiplier = lambda x,y: x*y
# a = reduce(multiplier,data)
# print(a)

# earth_metals = ["Beryllium","Magnesium","Calcium","Strontium","Barium","Radium"]
# earth_metals.sort()
# print(earth_metals)

# earth_metals.sort(reverse = True)
# print(earth_metals)

#earth_metals = ("Beryllium","Magnesium","Calcium","Strontium","Barium","Radium")
# #__Not Possible_______-> earth_metals.sort()

# planets = [
#     ("Mercury", 2440, 5.43, 0.395),
#     ("Venus", 6052,5.24,0.723),
#     ("Earth", 6378,5.52,1.000),
#     ("Mars", 3396,3.93,1.530),
#     ("jupiter",71492,1.33,5.210),
#     ("Saturn",25559,1.27,19.213),
#     ("Neptune", 24764,1.64,30.070)
# ]

# size = lambda planet: planet[1]
# a = planets.sort(key = size, reverse = True)
# print(planets)
# density = lambda planet: planet[2]
# planets.sort(key = density)
# print(planets)

# sorted_earth_metals = sorted(earth_metals)
# print(sorted_earth_metals)

# data = (7,2,5,6,1,3,9,10,4,8)
# sorted(data)
# print(data)

# from math import pi

# def circle_area(r):
#     return pi*(r**2)

# radii = [2, 0 , -3 , 2+5j , True, "radius"]
# message = "Area of circle with r = {radious} is {area}."

# for i in radii:
#     A = circle_area(i)
#     print(message.format(radious = i, area = A))

# import unittest 
# from circles import circle_area
# from math import pi

# class TestcircleArea(unittest.TestCase):
#     def test_area(self):
#         self.assertAlmostEqual(circle_area(1),pi)
#         self.assertAlmostEqual(circle_area(0),0)
#         self.assertAlmostEqual(circle_area(2.1), pi * 2.1**2)

#     def test_values(self):
#         self.assertRaises(ValueError, circle_area, -2)

# from math import pi
# def circle_area(r):
#     if r < o:
#         raise ValueError("The radius cannot be negatve. ")
#     return pi*(r**2)

# for i in range(5):
#     print("Hello World")

# import logging 
# import time 
# logging.basicConfig(filename = "c:\\python",level = logging.DEBUG)

# logger = logging.getLogger()
# def read_file_timed(path):
#     start_time = time.time()
#     try:
#         f = open(path, mode = "rd")
#         data = f.read()
#         return data 
#     except FileNotFoundError as err:
#         logger.error(err)
#         raise
#     else:
#         f.close()
#     finally:
#         stop_time = time.time()
#         dt = stop_time - start_time
#         logger.info("time required for {file} = {time}". format(file = path, time = dt))

# data = read_file_timed("E:\\python_Lessons\\audio_file.wav")

import urllib3
import urllib

#dir(urllib)

from urllib import request 
#der (request)

resp = request.urlopen("https:/www.wikipedia.org")

dir(resp)













