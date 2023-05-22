from django.db import models

class Fare(models.Model):
    station_name = models.CharField(max_length=30)
    IIT_Kanpur = models.CharField(max_length=5)
    Kalyanpur = models.CharField(max_length=5)
    SPM_Hospital = models.CharField(max_length=5)
    Vishwavidyalay = models.CharField(max_length=5)
    Gurudev_Chauraha = models.CharField(max_length=5)
    Geeta_Nagar = models.CharField(max_length=5)
    Rawatpur = models.CharField(max_length=5)
    Lala_Lajpat_Rai_Hospital = models.CharField(max_length=5)
    Motijheel = models.CharField(max_length=5)
    
    def __str__(self):
        return self.station_name
        
class Kochi_fare(models.Model):
    station_name = models.CharField(max_length=30)
    Aluva = models.CharField(max_length=5)
    Pulinchodu = models.CharField(max_length=5)
    Companypady = models.CharField(max_length=5)
    Ambattukavu = models.CharField(max_length=5)
    Muttom = models.CharField(max_length=5)
    Kalamassery = models.CharField(max_length=5)
    Cochin_University = models.CharField(max_length=5)
    Pathadipalam = models.CharField(max_length=5)
    Edapally = models.CharField(max_length=5)
    Changampuzha = models.CharField(max_length=5)
    Palarivattom = models.CharField(max_length=5)
    JLN_Stadium = models.CharField(max_length=5)
    Kaloor = models.CharField(max_length=5)
    Lissie = models.CharField(max_length=5)
    MG_Road = models.CharField(max_length=5)
    Maharajas = models.CharField(max_length=5)
    Ernakulam_South = models.CharField(max_length=5)
    Kadavanthra = models.CharField(max_length=5)
    Elamkulam = models.CharField(max_length=5)
    Vytilla = models.CharField(max_length=5)
    Thaikoodam = models.CharField(max_length=5)
    Petta = models.CharField(max_length=5)
    Vadakkekotta = models.CharField(max_length=5)
    SN_Junction = models.CharField(max_length=5)

    def __str__(self):
        return self.station_name
    
class Jaipur_fare(models.Model):
    station_name = models.CharField(max_length=30)
    Mansarovar = models.CharField(max_length=5)
    New_Aatish_Market = models.CharField(max_length=5)
    Vivek_Vihar = models.CharField(max_length=5)
    Shayam_Nagar = models.CharField(max_length=5)
    Ram_Nagar = models.CharField(max_length=5)
    Civil_Lines = models.CharField(max_length=5)
    Jaipur_Metro_Station = models.CharField(max_length=5)
    Sindhi_Camp = models.CharField(max_length=5)
    Chandpole = models.CharField(max_length=5)
    Chhoti_Chaupar = models.CharField(max_length=5)
    Badi_Chaupar = models.CharField(max_length=5)

    def __str__(self):
        return self.station_name
    
class Nagpur_fare(models.Model):
    station_name = models.CharField(max_length=30)
    khp = models.CharField(max_length=5)
    nap = models.CharField(max_length=5)
    sap = models.CharField(max_length=5)
    aip = models.CharField(max_length=5)
    ujn = models.CharField(max_length=5)
    jpn = models.CharField(max_length=5)
    cps = models.CharField(max_length=5)
    ajs = models.CharField(max_length=5)
    rhc = models.CharField(max_length=5)
    cgn = models.CharField(max_length=5)
    stb = models.CharField(max_length=5)
    zm = models.CharField(max_length=5)
    kcp = models.CharField(max_length=5)
    gdg = models.CharField(max_length=5)
    kdc = models.CharField(max_length=5)
    nrr = models.CharField(max_length=5)
    aus = models.CharField(max_length=5)
    lmn = models.CharField(max_length=5)
    ban = models.CharField(max_length=5)
    vdn = models.CharField(max_length=5)
    rrr = models.CharField(max_length=5)
    sbn = models.CharField(max_length=5)
    dpc = models.CharField(max_length=5)
    lds = models.CharField(max_length=5)
    sns = models.CharField(max_length=5)
    ioe = models.CharField(max_length=5)
    jrs = models.CharField(max_length=5)
    nps = models.CharField(max_length=5)
    dvs = models.CharField(max_length=5)
    ags = models.CharField(max_length=5)
    cts = models.CharField(max_length=5)
    tpe = models.CharField(max_length=5)
    abs = models.CharField(max_length=5)
    vns = models.CharField(max_length=5)
    pjn = models.CharField(max_length=5)

    def __str__(self):
        return self.station_name    
