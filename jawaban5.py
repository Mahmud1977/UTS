
# Soal No. 5

class waktu:
    def __init__(self, jam, menit, detik):
        self.jam = jam
        self.menit = menit
        self.detik = detik

    def validasiJam(self):
        vJam = self.jam
        if(int(vJam) > 24):    
            print("Jam salah!!!")

    def validasiMenit(self):
        vMenit = self.menit
        if(int(vMenit) > 60):
            print("Menit salah!!!")
    
    def validasiDetik(self):
        vJam = self.jam
        vMenit = self.menit
        vDetik = self.detik
        if(int(vDetik) > 60):
            print("Detik salah!!!")
        elif(int(vDetik) < 60):
             print(str(vJam) + " : " + str(vMenit) + " : " + str(vDetik))

jam = int(input ("Masukkan jam: ")) 
menit = int(input ("Masukkan menit: "))
detik = int(input ("Masukkan detik: "))

vWaktu = waktu(jam, menit, detik)
vWaktu.validasiJam()
vWaktu.validasiMenit()
vWaktu.validasiDetik()


        



