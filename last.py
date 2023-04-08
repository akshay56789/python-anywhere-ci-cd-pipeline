value1 = 'gdg'
value2 = 'abs'
cnt = []
print(value1)
print(value2)
intc = "No interchange"
aqua = ['pjn', 'vns', 'abs', 'tpe', 'cts', 'ags', 'dvs', 'nps', 'stb',
        'jrs', 'ioe', 'sns', 'lds', 'dpc', 'sbn', 'rrr', 'vdn', 'ban', 'lmn']
aqua_rev = ['lmn', 'ban', 'vdn', 'rrr', 'sbn', 'dpc', 'lds', 'sns', 'ioe',
            'jrs', 'stb',  'nps', 'dvs', 'ags', 'cts', 'tpe', 'abs', 'vns', 'pjn']
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
        intc = "Active"
        stn_btw = cnt[1:-1]
        stnbtw_count = len(stn_btw)
        lststn_count = len(cnt[1:])

elif value1 in aqua[0:aqua.index('stb')] and value2 in org_rev[org_rev.index('stb'):]:
    for i in range(aqua.index(value1), aqua.index('stb')):
        cnt.append(aqua[i])
    for j in range(org_rev.index('stb'),org_rev.index(value2)+1):
        cnt.append(org_rev[j])
        intc = "Active"
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
        intc = "Active"
        stn_btw = cnt[1:-1]
        stnbtw_count = len(stn_btw)
        lststn_count = len(cnt[1:])

elif value1 in aqua_rev[0:aqua_rev.index('stb')] and value2 in org_rev[org_rev.index('stb'):]:
    for i in range(aqua_rev.index(value1), aqua_rev.index('stb')):
        cnt.append(aqua_rev[i])
    for j in range(org_rev.index('stb'),org_rev.index(value2)+1):
        cnt.append(org_rev[j])
        intc = "Active"
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
        intc = "Active"
        stn_btw = cnt[1:-1]
        stnbtw_count = len(stn_btw)
        lststn_count = len(cnt[1:])

elif value1 in org[0:org.index('stb')] and value2 in aqua_rev[aqua_rev.index('stb'):]:#east
    for i in range(org.index(value1), org.index('stb')):
        cnt.append(org[i])
    for j in range(aqua_rev.index('stb'),aqua_rev.index(value2)+1):
        cnt.append(aqua_rev[j])
        intc = "Active"
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
        intc = "Active"
        stn_btw = cnt[1:-1]
        stnbtw_count = len(stn_btw)
        lststn_count = len(cnt[1:])

elif value1 in org_rev[0:org_rev.index('stb')] and value2 in aqua_rev[aqua_rev.index('stb'):]:#east
    for i in range(org_rev.index(value1), org_rev.index('stb')):
        cnt.append(org_rev[i])
    for j in range(aqua_rev.index('stb'),aqua_rev.index(value2)+1):
        cnt.append(aqua_rev[j])
        intc = "Active"
        stn_btw = cnt[1:-1]
        stnbtw_count = len(stn_btw)
        lststn_count = len(cnt[1:])
###################################################################################





















stn_dict = {'pjn': 'Prajapati Nagar', 'vns': 'Vaishnodevi Square', 'abs': 'Ambedkar Square', 'tpe': 'Telephone Exchange', 'cts': 'Chitroli Square', 'ags': 'Agrasen Square', 'dvs': 'Dosar Vaishya Square', 'nps': 'Nagpur Railway Station', 'stb': 'Sitabuldi', 'jrs': 'Jhansi Rani Square', 'ioe': 'Institution of Engineers', 'sns': 'Shankar Nagar Square', 'lds': 'LAD Square', 'dpc': 'Dharampeth College', 'sbn': 'Subhash Nagar Square', 'rrr': 'Rachana Ring Road Junction',
            'vdn': 'Vasudev Nagar', 'ban': 'Bansi Nagar', 'lmn': 'Lokmanya Nagar', 'khp': 'Khapri', 'nap': 'New Airport', 'sap': 'Airport South', 'aip': 'Airport', 'ujn': 'Ujjwal Nagar', 'jpn': 'Jaiprakash Nagar', 'cps': 'Chhatrapati Square', 'ajs': 'Ajni Square', 'rhc': 'Rahate Colony', 'cgn': 'Congress Nagar', 'zm': 'Zero Mile Freedom Park', 'kcp': 'Kasturchand Park', 'gdg': 'Gaddigodam Square', 'kdc': 'Kadbi Square', 'nrr': 'Nari Road', 'aus': 'Automotive Square', 'iew': 'Interchange to Sitabuldi EW Corridor', 'ins': 'Interchange to Sitabuldi NS Corridor'}
cnt1 = []
stnbtw_new = []
for i in cnt:
    cnt1.append(stn_dict.get(i))
for i in stn_btw:
    stnbtw_new.append(stn_dict.get(i))
print(stnbtw_new)
print(stnbtw_count)
print(lststn_count)
print(intc)
