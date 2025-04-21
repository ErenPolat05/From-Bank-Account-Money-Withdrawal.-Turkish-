
#From bank account,money withdrawal application turkish.


ErenHesap = {
    "Adi": "Eren Polat",
    "HesapNo":"19051905",
    "Bakiye":5000,
    "EkHesap":2500
}

HamzaHesap = {
    "Adi":"Hamza Ali Polat",
    "HesapNo":"19071907",
    "Bakiye":6000,
    "EkHesap":3000
}

def paracek(hesap,miktar):
    print(f"Merhaba {hesap["Adi"]}")

    if (hesap["Bakiye"]>=miktar):
        hesap["Bakiye"] -= miktar
        print(f"{miktar} TL tutarindaki bakiyeniz basariyla cekilmistir.")
    else:
        toplam = hesap["Bakiye"] + hesap["EkHesap"]
       
        if toplam >= miktar :
            soru = input("Ek Hesap Kullanilsin mi e(evet)/h(hayir): ")
            if soru == "e":

             ekhesaptanallinacakpara = miktar - hesap["Bakiye"]
             hesap["Bakiye"] = 0
             hesap["EkHesap"] -= ekhesaptanallinacakpara

             print(f"{hesap["HesapNo"]} no'lu hesabinizdan para cekimi gerceklestirilmistir.")
            elif soru == "h":
                print(f"{hesap["HesapNo"]} no'lu hesabinizin bakiyesi {hesap["Bakiye"]} TL'dir. Yetersiz Bakiyedir.")
        else:
            print(f"{hesap["HesapNo"]} no'lu hesabinizdaki toplam para yetersizdir.")        

def bakiyesorgulama(hesap):
    print(f"{hesap["HesapNo"]} no'lu hesabinizda kalan bakiye {hesap["Bakiye"]} TL ve EkHesapta Kalan Paraniz ise {hesap["EkHesap"]} TL'dir.")


print("*********")
paracek(ErenHesap,3000)
bakiyesorgulama(ErenHesap)
print("*********")
paracek(ErenHesap,2600)
bakiyesorgulama(ErenHesap)
print("*********")
