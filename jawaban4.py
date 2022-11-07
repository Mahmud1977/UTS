#soal no. 4

print("Nama : MAHMUD S LAOPO")
print("Nim  : 20210801203")

print("pilihan")
print("1. capucino")
print("2. teh")
print("3. exit")

pilihan = input ("masukkan pilihan : ")
if(int(pilihan) == 1):
    print(str("CAPUCINO"))
elif(int(pilihan) == 2):
    print(str("TEH"))
elif(int(pilihan) == 3):
    exit()
harga = input ("masukkan harga\t : ")

hasil = (int(harga) * 10 / 100) + int(harga)

print(str(hasil))