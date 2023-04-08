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