lst_a = ['IT', 5001]
lst_b = ['E', ('is', 'easy')]
lst_c = lst_a + lst_b
print('1.', lst_a)
print('2.', lst_b)
print('3.', lst_c)
tup_a = ('IT', 5001)
#tup_a[1] = 5003
lst_a[1] = 5003
print('4.', lst_a)
lst_a.append('E')
print('5.', lst_a)
lst_a.extend('easy')
print('6.', lst_a)
cpy_b = lst_b[:]
print('7.', cpy_b)
cpy_b[1] = 'is hard'
print('8.', cpy_b)
print('9.', lst_b)
lst_d = [1, [2], 3]
cpy_d = lst_d[:]
print('10.', cpy_d)
print('11.', lst_d)
lst_d[1][0] = 9
print('12.', cpy_d)
print('13.', lst_d)
print('14.', lst_d == cpy_d)
print('15.', lst_d is cpy_d)
print('16.', lst_d[1] == cpy_d[1])
print('17.', lst_d[1] is cpy_d[1])