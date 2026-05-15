classDiagram

class YazIndirim {
    +hesapla(toplam_fiyat)
}

class VipMusteri {
    +hesapla(toplam_fiyat)
}

class Personel {
    +hesapla(toplam_fiyat)
}

class IndirimFactory {
    +olustur(indirim_tipi)
}

class Sepet {
    +toplam_hesapla()
}

IndirimFactory ..> YazIndirim : creates
IndirimFactory ..> VipMusteri : creates
IndirimFactory ..> Personel : creates

Sepet ..> IndirimFactory
```