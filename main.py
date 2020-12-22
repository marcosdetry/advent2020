import re
import string
f = open("numeros.txt", "r")

# Day 1
# numeros = f.readlines()
#
# numeros = [int(x) for x in numeros]
#
# for x in numeros:
#     for z in numeros:
#         for y in numeros:
#             if x + z + y == 2020:
#                 print(x * z * y)


# numeros = f.readlines()

# numeros = [x.strip() for x in numeros]
# total = 0
# for line in numeros:
#     line = line.split()
#     password = line[2]
#     rango = line[0].split('-')
#     rango = [int(x) for x in rango]
#     letter = line[1][0]
#
#     # if password.count(letter) in range(rango[0], rango[1] + 1):
#     #     total += 1
#     # else:
#     #     pass
#
#     if (password[rango[0]-1] == letter
#     and password[rango[1]-1] != letter) or (password[rango[1]-1] == letter and password[rango[0]-1] != letter):
#         total += 1
#
# print(total)


# x = "HellHellHellHell"
# x = list(x)
# print(x)
# y = 0
#
# for i in range(0,4):
#     y += 3
#     print(x[y])

# tobbogan = f.readlines()
#
# tobbogan = [x.strip() for x in tobbogan]
# movement = 0
# total = 0
#
# for x in tobbogan:
#     try:
#         if x[movement] == "#":
#             movement += 3
#             total += 1
#         else:
#             movement += 3
#     except IndexError:
#         movement = movement - len(x)
#         if x[movement] == "#":
#             movement += 3
#             total += 1
#         else:
#             movement += 3
# print(total)
#
# slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
# print (type(slopes))
#
# arboles = 1
#
# for right,down in slopes:
#     position = 0
#     final = 0
#
#     for number_line, x in enumerate(tobbogan):
#             if number_line % down == 0:
#                 if position > len(x) - 1:
#                     position = position - len(x)
#                 if x[position] == '#':
#                     final += 1
#                 position += right
#     print (final)
#     arboles = arboles * final
# print (arboles)

#passports = f.readline()

#          4
#
# passport_must_have = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
# passport_optional = ['cid']
# valid_eye_color = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
#
# passports = []
#
# passport_has = []
# for line in f:
#      if line != '\n':
#         # print (line)
#         for x in (line.strip().split(' ')):
#             code = x.split(':')[0]
#             data = x.split(':')[1]
#             if code == 'byr':
#                 if len(data) == 4 and int(data) >= 1920 and int(data) <= 2002:
#                     passport_has.append(code)
#             if code == 'iyr':
#                 if len(data) == 4 and int(data) >= 2010 and int(data) <= 2020:
#                     passport_has.append(code)
#             if code == 'eyr':
#                 if len(data) == 4 and int(data) >= 2020 and int(data) <= 2030:
#                     passport_has.append(code)
#             if code == 'hgt':
#                 unidad = data[-2:]
#                 try:
#                     valor = int(data[:-2])
#                 except ValueError:
#                     valor = 0
#                 if (unidad == 'cm' and valor >=150 and valor <= 193) or (unidad == 'in' and valor >=59 and valor <= 76):
#                     passport_has.append(code)
#
#             if code == 'hcl':
#                 hexacolor = data[1:]
#                 simbolohexa = data[0]
#                 if (simbolohexa == '#') and re.search('^([0-9]|[a-f]){6}$', hexacolor) != None:
#                     passport_has.append(code)
#             if code == 'ecl':
#                 if data in valid_eye_color:
#                     passport_has.append(code)
#             if code == 'pid':
#                 if re.search('^[0-9]{9}$',data) != None:
#                     passport_has.append(code)
#                 else:
#                     print(code, data)
#             if code == 'cid':
#                     passport_has.append(code)
#      else:
#         passports.append(passport_has)
#         passport_has = []
#
# passports.append(passport_has)
# print (passports)
#
# total_valid_passports = 0
#
# for passport in passports:
#     passport_must_have_items = passport_must_have.copy()
#     for item in passport:
#         try:
#             passport_must_have_items.remove(item)
#         except:
#             print(f'Este item {item} no estaba en {passport_must_have_items}')
#     if len (passport_must_have_items) == 0: total_valid_passports += 1
#
# print(f"El total de pasaportes validos es: {total_valid_passports}")
#

# 5

# FBFBBFFRLR
# 0101100
# RLR
# 101
#
# occupied_plane_seats =[]
# total_plane_seats =[]
#
# for seat in f:
#     row = int(('0b'+ seat[0:7]).replace('F', '0').replace('B','1'),2)
#     seat = int(('0b'+ seat[7:10]).replace('R', '1').replace('L','0'),2)
#     row_seat = [row,seat]
#     occupied_plane_seats.append(row_seat)
#
# last_seat = max(occupied_plane_seats,key = lambda k: k[0])
# first_seat = min(occupied_plane_seats,key = lambda k: k[0])
#
#
# #key2 = max(square, key = lambda k: square[k])
#
# print(occupied_plane_seats)
# print(last_seat[0],first_seat[0])
#
# total_plane_seats = [[x,y] for x in range(10,115) for y in range(0,8)]
#
#
#
# print (total_plane_seats)
#
# my_seat = total_plane_seats.copy()
#
# for seat in occupied_plane_seats:
#     my_seat.remove(seat)
#
# print (last_seat[0]*8+7)
# print(my_seat)
# print(my_seat[0][0]*8+my_seat[0][1])


#6

# total = 0
# group = set(string.ascii_lowercase)
# print (group)
#
#
# for line in f:
#     if line != '\n':
#         person_set = set(line.strip())
#         group = group & person_set
#     else:
#         total += len(group)
#         group = set(string.ascii_lowercase)
#
# total += len(group)
#
# print(total)

