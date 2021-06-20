Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Q2
print(5**9)
print(3//2)
print(7//3)
print(7/3)
print(6==6)
a = 20; a+= 30; a%=3;
print(a)
print(True * False)
print(True & False)
print(True and False)
print(((6>3) and (7<4) or (18==3)) and (9>3))
print( True is False)
print("False" in "False")
print(((True == False) or (False > True)) and (False <= True))



#Q3
s1="Nice to have it"
s2="here"
s3=s1+" "+s2
print(s3)


#Q4
a=[1,2,[3,4],[5,[100,200,['Hello']],23,11],1,7]
print(a[3][1][2][0])


#Q5
s1="Nice to have it"
s2="here"
a =[1,2,[3,4],[5,[100,200,['Hello']],23,11],1,7]
a.insert(0,s1)
a.append(s2)
print(a)


#Q6
color_list_1 = set(["White","Black","Red"])
color_list_2 = set(["Red","Green"])
print(color_list_1-color_list_2)


#Q7
import string

def ispangram(str):
    #alphabet = "abcdefghijklmnopqrstuvwxyz"
    #for char in alphabet:
        #if char not in str.lower():
            #return False

        #return True
string = 'the quick brown fox jumps over the lazy dog'
if (ispangram(string) == True):
    #print("yes")
else:
    #print("No")


#Q8
a = int(input("enter an integer:"))
n1 = int("%s" %a)
n2 = int("%s%s" % (a,a))
n3 = int("%s%s%s" %(a,a,a))
value=n1+n2+n3
print(value)


#Q9
items = input("enter sequence of words : ")
words = [word for word in items.split(",")]
print(",".join(sorted(list(set(words)))))


#Q10
d = {'student': ["Rahul","Kishore","Vidhya","Raakhi"], "Marks": [57,87,67,79]}
print(d['student'][1])