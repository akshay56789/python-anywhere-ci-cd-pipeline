
def bubblesort(elements):
    size = len(elements)
    for i in range(size-1):
        swapped = False
        for j in range(size-1):
            if elements[j]>elements[j+1]:
                tmp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1]= tmp
                swapped = True
        if not swapped:
            break

kkk = []
elements = ['RDG: Raidurg', 'HTC: HITEC City', 'DGC: Durgam Cheruvu', 'MDP: Madhapur', 'PDG: Peddamma Gudi', 'JHC: Jubilee Hills Check Post', 'RJH: Road No. 5 Jubilee Hills', 'GCS: Yusufguda', 'MDN: Madhura Nagar', 'AMR: Ameerpet', 'SRN: S R Nagar', 'BGM: Begumpet', 'PJG: Panjagutta', 'PKN: Prakash Nagar', 'RSL: Rasoolpura', 'PRD: Paradise', 'PRG: Parade Ground', 'SEM: Secunderabad East Metro Station', 'MTG: Mettuguda', 'TNK: Tarnaka', 'HBS: Habsiguda', 'NGR: Ngri', 'STD: Stadium', 'UPL: Uppal', 'NGL: Nagole', 'MYP: Miyapur', 'JNC: JNTU College', 'KPH: KPHB Colony', 'KTP: Kukatpally',
         'BLN: Dr. BR Ambedkar Balanagar Metro Station', 'MSP: Moosapet', 'BRN: Bharat Nagar', 'ERG: Erragadda', 'ESI: ESI Hospital', 'IIM: Irrum Manzil', 'KRT: Khairatabad', 'LKD: Lakdikapul', 'ASM: Assembly', 'NMP: Nampally', 'GDB: Gandhi Bhavan', 'OMC: Osmania Medical College', 'MGB: MG Bus Station', 'SLB: Sultan Bazaar', 'MKP: Malakpet', 'NMR: New Market', 'MRB: Musarambagh', 'DSK: Dilsukhnagar', 'CMS: Chaitanyapuri Metro', 'VML: Victoria Memorial', 'LBN: LB Nagar', 'JBS: JBS Parade Ground', 'SCW: Secunderabad West', 'GHP: Gandhi Hospital', 'MSH: Musheerabad', 'RTC: RTC X Roads', 'CKD: Chikkadpally', 'NYN: Narayanaguda']
bubblesort(elements)
for i in elements:
    print('<option value=\''+i[:3]+'\'>' + i[5:] + '</option>')
