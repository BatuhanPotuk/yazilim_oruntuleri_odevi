from abc import ABC


class IndirimInterface(ABC):
    def hesapla(self, toplam_fiyat): pass

class Indirim(IndirimInterface):
    def hesapla(self, toplam_fiyat):
        toplam_fiyat = self._on_islem(toplam_fiyat)
        toplam_fiyat = toplam_fiyat * self._oran()
        toplam_fiyat = self._son_islem(toplam_fiyat)
        return toplam_fiyat

    def _on_islem(self, toplam):
        return toplam

    def _oran(self):
        pass

    def _son_islem(self, toplam):
        return toplam


class YazIndirim(Indirim):
    def _oran(self):
        return 0.8


class VipMusteri(Indirim):
    def _oran(self):
        return 0.5


class Personel(Indirim):
    def __init__(self, personel_id):
        if not personel_id:
            raise ValueError(f"{personel_id} ID bulunamadı.")
        self.personel_id = personel_id

    def _oran(self):
        return 0.6 if self.personel_id < 50 else 0.7


class KDV(Indirim):
    KDV_ORANI = 1.18

    def __init__(self, hesaplayici):
        self.hesaplayici = hesaplayici

    def _oran(self):
        return self.KDV_ORANI

    def _on_islem(self, toplam):
        return self.hesaplayici.hesapla(toplam)


class IndirimFactory:
    _kayitli_indirimler = {
        "YAZ": YazIndirim,
        "VIP": VipMusteri,
        "PERSONEL": Personel,
    }

    def olustur(indirim_tipi, personel_id=None):
        sinif = IndirimFactory._kayitli_indirimler.get(indirim_tipi)
        if sinif is None:
            raise ValueError(f"Bilinmeyen indirim tipi: {indirim_tipi}")
        if indirim_tipi == "PERSONEL":
            return sinif(personel_id)
        return sinif()


class IndirimHalkasi(ABC):
    def __init__(self):
        self._sonraki = None

    def sonraki(self, halka):
        self._sonraki = halka
        return halka

    def isle(self, toplam):
        toplam = self._uygula(toplam)
        if self._sonraki:
            toplam = self._sonraki.isle(toplam)
        return toplam

    def _uygula(self, toplam):
        pass


class IndirimUygulayici(IndirimHalkasi):
    def __init__(self, indirim):
        super().__init__()
        self.indirim = indirim

    def _uygula(self, toplam):
        return self.indirim.hesapla(toplam)


class KDVUygulayici(IndirimHalkasi):
    KDV_ORANI = 1.18

    def _uygula(self, toplam):
        return toplam * self.KDV_ORANI


class VeriTabaniServisi:
    def kaydet(self, sepet_id, toplam):
        print(f"[DB] Sepet {sepet_id} → {toplam:.2f} TL kaydedildi.")


class Urun:
    def __init__(self, ad, fiyat):
        self.ad = ad
        self.fiyat = fiyat


class Sepet:
    def __init__(self, urunler, db_servisi):
        self.urunler = urunler
        self.db_servisi = db_servisi

    def _ham_toplam(self):
        return sum(u.fiyat for u in self.urunler)

    def toplam_hesapla(self, indirim_tipi, personel_id=None, kdv=False):
        indirim = IndirimFactory.olustur(indirim_tipi, personel_id)
        baslangic = IndirimUygulayici(indirim)
        if kdv:
            baslangic.sonraki(KDVUygulayici())
        return baslangic.isle(self._ham_toplam())

    def kaydet(self, sepet_id, toplam):
        self.db_servisi.kaydet(sepet_id, toplam)