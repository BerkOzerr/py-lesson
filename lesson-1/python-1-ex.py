import sys



sayilar = [1, 2, 3, 4, 5, 6, 7, 8]
yeniSayilar = [
  sayi*2 if i % 2== 0 else sayi
  for i,sayi in enumerate(sayilar)
]
print(yeniSayilar)

kelime = "python"

newKelime=""
for i,val in enumerate(kelime):
  newKelime += val.upper() if i % 2 ==0 else val 

print((newKelime))

sayilar = [2, 4, 6, 8, 10]

sonuc = lambda s:s*3

print(sonuc(5))



sayilar = [1, 2, 3, 4, 5]

sonuc = list(map(lambda sayi:sayi*10 ,sayilar))
print(sonuc)

x = sys.argv[1] if len(sys.argv)==2 else 10
print(x)

liste = ["a", 5, "b", 8, "c", 12, "d", 3]

liste =[
  val.upper() if isinstance(val ,str) else val
    for i, val in enumerate (liste)
]
print(liste)

import random
import string


def generate_id(x):
 if x%2 !=0:
  x+=1
 userid = [
   random.choice(string.ascii_lowercase) if i > (x // 2)-1  else random.choice(string.digits)
  for i in range(x) 
 ]
 random.shuffle(userid)
 return "".join(userid)

# print("gene-1->  "+ generate_id(7))


x=int(sys.argv[1]) if len(sys.argv) >= 2 else 10
z= sys.argv[2] if len(sys.argv) ==3 else None
id = list(generate_id(x))
while any((id[i] in string.digits) == (id[i+1] in string.digits)  for i  in range(len(id)-1)):
  random.shuffle(id)

id= [
### önemli noktası
  val.upper() if z =="upper" else  val.lower()  if   z=="lower"  else val.upper() if z==None and i % 3 ==0 else val  
  for i, val in enumerate(id)
]

print(id)