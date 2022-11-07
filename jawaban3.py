
# break adalah perintah khusus yang dipakai untuk memaksa sebuah perulangan 
# berhenti sebelum waktunya


for val in "bahasa" :
    if val == "h":
        break
    print (val)
print()

# Dengan pernyataan continue kita dapat menghentikan iterasi saat ini, dan melanjutkan 
# dengan yang berikutnya:

for val in "bahasa" :
    if val == "h":
        continue
    print (val)
print()