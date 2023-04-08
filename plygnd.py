value1 = 'vns'
value2 = 'sns'
cnt = []
print(value1)
print(value2)
intc = "No interchange"
aqua = ['pjn', 'vns', 'abs', 'tpe', 'cts', 'ags', 'dvs', 'nps', 'stb',
        'jrs', 'ioe', 'sns', 'lds', 'dpc', 'sbn', 'rrr', 'vdn', 'ban', 'lmn']  # east to west
aqua_rev = ['lmn', 'ban', 'vdn', 'rrr', 'sbn', 'dpc', 'lds', 'sns', 'ioe',
            'jrs', 'stb', 'nps', 'dvs', 'ags', 'cts', 'tpe', 'abs', 'vns', 'pjn']  # west to east
org = ['khp', 'nap', 'sap', 'aip', 'ujn', 'jpn', 'cps', 'ajs',
       'rhc', 'cgn', 'stb', 'zm', 'kcp', 'gdg', 'kdc', 'nrr', 'aus']  # south to north
org_rev = ['aus', 'nrr', 'kdc', 'gdg', 'kcp', 'zm', 'stb', 'cgn',
           'rhc', 'ajs', 'cps', 'jpn', 'ujn', 'aip', 'sap', 'nap', 'khp']  # north to south


# from aqua east to orange north or south


#if value1 and value2 in aqua_rev:
#    for i in range(aqua_rev.index(value1),aqua_rev.index(value2)+1):
#        cnt.append(aqua_rev[i])

# if value1 and value2 in org:
    # for i in range(org.index(value1),org.index(value2)+1):
        # cnt.append(org[i])

# if value1 and value2 in org_rev:
    # for i in range(org_rev.index(value1),org_rev.index(value2)+1):
        # cnt.append(org_rev[i])




if value1 in aqua:
    if value1 and value2 in aqua[0:aqua.index('stb')]:
        for i in range(aqua.index(value1),aqua.index(value2)+1):
            cnt.append(aqua[i])
        print(cnt)
        stn_btw = cnt[1:-1]
        print(stn_btw)
        stnbtw_count = len(stn_btw)
        lststn_count = len(cnt[1:]) 
    
    if value1 and value2 in aqua[aqua.index('stb'):]:
        for i in range(aqua.index(value1),aqua.index(value2)+1):
            cnt.append(aqua[i])
        print(cnt)
        stn_btw = cnt[1:-1]
        print(stn_btw)
        stnbtw_count = len(stn_btw)
        lststn_count = len(cnt[1:]) 

    if value1 in aqua[0:aqua.index('stb')]:
        if value2 in aqua[aqua.index('stb'):]:
            for i in range(aqua.index(value1), aqua.index(value2)+1):
                cnt.append(aqua[i])
            print(cnt)  # from aqua east to aqua west
            stn_btw = cnt[1:-1]
            print(stn_btw)
            stnbtw_count = len(stn_btw)
            lststn_count = len(cnt[1:])
        
        elif value2 not in aqua:
            if value2 in org[org.index('stb'):]:  # going to north
                for i in range(aqua.index(value1), aqua.index('stb')):
                    cnt.append(aqua[i])
                print(cnt)
                for j in range(org.index('stb'), org.index(value2)+1):
                   cnt.append(org[j])
                print(cnt)
                intc = "Interchnage trains from EW to NS"
                print(intc)
                stn_btw = cnt[1:-1]
                print(stn_btw)
                stnbtw_count = len(stn_btw)
                lststn_count = len(cnt[1:])
            elif value2 in org_rev[org_rev.index('stb'):]:  # going to south
                for i in range(aqua.index(value1), aqua.index('stb')):
                    cnt.append(aqua[i])
                print(cnt)
                for j in range(org_rev.index('stb'), org_rev.index(value2)+1):
                    cnt.append(org_rev[j])
                print(cnt)
                intc = "Interchnage trains from EW to NS"
                print(intc)
                stn_btw = cnt[1:-1]
                print(stn_btw)
                stnbtw_count = len(stn_btw)
                lststn_count = len(cnt[1:])




# from aqua west to orange north or south


elif value1 in aqua_rev:
    

    if value2 in aqua_rev:
        for i in range(aqua_rev.index(value1), aqua_rev.index(value2)+1):
            cnt.append(aqua_rev[i])
        print(cnt)  # from aqua west to aqua east
        stn_btw = cnt[1:-1]
        print(stn_btw)
        stnbtw_count = len(stn_btw)
        lststn_count = len(cnt[1:])
    elif value2 not in aqua_rev:
        if value2 in org[org.index('stb'):]:  # going to north
            for i in range(aqua_rev.index(value1), aqua_rev.index('stb')):
                cnt.append(aqua_rev[i])
            print(cnt)
            for j in range(org.index('stb'), org.index(value2)+1):
                cnt.append(org[j])
            print(cnt)
            intc = "Interchnage trains from EW to NS"
            print(intc)
            stn_btw = cnt[1:-1]
            print(stn_btw)
            stnbtw_count = len(stn_btw)
            lststn_count = len(cnt[1:])
        elif value2 in org_rev[org_rev.index('stb'):]:  # going to south
            for i in range(aqua_rev.index(value1), aqua_rev.index('stb')):
                cnt.append(aqua_rev[i])
            print(cnt)
            for j in range(org_rev.index('stb'), org_rev.index(value2)+1):
                cnt.append(org_rev[j])
            print(cnt)
            intc = "Interchnage trains from EW to NS"
            print(intc)
            stn_btw = cnt[1:-1]
            print(stn_btw)
            stnbtw_count = len(stn_btw)
            lststn_count = len(cnt[1:])




# from org south to org north, to aqua west and east
elif value1 in org[0:org.index('stb')]:
    if value2 in org:
        for i in range(org.index(value1), org.index(value2)+1):
            cnt.append(org[i])
        print(cnt)  # from org south to org north
        stn_btw = cnt[1:-1]
        print(stn_btw)
        stnbtw_count = len(stn_btw)
        lststn_count = len(cnt[1:])
    elif value2 not in org:
        if value2 in aqua[aqua.index('stb'):]:  # going to west
            for i in range(org.index(value1), org.index('stb')):
                cnt.append(org[i])
            print(cnt)
            for j in range(aqua.index('stb'), aqua.index(value2)+1):
                cnt.append(aqua[j])
            print(cnt)
            intc = "Interchnage trains from NS to EW"
            print(intc)
            stn_btw = cnt[1:-1]
            print(stn_btw)
            stnbtw_count = len(stn_btw)
            lststn_count = len(cnt[1:])
        elif value2 in aqua_rev[aqua_rev.index('stb'):]:  # going to east
            for i in range(org.index(value1), org.index('stb')):
                cnt.append(org[i])
            print(cnt)
            for j in range(aqua_rev.index('stb'), aqua_rev.index(value2)+1):
                cnt.append(aqua_rev[j])
            print(cnt)
            intc = "Interchnage trains from NS to EW"
            print(intc)
            stn_btw = cnt[1:-1]
            print(stn_btw)
            stnbtw_count = len(stn_btw)
            lststn_count = len(cnt[1:])




# from org north to org south, to aqua west and east
elif value1 in org_rev[0:org_rev.index('stb')]:
    if value2 in org_rev:
        for i in range(org_rev.index(value1), org_rev.index(value2)+1):
            cnt.append(org_rev[i])
        print(cnt)  # from org north to org south
        stn_btw = cnt[1:-1]
        print(stn_btw)
        stnbtw_count = len(stn_btw)
        lststn_count = len(cnt[1:])
    elif value2 not in org_rev:
        if value2 in aqua[aqua.index('stb'):]:  # going to west
            for i in range(org_rev.index(value1), org_rev.index('stb')):
                cnt.append(org_rev[i])
            print(cnt)
            for j in range(aqua.index('stb'), aqua.index(value2)+1):
                cnt.append(aqua[j])
            print(cnt)
            intc = "Interchnage trains from NS to EW"
            print(intc)
            stn_btw = cnt[1:-1]
            print(stn_btw)
            stnbtw_count = len(stn_btw)
            lststn_count = len(cnt[1:])
        elif value2 in aqua_rev[aqua_rev.index('stb'):]:  # going to east
            for i in range(org_rev.index(value1), org_rev.index('stb')):
                cnt.append(org_rev[i])
            print(cnt)
            for j in range(aqua_rev.index('stb'), aqua_rev.index(value2)+1):
                cnt.append(aqua_rev[j])
            print(cnt)
            intc = "Interchnage trains from NS to EW"
            print(intc)
            stn_btw = cnt[1:-1]
            print(stn_btw)
            stnbtw_count = len(stn_btw)
            lststn_count = len(cnt[1:])
else:
    print("error!")

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
print(intc)


