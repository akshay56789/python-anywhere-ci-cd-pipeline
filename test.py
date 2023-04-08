list7 = ['Aluva','Pulinchodu','Companypady','Ambattukavu','Muttom','Kalamassery','Cochin_University','Pathadipalam','Edapally','Changampuzha','Palarivattom','JLN_Stadium','Kaloor','Lissie','MG_Road','Maharajas','Ernakulam_South','Kadavanthra','Elamkulam','Vytilla','Thaikoodam','Petta','Vadakkekotta','SN_Junction']
list8 = []
temp = len(list7)
for i in list7:
    list8.append(list7[temp-1])
    temp = temp-1

print(list8)