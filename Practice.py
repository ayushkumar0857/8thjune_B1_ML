Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> ##Q2...
>>> 5**9
1953125
>>> 3//2
1
>>> 7//3
2
>>> 7/3
2.3333333333333335
>>> 6==6
True
>>> a = 20 ; a+=30 ; a%=3 ; print(a)
2
>>> True*False
0
>>> True&False
False
>>> True and False
False
>>> ((6>3) and (7<4) or (18==3)) and (9>3)
False
>>> True is False
False
>>> False is 'false'
False
>>> ((True == False) or (False > True )) and (False <=True)
False
>>> 
>>> ## Q3.........
>>> s1 = " Nice to have it"
>>> s2 = " here"
>>> s3 = s1 + s2
>>> print(s3)
 Nice to have it here
>>> 
>>> ## Q4.........
>>> a = [1, 2,[3 , 4],[5,[100,200,['hello']],23,11],1,7]
>>> [1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7]
[1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7]
>>> a[3][-3][-1][-1]
'hello'
>>> 
>>> ## Q5..........
>>> a = [1, 2,[3 , 4],[5,[100,200,['hello']],23,11],1,7]
>>> a.insert(0,s3) ; a.append(s3)
>>> print(a)
[' Nice to have it here', 1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7, ' Nice to have it here']
>>> 
>>> ## Q6..........
>>> color_list_1 = set(["White", "Black", "Red"])
>>> color_list_2 = set(["Red", "Green"])
>>> print (set(color_list_1 - color_list_2))
{'White', 'Black'}
>>> 
>>> ## Q8..........
>>> eval('{0}+{0}{0}+{0}{0}{0}'.format(input('Enter the number : ')))
Enter the number : 5
615
>>> 
>>> ## Q9..........
>>> a = ['without','hello','bag','world']
>>> a.sort()
>>> print(a)
['bag', 'hello', 'without', 'world']
>>> 
>>> # Q10.........
>>> d = {'Student': ['Rahul', 'Kishore', 'Vidhya', 'Raakhi'],'Marks': [57,87,67,79]}
>>> 
KeyboardInterrupt
>>> print(d['Student'][d['Marks'].index(max(d['Marks']))])

Kishore
>>> 
>>> 