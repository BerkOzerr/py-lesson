import numpy as np
###################################################### önemli axis = 0 sütun bazında işlem axis =1 satır bazında
notlar = np.array([
    [70, 85, 90, 60, 75],
    [80, 95, 70, 85, 90],
    [60, 75, 80, 70, 65],
    [90, 85, 95, 100, 80]
])


print(np.ndim(notlar))
print(np.shape(notlar))
print(np.size(notlar))
print(notlar.dtype)
print(notlar[0,2])
print(notlar[2,4])
print(notlar[3,:])
print(notlar[:,1])
print(notlar[:2,:3])
# print("stu1 ->",np.mean( notlar[:1],axis=(0,1) )) 
# print("stu2 ->",np.mean( notlar[1,:],axis=0))
# print("stu3 ->",np.mean( notlar[2,:],axis=0))
# print("stu4 ->",np.mean( notlar[3,:],axis=0))
print("stu ortalamalari ->",  np.mean(notlar,axis=1))
print("-"*np.size(notlar))
# print("ex1 ->",np.mean(notlar[:,:1],axis=0))
# print("ex2 ->",np.mean(notlar[:,1],axis=0))
# print("ex3 ->",np.mean(notlar[:,2],axis=0))
# print("ex4 ->",np.mean(notlar[:,3],axis=0))
# print("ex5 ->",np.mean(notlar[:,4],axis=0))
print("ex ortalamari ->",  np.mean(notlar,axis=0))

print(np.max(notlar))
print(np.min(notlar))
# print("stu1 ->",np.max( notlar[:1]) ,np.min( notlar[:1]) ,notlar[:1]) 
# print("stu2 ->",np.max( notlar[1,:]) ,np.min( notlar[1,:]) ,notlar[1,:]) 
# print("stu3 ->",np.max( notlar[2,:]) ,np.min( notlar[2,:]) ,notlar[2,:]) 
# print("stu4 ->",np.max( notlar[3,:]) ,np.min( notlar[3,:]) ,notlar[3,:]) 
print("stu -> max", np.max(notlar ,axis=1),"stu -> min ", np.min(notlar, axis=1))
print("ex -> max", np.max(notlar ,axis=0),"ex -> min ", np.min(notlar, axis=0))


print(notlar[notlar>60])
print(notlar[notlar>=90])
tempnot =np.where(notlar>=60,1,0)
print(tempnot)


notlar = notlar+5
tmp = np.where(notlar >100 , 100 , notlar) ###### tmp = np.minimum(notlar + 5, 100)
print(tmp)

katsayi = np.array([
    [1],
    [2],
    [1],
    [2]
])
print(np.shape(notlar)," <- notlar", "katsayi ->",np.shape(katsayi))
print(notlar*katsayi)# çalışır 4 satırlar uyuyor sütünları kendi için de çarpar

a = np.arange(1, 21)
sayilar = np.array(a).reshape(4,5)
print(sayilar.T)
print(sayilar)
# print(np.sum(sayilar[:1,:]),sayilar[:1,:])
# print(np.sum(sayilar[1,:]),sayilar[1,:])
# print(np.sum(sayilar[2,:]),sayilar[2,:])
# print(np.sum(sayilar[3,:]),sayilar[3,:])
print("sayilar - satirlarinin toplami ->",np.sum(sayilar, axis=1))

# print(np.sum(sayilar[:,:1]),sayilar[:,:1])
# print(np.sum(sayilar[:,1]),sayilar[:,1])
# print(np.sum(sayilar[:,2]),sayilar[:,2])
# print(np.sum(sayilar[:,3]),sayilar[:,3])
# print(np.sum(sayilar[:,4]),sayilar[:,4])
print("sayilar - sütünlarinin toplami ->", np.sum(sayilar, axis=0))


print(sayilar[sayilar >10])
print(sayilar[sayilar<15])
print(sayilar[(sayilar >10) & (sayilar <15)])
 