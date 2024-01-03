w = input('apka naame bataye :')
print('apkaa swagat he hamare kon banega karodapati ke python consent me',w,'\n')
'''h = ['1.list is muttable?','2.by using python ,we can predict stock market? ','3.python is a interpreter launange','4.ython have a built-in function?']
print('yee raha apke samne apka saval\n')

print(h[0])
o = input('inmese apka answer kya he?true/false :')
if o in 'true/True/TRUE':
        print('sahi javab, app jitt rahe he is sal ka naya toffa\n')
        print(h[1])
        f = input('inmese apka answer kya he?true/false :')
        
        if f in 'true/True/TRUE':
            print('sahi javab, app jitt rahe he is sal ka naya toffa\n')
            print(h[2])
            v = input('inmese apka answer kya he?true/false :')
            
            if v in 'TRUE/True/true':
                print('sahi javab, app jitt rahe he is sal ka naya toffa\n')
                print(h[3])
            else:
                print('stop')
                
        else:
            print('stop')
            
else:
    print('stop')
print('bhut acchaa')'''

question =[ 
    ['whose is maade afil tower :','burj khalifa','turkey','tutiya','brazil',3],
    ['whose is maade afil tower :','burj khalifa','turkey','tutiya','brazil',3],
    ['whose is maade afil tower :','burj khalifa','turkey','tutiya','brazil',3],
    ['whose is maade afil tower :','burj khalifa','turkey','tutiya','brazil',3],
    ['whose is maade afil tower :','burj khalifa','turkey','tutiya','brazil',3],
    ['whose is maade afil tower :','burj khalifa','turkey','tutiya','brazil',3],
    ['whose is maade afil tower :','burj khalifa','turkey','tutiya','brazil',3],
    ['whose is maade afil tower :','burj khalifa','turkey','tutiya','brazil',3],
    ['whose is maade afil tower :','burj khalifa','turkey','tutiya','brazil',3],
    ['whose is maade afil tower :','burj khalifa','turkey','tutiya','brazil',3],
    ['whose is maade afil tower :','burj khalifa','turkey','tutiya','brazil',3],
]
levels = [1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,11000,12000,13000,14000,15000]
money = 0
i = 0
for i in range(0, len(question)):
    question = question[i]
    print(f"question for rupee {levels[i]}")
    print(f"a.{question[1]}b.{question[2]}")
    print(f"c.{question[3]}d.{question[4]}")
    reply = int(input('enter any number 1-4 :'))
    if  (reply ==question[-1]):
        print(f'ccorrect answer ,you have won {levels[i]}')
        if(i == 4):
            money=10000
        elif(i == 8):
            money=20000
        elif(i == 10):
            money=40000
    else:
        print('wrong answer')
        break