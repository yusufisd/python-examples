import random
class Muzikcalar():
    def __init__(self,sarkilar=[]):
        self.sarkilar=sarkilar
        self.suan_calan=""
        self.ses=50
        self.durum = True

    def menu(self):
        print("""
        
        Müzik Çalar Programına Hoşgeldiniz!

        Şarkı listesi:{}
        Şu an çalan şarkı:{}
        Ses düzeyi:{}

        1.Şarkı Ekle
        2.Ses Arttır
        3.Ses Azalt
        4.Rastgele Şarkı Aç
        5.Şarkı Seç
        6.Şarkı Sil
        7.Çıkış
        """.format(self.sarkilar,self.suan_calan,self.ses))

    def calistir(self):
        self.menu()
        secim=int(input("Lütfen işlem seçiniz: "))
        if secim<=0 or secim>=8:
                secim=int(input("1-7 arası seçim yapınız: "))

        if secim==1:
            sanatci=input("Sanatçı: ")
            sarki=input("Şarkı ismi: ")
            self.sarkilar.append(sanatci+"-"+sarki)
            
        if secim==2:
            if self.ses==100:
                print("Ses maksimum seviyede")
            kac=int(input("Ses kaç artırılsın:"))
            self.ses=self.ses+kac
            if self.ses<0:
                self.ses=0



        if secim==3:
            if self.ses==0:
                print("Ses minimum seviyede")
            kac=int(input("Ses kaç azaltılsın:"))
            self.ses=self.ses-kac
            if self.ses<0:
                self.ses=0

        if secim==4:
            if not self.sarkilar:
                print("Şarkı listesi boş.")
            else:
                rastgele=random.sample(self.sarkilar,1)
                self.suan_calan=rastgele
            
        if secim==5:
            if not self.sarkilar:
                print("\nŞarkı listesi boş.")
            else:    
                a=1
                for sarki in self.sarkilar:
                    print("{}){}\n".format(a,sarki))
                    a+=1
                secilen=int(input("Seçmek istedğiniz şarkı numarasını girin: "))
                self.suan_calan=self.sarkilar[secilen-1]
        if secim==6:
            id=1
            if not self.sarkilar:
                print("\nŞarkı listesi boş.")
            else:    
                for sarki in self.sarkilar:
                    print("{}){}".format(id,sarki))
                    id+=1
                silinen=int(input("Silmek istediğiniz şarkı numarası: "))
                while silinen<1 or silinen >len(self.sarkilar):
                    silinen=int(input("Silmek istediğiniz şarkının numarasını doğru girin: "))
                self.sarkilar.pop(silinen-1)        

        if secim==7:
            self.cikis()          
    def cikis(self):
        self.durum=False
        print("\nBaşarıyla çıkış yapıldı.\n")

muzikcalar=Muzikcalar()
while muzikcalar.durum:
    muzikcalar.calistir()
