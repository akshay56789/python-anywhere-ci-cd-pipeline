
value1 = 'rhc'
value2 = 'cps'

print(value1)
print(value2)

list7 = ['pjn','vns','abs','tpe','cts','ags','dvs','nps','stb','jrs','ioe','sns','lc','dpc','sbn','rrr','vdn','ban','lmn']
list8 = ['lmn','ban','vdn','rrr','sbn','dpc','lc','sns','ioe','jrs','stb','nps','dvs','ags','cts','tpe','abs','vns','pjn']
int1 = ['khp','nap','sap','aip','ujn','jpn','cps','ajs','rhc','cgn','stb','zm','kcp','gdg','kdc','nrr','aus']
list5 = []
list6 = []
list9 = []
list10 = []
akshay = []
if(value2 not in list7):
     for j in range(list7.index(value1), list7.index('stb')):
          akshay.append(list7[j])
for i in range(list7.index(value1)+1, len(list7)):
    list5.append(list7[i])

if value2 in list5:
    print(list5)
    list9 = list5[:list5.index(value2)+1]
    print(list9)

else:
    for i in range(list8.index(value1)+1, len(list8)):
        list6.append(list8[i])
    print(list6)
    list10 = list6[:list6.index(value2)+1]
    print(list10)

no1 = len(list9)  # length of list for stations up
no2 = len(list10)  # station down

list11 = []
list12 = []
for i in list9:
        temp1 = i.split("_")
        list11.append(" ".join(temp1))
print(list11)
no1 = len(list11)
print(len(list11))

for i in list10:
        temp2 = i.split("_")
        list12.append(" ".join(temp2))
print(list12)
no2 = len(list12)
print(len(list12))

temp3 = value1.split("_")
value3 = " ".join(temp3)

temp4 = value2.split("_")
value4 = " ".join(temp4)

if(no1 == 1):
     price = 10
elif(1 < no1 or no2 <=3 ):
     price = 15
elif(3 < no1 or no2 <=6):
     price = 20
elif(6 < no1 or no2 <=9):
     price = 25
elif(9 < no1 or no2 <=15):
     price = 30
elif(15 < no1 or no2 <=18):
     price = 35
print('price='+str(price) ) 

