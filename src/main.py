from abc import ABC, abstractmethod

class IndirimInterface(ABC):
    @abstractmethod
    def hesapla(self, toplam_fiyat): pass


class YazIndirim(IndirimInterface):
    def hesapla(self, toplam_fiyat):
        return toplam_fiyat * 0.8


class VipMusteri(IndirimInterface):
    def hesapla(self, toplam_fiyat):
        return toplam_fiyat * 0.5


class Personel(IndirimInterface):
    def __init__(self, personel_id):
        if not personel_id:
            raise ValueError(f"{personel_id} ID bulunamadı.")
        self.personel_id = personel_id

    def hesapla(self, toplam_fiyat):
        return toplam_fiyat * 0.6 if self.personel_id < 50 else toplam_fiyat * 0.7


class KDV(IndirimInterface):
    KDV_ORANI = 1.18

    def __init__(self, hesaplayici):
        self.hesaplayici = hesaplayici

    def hesapla(self, toplam_fiyat):
        return self.hesaplayici.hesapla(toplam_fiyat) * self.KDV_ORANI


class IndirimFactory:
    _kayitli_indirimler = {
        "YAZ": YazIndirim,
        "VIP": VipMusteri,
        "PERSONEL": Personel,
    }

    @staticmethod
    def olustur(indirim_tipi, personel_id=None):
        sinif = IndirimFactory._kayitli_indirimler.get(indirim_tipi)
        if sinif is None:
            raise ValueError(f"Bilinmeyen indirim tipi: {indirim_tipi}")
        if indirim_tipi == "PERSONEL":
            return sinif(personel_id)
        return sinif()


class VeriTabaniServisi:
    @staticmethod
    def kaydet(self, sepet_id, toplam):
        print(f"[DB] Sepet {sepet_id} → {toplam:.2f} TL kaydedildi.")


class IndirimFacade:
    @staticmethod
    def hesapla(self, toplam_fiyat, indirim_tipi, personel_id=None, kdv=False):
        indirim = IndirimFactory.olustur(indirim_tipi, personel_id)
        if kdv:
            indirim = KDV(indirim)
        return indirim.hesapla(toplam_fiyat)


class Urun:
    def __init__(self, ad, fiyat):
        self.ad = ad
        self.fiyat = fiyat


class Sepet:
    def __init__(self, urunler, db_servisi):
        self.urunler = urunler
        self.db_servisi = db_servisi
        self._indirim_facade = IndirimFacade()

    def _ham_toplam(self):
        return sum(u.fiyat for u in self.urunler)

    def toplam_hesapla(self, indirim_tipi, personel_id=None, kdv=False):
        return self._indirim_facade.hesapla(
            self._ham_toplam(),
            indirim_tipi,
            personel_id,
            kdv
        )

    def kaydet(self, sepet_id, toplam):
        self.db_servisi.kaydet(sepet_id, toplam)

