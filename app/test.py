# dicts = {}
# IDs = ['m1','m2','m3','m4']
# keys = range(4)
# values = ['Date','Time','Name','Message']
# for i in keys:
#     dicts[i] = values[i]
# D = dict.fromkeys(IDs, dicts)
# print(dicts)
# print(D)
import sys, io
from emoji import emojize
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
f = io.open("C:/Users/mayank/Desktop/WhatsApp Chat with Test.txt", "r", encoding="utf-8")
file_content = f.readlines()

print(len(file_content))
for i in range(len(file_content)):
    print(file_content[i].translate(non_bmp_map).split(', ',1))

# print(file_content[0].translate(non_bmp_map))
# for line in f:
#     data = line.translate(non_bmp_map).split(', ',1)
#     for i in data:
#         print(i)
#         x = i.split(' - ')
#         for j in x:
#             print(j)
#             m = j.split(': ')
#             for n in m:
#                 print(n)
