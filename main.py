# 9.14, 9.16

s = 'яблоко'
x = len(s)
print(x)
print(s[5])


#9.15
#sl = input('Введите слова\n')


#9.16

if s[2] == s[4]:
    print('одинаковые')
else:
    print('разные')

#9.24

a = s[1:5]
x = s[3:]
print(a)
print(x)

#9.38(a)

q = input('Введите слово\n')
z = len(q)
result = q[7:12] + q[4:7] + q[0:4]

if z == 12:
    print(result)
else:
    print('error')


#41

y = 'arsenal'
for i in range(0, len(y)-1):
    print(y[i])

#9.59

coll = 0
n = 'Сколько лет, сколько зим'
for i in n:
    if i == 'о':
        coll += 1
print(coll)

# 9.76

asd = input('Дано предложение, в котором имеется несколько букв')

cnt = 0

