from django.shortcuts import HttpResponse, render
from home.models import Fare, Kochi_fare,Jaipur_fare


def home(request):
    return render(request, 'home.html')

def kanpur(request):
    return render(request, 'kanpurfare.html')

def jaipurfare(request):
    return render(request,'jaipurfare.html')

def jaipurresult(request):
    if request.method == 'GET':
        value1 = request.GET.get('origin', "")
        value2 = request.GET.get('dest', "")
    
    print(value1)
    print(value2)
    dict2 = {'Mansarovar':0,'New_Aatish_Market':1,'Vivek_Vihar':2, 'Shayam_Nagar':3,'Ram_Nagar':4,'Civil_Lines':5,'Jaipur_Metro_Station':6,'Sindhi_Camp':7,'Chandpole':8,'Chhoti_Chaupar':9,'Badi_Chaupar':10}
    jpm = Jaipur_fare.objects.all()
    string = "jpm[dict2.get(value1)]." + value2
    fare2 = eval(string) #fare
    

    #myresult = mycursor.fetchall()
    #print(myresult[0][0])
    #result = myresult[0][0]
   
    list7 = ['Mansarovar','New_Aatish_Market','Vivek_Vihar','Shayam_Nagar','Ram_Nagar','Civil_Lines','Jaipur_Metro_Station','Sindhi_Camp','Chandpole','Chhoti_Chaupar','Badi_Chaupar']
    list8 = ['Badi_Chaupar', 'Chhoti_Chaupar', 'Chandpole', 'Sindhi_Camp', 'Jaipur_Metro_Station', 'Civil_Lines', 'Ram_Nagar', 'Shayam_Nagar', 'Vivek_Vihar', 'New_Aatish_Market', 'Mansarovar']
    list5 = []
    list6=[]
    list9 = []
    list10 = []
    for i in range(list7.index(value1)+1, len(list7)):
        list5.append(list7[i])
    


    if value2 in list5:
        print(list5)
        list9 = list5[:list5.index(value2)]
        print(list9)
        
    else:
        for i in range(list8.index(value1)+1, len(list8)):
            list6.append(list8[i])
        print(list6)
        list10 = list6[:list6.index(value2)]
        print(list10)
        

    no1 = len(list9) #length of list for stations up
    no2 = len(list10) #station down

    list11 = []
    list12 = [] 
    for i in list9:
        temp1 = i.split("_")
        list11.append(" ".join(temp1))
    print(list11)

    for i in list10:
        temp2 = i.split("_")
        list12.append(" ".join(temp2))
    print(list12)

    temp3 = value1.split("_")
    value3 = " ".join(temp3)

    temp4 = value2.split("_")
    value4 = " ".join(temp4)
    
    context = {'value1':value3, 'value2':value4, 'list9':list11,'list10':list12,'result':fare2,'no1':no1,'no2':no2}
    return render(request, 'jaipurresult.html', context)

def result(request):
    if request.method == 'GET':
        value1 = request.GET.get('origin', "")
        value2 = request.GET.get('dest', "")
    #mydb.reconnect()
    #mycursor = mydb.cursor()
    #mycursor.execute("SELECT "+value1+" FROM kanpur_fare WHERE STATIONS = '"+value2+"';")
    dict1 = {'IIT_Kanpur':8,'Kalyanpur':7,'SPM_Hospital':6, 'Vishwavidyalay':5,'Gurudev_Chauraha':4,'Geeta_Nagar':3,'Rawatpur':2,'Lala_Lajpat_Rai_Hospital':1,'Motijheel':0}
    aks = Fare.objects.all()
    string = "aks[dict1.get(value1)]." + value2
    fare1 = eval(string) #fare
    

    #myresult = mycursor.fetchall()
    #print(myresult[0][0])
    #result = myresult[0][0]
   
    list7 = ['IIT_Kanpur','Kalyanpur','SPM_Hospital','Vishwavidyalay','Gurudev_Chauraha','Geeta_Nagar','Rawatpur','Lala_Lajpat_Rai_Hospital','Motijheel']
    list8 = ['Motijheel','Lala_Lajpat_Rai_Hospital','Rawatpur','Geeta_Nagar','Gurudev_Chauraha','Vishwavidyalay','SPM_Hospital','Kalyanpur','IIT_Kanpur']
    list5 = []
    list6=[]
    list9 = []
    list10 = []
    for i in range(list7.index(value1)+1, len(list7)):
        list5.append(list7[i])
    


    if value2 in list5:
        print(list5)
        list9 = list5[:list5.index(value2)]
        print(list9)
        
    else:
        for i in range(list8.index(value1)+1, len(list8)):
            list6.append(list8[i])
        print(list6)
        list10 = list6[:list6.index(value2)]
        print(list10)
        

    no1 = len(list9) #length of list for stations up
    no2 = len(list10) #station down

    list11 = []
    list12 = [] 
    for i in list9:
        temp1 = i.split("_")
        list11.append(" ".join(temp1))
    print(list11)

    for i in list10:
        temp2 = i.split("_")
        list12.append(" ".join(temp2))
    print(list12)

    temp3 = value1.split("_")
    value3 = " ".join(temp3)

    temp4 = value2.split("_")
    value4 = " ".join(temp4)
    
    context = {'value1':value3, 'value2':value4, 'list9':list11,'list10':list12,'result':fare1,'no1':no1,'no2':no2}
    
    return render(request, 'result.html', context)

def nagpurfare(request):
    return render(request, 'nagpurfare.html')

def nagpurresult(request):  
    if request.method == 'GET':
        value1 = request.GET.get('origin', "")
        value2 = request.GET.get('dest', "")
    
    cnt = []
    intc = "No interchange"
    print(value1)
    print(value2)
    aqua = ['pjn', 'vns', 'abs', 'tpe', 'cts', 'ags', 'dvs', 'nps', 'stb',
        'jrs', 'ioe', 'sns', 'lds', 'dpc', 'sbn', 'rrr', 'vdn', 'ban', 'lmn']  # east to west
    aqua_rev = ['lmn', 'ban', 'vdn', 'rrr', 'sbn', 'dpc', 'lds', 'sns', 'ioe',
            'jrs', 'stb', 'nps', 'dvs', 'ags', 'cts', 'tpe', 'abs', 'vns', 'pjn']  # west to east
    org = ['khp', 'nap', 'sap', 'aip', 'ujn', 'jpn', 'cps', 'ajs',
       'rhc', 'cgn', 'stb', 'zm', 'kcp', 'gdg', 'kdc', 'nrr', 'aus']  # south to north
    org_rev = ['aus', 'nrr', 'kdc', 'gdg', 'kcp', 'zm', 'stb', 'cgn',
           'rhc', 'ajs', 'cps', 'jpn', 'ujn', 'aip', 'sap', 'nap', 'khp']  # north to south

    ########################################################################
    if value1 in aqua and value2 in aqua[aqua.index(value1):]:
        for i in range(aqua.index(value1), aqua.index(value2)+1):
            cnt.append(aqua[i])
        stn_btw = cnt[1:-1]
        stnbtw_count = len(stn_btw)
        lststn_count = len(cnt[1:])

    elif value1 in aqua[0:aqua.index('stb')] and value2 in org[org.index('stb'):]:#north
        for i in range(aqua.index(value1), aqua.index('stb')):
            cnt.append(aqua[i])
        for j in range(org.index('stb'),org.index(value2)+1):
            cnt.append(org[j])
            intc = "Interchange train from Sitabuldi EW Corridor to Sitabuldi NS Corridor"
            stn_btw = cnt[1:-1]
            stnbtw_count = len(stn_btw)
            lststn_count = len(cnt[1:])

    elif value1 in aqua[0:aqua.index('stb')] and value2 in org_rev[org_rev.index('stb'):]:
        for i in range(aqua.index(value1), aqua.index('stb')):
            cnt.append(aqua[i])
        for j in range(org_rev.index('stb'),org_rev.index(value2)+1):
            cnt.append(org_rev[j])
            intc = "Interchange train from Sitabuldi EW Corridor to Sitabuldi NS Corridor"
            stn_btw = cnt[1:-1]
            stnbtw_count = len(stn_btw)
            lststn_count = len(cnt[1:])
########################################################################

#######################################################################
    if value1 in aqua_rev and value2 in aqua_rev[aqua_rev.index(value1):]:
        for i in range(aqua_rev.index(value1), aqua_rev.index(value2)+1):
            cnt.append(aqua_rev[i])
        stn_btw = cnt[1:-1]
        stnbtw_count = len(stn_btw)
        lststn_count = len(cnt[1:])

    elif value1 in aqua_rev[0:aqua_rev.index('stb')] and value2 in org[org.index('stb'):]:#north
        for i in range(aqua_rev.index(value1), aqua_rev.index('stb')):
            cnt.append(aqua_rev[i])
        for j in range(org.index('stb'),org.index(value2)+1):
            cnt.append(org[j])
            intc = "Interchange train from Sitabuldi EW Corridor to Sitabuldi NS Corridor"
            stn_btw = cnt[1:-1]
            stnbtw_count = len(stn_btw)
            lststn_count = len(cnt[1:])

    elif value1 in aqua_rev[0:aqua_rev.index('stb')] and value2 in org_rev[org_rev.index('stb'):]:
        for i in range(aqua_rev.index(value1), aqua_rev.index('stb')):
            cnt.append(aqua_rev[i])
        for j in range(org_rev.index('stb'),org_rev.index(value2)+1):
            cnt.append(org_rev[j])
            intc = "Interchange train from Sitabuldi EW Corridor to Sitabuldi NS Corridor"
            stn_btw = cnt[1:-1]
            stnbtw_count = len(stn_btw)
            lststn_count = len(cnt[1:])
####################################################################################

########################################################################################
    if value1 in org and value2 in org[org.index(value1):]:
        for i in range(org.index(value1), org.index(value2)+1):
            cnt.append(org[i])
        stn_btw = cnt[1:-1]
        stnbtw_count = len(stn_btw)
        lststn_count = len(cnt[1:])

    elif value1 in org[0:org.index('stb')] and value2 in aqua[aqua.index('stb'):]:#west
        for i in range(org.index(value1), org.index('stb')):
            cnt.append(org[i])
        for j in range(aqua.index('stb'),aqua.index(value2)+1):
            cnt.append(aqua[j])
            intc = "Interchange train from Sitabuldi NS Corridor to Sitabuldi EW Corridor"
            stn_btw = cnt[1:-1]
            stnbtw_count = len(stn_btw)
            lststn_count = len(cnt[1:])

    elif value1 in org[0:org.index('stb')] and value2 in aqua_rev[aqua_rev.index('stb'):]:#east
        for i in range(org.index(value1), org.index('stb')):
            cnt.append(org[i])
        for j in range(aqua_rev.index('stb'),aqua_rev.index(value2)+1):
            cnt.append(aqua_rev[j])
            intc = "Interchange train from Sitabuldi NS Corridor to Sitabuldi EW Corridor"
            stn_btw = cnt[1:-1]
            stnbtw_count = len(stn_btw)
            lststn_count = len(cnt[1:])
#####################################################################################

##########################################################################################
    elif value1 in org_rev and value2 in org_rev[org_rev.index(value1):]:
        for i in range(org_rev.index(value1), org_rev.index(value2)+1):
            cnt.append(org_rev[i])
        stn_btw = cnt[1:-1]
        stnbtw_count = len(stn_btw)
        lststn_count = len(cnt[1:])

    elif value1 in org_rev[0:org_rev.index('stb')] and value2 in aqua[aqua.index('stb'):]:#west
        for i in range(org_rev.index(value1), org_rev.index('stb')):
            cnt.append(org_rev[i])
        for j in range(aqua.index('stb'),aqua.index(value2)+1):
            cnt.append(aqua[j])
            intc = "Interchange train from Sitabuldi NS Corridor to Sitabuldi EW Corridor"
            stn_btw = cnt[1:-1]
            stnbtw_count = len(stn_btw)
            lststn_count = len(cnt[1:])

    elif value1 in org_rev[0:org_rev.index('stb')] and value2 in aqua_rev[aqua_rev.index('stb'):]:#east
        for i in range(org_rev.index(value1), org_rev.index('stb')):
            cnt.append(org_rev[i])
        for j in range(aqua_rev.index('stb'),aqua_rev.index(value2)+1):
            cnt.append(aqua_rev[j])
            intc = "Interchange train from Sitabuldi NS Corridor to Sitabuldi EW Corridor"
            stn_btw = cnt[1:-1]
            stnbtw_count = len(stn_btw)
            lststn_count = len(cnt[1:])
###################################################################################

    stn_dict = {'pjn': 'Prajapati Nagar', 'vns': 'Vaishnodevi Square', 'abs': 'Ambedkar Square', 'tpe': 'Telephone Exchange', 'cts': 'Chitroli Square', 'ags': 'Agrasen Square', 'dvs': 'Dosar Vaishya Square', 'nps': 'Nagpur Railway Station', 'stb': 'Sitabuldi', 'jrs': 'Jhansi Rani Square', 'ioe': 'Institution of Engineers', 'sns': 'Shankar Nagar Square', 'lds': 'LAD Square', 'dpc': 'Dharampeth College', 'sbn': 'Subhash Nagar Square', 'rrr': 'Rachana Ring Road Junction',
            'vdn': 'Vasudev Nagar', 'ban': 'Bansi Nagar', 'lmn': 'Lokmanya Nagar', 'khp': 'Khapri', 'nap': 'New Airport', 'sap': 'Airport South', 'aip': 'Airport', 'ujn': 'Ujjwal Nagar', 'jpn': 'Jaiprakash Nagar', 'cps': 'Chhatrapati Square', 'ajs': 'Ajni Square', 'rhc': 'Rahate Colony', 'cgn': 'Congress Nagar', 'zm': 'Zero Mile Freedom Park', 'kcp': 'Kasturchand Park', 'gdg': 'Gaddigodam Square', 'kdc': 'Kadbi Square', 'nrr': 'Nari Road', 'aus': 'Automotive Square','iew':'Interchange to Sitabuldi EW Corridor','ins':'Interchange to Sitabuldi NS Corridor'}
    cnt1 = []
    stnbtw_new=[]
    for i in cnt:
        cnt1.append(stn_dict.get(i))
    for i in stn_btw:
        stnbtw_new.append(stn_dict.get(i))
    print(stnbtw_new)
    print(stnbtw_count)
    print(lststn_count)
    new_value1 = stn_dict.get(value1)
    new_value2 = stn_dict.get(value2)
    #fare
    if(lststn_count == 1):
        price = 10
    elif(1 < lststn_count <=2 ):
        price = 15
    elif(2 < lststn_count  <=3):
        price = 20
    elif(3 < lststn_count <=8):
        price = 25
    elif(8 < lststn_count <=13):
        price = 30
    elif(13 < lststn_count <=15):
        price = 35
    elif(15<lststn_count):
        price = 41
    context = {'value1':new_value1,'value2':new_value2,'list':stnbtw_new,'no':stnbtw_count,'intc':intc,'fare':price}
    return render(request,'nagpurresult.html',context)


def kochifare(request):
    return render(request, 'kochifare.html')

def kochiresult(request):
    if request.method == 'GET':
        value1 = request.GET.get('origin', "")
        value2 = request.GET.get('dest', "")
    #mydb.reconnect()
    #mycursor = mydb.cursor()
    #mycursor.execute("SELECT "+value1+" FROM kanpur_fare WHERE STATIONS = '"+value2+"';")
    print(value1)
    print(value2)
    dict1 = {'Aluva':0,'Pulinchodu':1,'Companypady':2, 'Ambattukavu':3,'Muttom':4,'Kalamassery':5,'Cochin_University':6,'Pathadipalam':7,'Edapally':8,'Changampuzha':9,'Palarivattom':10,'JLN_Stadium':11,'Kaloor':12,'Lissie':13,'MG_Road':14,'Maharajas':15,'Ernakulam_South':16,'Kadavanthra':17,'Elamkulam':18,'Vytilla':19,'Thaikoodam':20,'Petta':21,'Vadakkekotta':22,'SN_Junction':23}
    lkh = Kochi_fare.objects.all()
    string = "lkh[dict1.get(value1)]." + value2
    fare = eval(string) #fare
    

    #myresult = mycursor.fetchall()
    #print(myresult[0][0])
    #result = myresult[0][0]
   
    list7 = ['Aluva','Pulinchodu','Companypady','Ambattukavu','Muttom','Kalamassery','Cochin_University','Pathadipalam','Edapally','Changampuzha','Palarivattom','JLN_Stadium','Kaloor','Lissie','MG_Road','Maharajas','Ernakulam_South','Kadavanthra','Elamkulam','Vytilla','Thaikoodam','Petta','Vadakkekotta','SN_Junction']
    list8 = ['SN_Junction', 'Vadakkekotta', 'Petta', 'Thaikoodam', 'Vytilla', 'Elamkulam', 'Kadavanthra', 'Ernakulam_South', 'Maharajas', 'MG_Road', 'Lissie', 'Kaloor', 'JLN_Stadium', 'Palarivattom', 'Changampuzha', 'Edapally', 'Pathadipalam', 'Cochin_University', 'Kalamassery', 'Muttom', 'Ambattukavu', 'Companypady', 'Pulinchodu', 'Aluva']
    list5 = []
    list6=[]
    list9 = []
    list10 = []
    for i in range(list7.index(value1)+1, len(list7)):
        list5.append(list7[i])
    


    if value2 in list5:
        print(list5)
        list9 = list5[:list5.index(value2)]
        print(list9)
        
    else:
        for i in range(list8.index(value1)+1, len(list8)):
            list6.append(list8[i])
        print(list6)
        list10 = list6[:list6.index(value2)]
        print(list10)
        

    no1 = len(list9) #length of list for stations up
    no2 = len(list10) #station down

    list11 = []
    list12 = [] 
    for i in list9:
        temp1 = i.split("_")
        list11.append(" ".join(temp1))
    print(list11)

    for i in list10:
        temp2 = i.split("_")
        list12.append(" ".join(temp2))
    print(list12)

    temp3 = value1.split("_")
    value3 = " ".join(temp3)

    temp4 = value2.split("_")
    value4 = " ".join(temp4)
    
    context = {'value1':value3, 'value2':value4, 'list9':list11,'list10':list12,'result':fare,'no1':no1,'no2':no2}
    return render(request, 'kochiresult.html', context)

def timings(request):
    if request.method == 'GET':
        value1 = request.GET.get('cars1', "")
    #mycursor = mydb.cursor()
    #mycursor.execute("SELECT TRIP1, TRIP2, TRIP3, TRIP4, TRIP5 FROM kanpur_tt WHERE STATIONS = '"+value1+"';")
    #myresult = mycursor.fetchall()
    #print(value1)
    #print(myresult)

    return render(request, 'timings.html')