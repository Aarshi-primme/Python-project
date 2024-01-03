a = [2,5,6,'h']
print(a[0:3])
#list comprehension
b = [i for i in range(4)]
print(b)
b = [i for i in range(4) if i%2==0]
print(b)

#list method

g = [1,2,6,4,9,8]

g.append(7)
print(g)

g.sort()
print(g)#only uspoort into int not string

g.reverse()
print(g)
print(g.index(1))

print(g.count(1))

m = [554,776,65757]
print(g.extend(m))#join one or more element add into the listinthe first time
print(g)

k = g+m
print(k)

#tuple
#tuple are not chanagable(immutable)
t = (1,3,4,4)
print(type(t),t)
print(t[3])
if 3 in t:
    print('hello')
    
#convert list into tuple or viseversa
u = list(t)
u.append(5)
print(u)
r = tuple(u)
print(r)

#concatingnate,duplicattion,length,index
#we can add two or more tuple
#tuple.index(element,start,stop) print(tuple)





