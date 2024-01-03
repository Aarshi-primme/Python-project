



#only enter valid 4 numbwers pin
'''try:
    a = input('enter your 4 digit pin :')
    print(int(a))
    if len(a)==4:
        print('your pin is conformed\n')
    else:
        print('re-enter\n')
except(ValueError,TypeError):
    print('please enter valid input\n')

finally:
    print('after enter your pin u will excute')'''


'''d1 = {122: 45,456: 456,34: 456,456: 56}
d2 = {123: 57,78: 897}

#update()
d1.update(d2)
print(d1)

#empty dict
empt = {}
print(type(empt))

#pop()
#del : for delete the entirely dict if we are not give a key
del d1[123]
print(d1)'''

#continue,pass,break
'''for i in range(7):
    print(i)
    i = i+1
    continue
else:
 print('hello')

#break
for i in range(7):
    print(i)
    i = i+1
    break
else:
 print('hello')

#pass
 for i in range(7):
    print(i)
    i = i+1
    pass
else:
 print('hello')'''


#custom error:
'''a = input('enter yuor word :')
if (a == 'QUIT/quit/Quit'):
    print(a)
else:
    raise TypeError('enter proper word')'''


#SHORT-HAND IF-ELSE STATEMENT :
'''a = 33
b = 34
#print(a)if (a==b) else print('=') if(a!=b)else print(b)
print(a) if(a>b) else print('=') if(a<b) else print(b)'''


#ENUMERATE FUNCTION :
'''index = 0
MARKS = [1,5,7,3,9,,8]
for mark,index in enumerate(MARKS):
    print(mark)
    if(index == 2):
        print('dimpal')'''

food = ['banana','apple','bhel','dhosa']

for i in (food):
    print(i)
a = input('enter your choise with number :')
try:
   print(food[a],'order')
  
    
except(TypeError,ValueError,IndexError):
  print('please,try again later')
finally:
  b = 'have a great day'
  print(b.capitalize())