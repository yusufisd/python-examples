def yeni_not():
    
    isim=input("isim: ")
    soyisim=input("soyisim: ")
    vize=(input("vize: "))
    final=(input("final: "))
    with open("ogr_not.txt","a", encoding="utf-8") as file:
        file.write(isim+" "+soyisim+":"+vize+" "+final+"\n")

def not_ortalama(satir):
    
    liste=satir.split(":")
    ogr_ad=liste[0]
    ogr_not=liste[1].split(" ")
    vize=int(ogr_not[0])
    final=int(ogr_not[1])
    ort=(vize*0.4)+(final*0.6)
    return (ogr_ad+":"+str(ort)+"\n")

def not_goruntule():
    with open("ogr_not.txt","r", encoding="utf-8") as file:
        for satir in file:
            print(not_ortalama(satir))

def not_kayit():
    with open("ogr_not.txt","r",encoding="utf-8") as file:
        oku = file.readlines()
       #for i in file:
        #  liste.append(i)
        with open("ogr_not_ort.txt","a",encoding="utf-8") as file2:
            for i in oku:
                file2.write(not_ortalama(i))
    print("\nKayıt başarılı!")
while True:
    secim=int(input("\n1.Notları görüntüle\n2.Yeni not gir\n3.Notları kayıt et\n4.Çıkış\nİŞLEM: "))

    if secim==1:
        not_goruntule()
    elif secim==2:
        yeni_not()
    elif secim==3:
        not_kayit()
    elif secim==4:
        break
    else:
        print("Doğru işlem girilmedi.")        
