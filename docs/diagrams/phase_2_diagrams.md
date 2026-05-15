classDiagram

class IndirimInterface {
    +hesapla(toplam_fiyat)
}

class YazIndirim {
    +hesapla(toplam_fiyat)
}

class VipMusteri {
    +hesapla(toplam_fiyat)
}

class Personel {
    +hesapla(toplam_fiyat)
}

class KDV {
    +hesapla(toplam_fiyat)
}

class IndirimFactory {
    +olustur()
}

class IndirimFacade {
    +hesapla()
}

class VeriTabaniServisi {
    +kaydet()
}

class Sepet {
    +toplam_hesapla()
    +kaydet()
}

IndirimInterface <|.. YazIndirim
IndirimInterface <|.. VipMusteri
IndirimInterface <|.. Personel
IndirimInterface <|.. KDV

KDV --> IndirimInterface : decorates

IndirimFactory ..> YazIndirim
IndirimFactory ..> VipMusteri
IndirimFactory ..> Personel

IndirimFacade ..> IndirimFactory
IndirimFacade ..> KDV

Sepet ..> IndirimFacade
Sepet ..> VeriTabaniServisi
```