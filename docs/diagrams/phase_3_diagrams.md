classDiagram

class IndirimInterface {
    +hesapla(toplam_fiyat)
}

class Indirim {
    +hesapla()
    +_on_islem()
    +_oran()
    +_son_islem()
}

class YazIndirim
class VipMusteri
class Personel
class KDV

class IndirimFactory {
    +olustur()
}

class IndirimHalkasi {
    +sonraki()
    +isle()
}

class IndirimUygulayici {
    +_uygula()
}

class KDVUygulayici {
    +_uygula()
}

class Sepet {
    +toplam_hesapla()
}

IndirimInterface <|-- Indirim

Indirim <|-- YazIndirim
Indirim <|-- VipMusteri
Indirim <|-- Personel
Indirim <|-- KDV

IndirimFactory ..> YazIndirim
IndirimFactory ..> VipMusteri
IndirimFactory ..> Personel

IndirimHalkasi <|-- IndirimUygulayici
IndirimHalkasi <|-- KDVUygulayici

IndirimUygulayici --> Indirim

Sepet ..> IndirimFactory
Sepet ..> IndirimHalkasi
```