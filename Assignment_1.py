## Q2...........
5**9
3//2
7//3
7/3
6 == 6
a = 20; a+= 30; a%=3; print(a)
True * False
True & False
True and False
((6>3) and (7<4) or (18==3)) and (9>3)
True is False
False in ‘False’
((True == False) or (False > True)) and (False <= True)


## Q3.........
s1 = " Nice to have it"
s2 = " here"
s3 = s1 + s2
print(s3)

## Q4.........
a = [1, 2,[3 , 4],[5,[100,200,['hello']],23,11],1,7]
[1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7]
a[3][-3][-1][-1]


## Q5..........
a = [1, 2,[3 , 4],[5,[100,200,['hello']],23,11],1,7]
a.insert(0,s3) ; a.append(s3)
print(a)

## Q6..........
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
print (set(color_list_1 - color_list_2))

## Q8..........
eval('{0}+{0}{0}+{0}{0}{0}'.format(input('Enter the number : ')))

## Q9..........
a = ['without','hello','bag','world']
a.sort()
print(a)


# Q10.........
d = {'Student': ['Rahul', 'Kishore', 'Vidhya', 'Raakhi'],'Marks': [57,87,67,79]}
print(d['Student'][d['Marks'].index(max(d['Marks']))])
