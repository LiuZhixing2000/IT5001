# question 1
# 1. {('A', 2), ('B', 3), (1, 4))}
# 2. False
# 3. {('A', 2), ('B', 3)}
# 4. {('A', 2), ('B', 3)}
# 5. error
# 6. {1, 'A', (1, 2), 4}
# 7. True
# 8. error //////////////////////False
# 9. {1, 'A', 4}
# 10. {1, 'A', 4}
# 11. {1, 'A', 4, 2}
# 12. {'A', 'B'}
# 13. {1, 'A', 4, 2, 'B'}
# 14. {'A'}
# 15. {1, 4, 2}
# 16. {1, 4, 2, 'B'}
#set_c = {'A', 'B', 1, 4, 2}
#set_b = {1, 'A', 4, 2}
# 17. {1, 'A', 4, 2}
# 18. {} ////////////////set()
# 19. {'B'}
#set_c = {'A', 'B', 1, 4, 2, {1, 'A', 4, 2}}
# 20. {'A', 'B', 1, 4, 2, {1, 'A', 4, 2}} ///////////////error
# 21. {1, 'A', 4, 2, 10, 20}
# 22. {1, 'A', 4, 2, 10, 20} /////////////////error


# a = ('A', 2), ('B', 3), (1, 4)
# set_a = set(a)
# print('1.', set_a)
# print('2.', 2 in set_a)
# set_a.discard((1, 4))
# print('3.', set_a)
# set_a.discard((1, 4))
# print('4.', set_a)
# #set_a.remove((1, 4))
# print('5.', set_a)
# b = [[1, 'A'], [(1, 2), 4]]
# set_b = set([y for x in b for y in x])
# print('6.', set_b)
# print('7.', (1, 2) in set_b)
# print('8.', set_a < set_b)
# set_b.remove((1, 2))
# print('9.', set_b)
# set_b.add(1)
# print('10.', set_b)
# set_b.add(2)
# print('11.', set_b)
# set_c = set((i[0] for i in set_a))
# print('12.', set_c)
# set_d = set_b | set_c
# print('13.', set_d)
# print('14.', set_b & set_c)
# print('15.', set_b - set_c)
# print('16.', set_b ^ set_c)
# set_c |= set_b
# print('17.', set_b & set_c)
# print('18.', set_b - set_c)
# print('19.', set_b ^ set_c)
# #set_c.add(set_b)
# print('20.', set_c)
# # union()的参数可以是list，但是|不可以
# print('21.', set_b.union([10, 20]))
# #print('22.', set_b | [10, 20])

# question 2
# 1. {'A': 2, 'B': 3, 1: 4}
# 2. error
# 3. None
# 4. {1: 'A', (2, 3): 4}
# 5. 4
# 6. 1
# 6. (2, 3)
# 7. 'A'\\\\\\\\\\\\\\\\\\
# 7. 4
# 8. 1 'A'
# 8. (2, 3) 4
# 9. {1: 'A'}
# 10. {1: 'A'}
# ('A', 'B', 1)
# 11. [2, 3, 4]
# 12. {1: {2: 3}, 4: 5}
# 13. {1: {2: 9}, 4: 9}\\\\\\\\\\\\\\\\\\\\\\
# 14. {1: {2: 9}, 4: 7, 2: 10, 3: 20}
# 15. None
# 16. (3, 20)
# 17. {}
# 18. {}
# 19. error
# 20. error

# a = (('A', 2), ('B', 3), (1, 4))
# dict_a = dict(a)
# print('1.', dict_a)
# #print('2.', dict_a[2])
# print('3.', dict_a.get(2))
# b = [[1, 'A'], [(2, 3), 4]]
# dict_b = dict(b)
# print('4.', dict_b)
# print('5.', dict_b[(2,3)])
# for key in dict_b.keys():
#     print('6.', key)
# for val in dict_b.values():
#     print('7.', val)
# for key,val in dict_b.items():
#     print('8.',key, val)
# del dict_b[(2, 3)]
# print('9.', dict_b)
# #del dict_b[2]
# print('10.', dict_b)
# print(tuple(dict_a.keys()))
# print('11.', list(dict_a.values()))
# dict_c = {1: {2: 3}, 4: 5}
# print('12.', dict_c)
# dict_d = dict_c.copy()
# dict_d[4] = 9
# dict_d[1][2] = 9
# print('13.', dict_c)
# dict_d.update({2: 10, 3: 20, 4: 7})
# print('14.', dict_d)
# #print('15', dict_d.pop(100))
# print('16', dict_d.popitem())
# dict_c.clear()
# print('17.', dict_c)
# print('18.', dict_d)
# del dict_c
# #print('19.', dict_c)
# print('20.', dict_d[1][2])