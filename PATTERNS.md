#faz_1

class YazIndirimi:
    def uygula(self, toplam):
        return toplam * 0.8

class VipMusteri:
    def uygula(self, toplam):
        return toplam * 0.5

class PersonelIndirimi:
    def uygula(self, toplam, personel_id=None):
        if personel_id is None:
            raise ValueError("Personel indirimi için personel_id zorunludur!")
        return toplam * 0.7


class Indirim:
    _kayitli_indirimler = {
        "YAZ_INDIRIMI": YazIndirimi,
        "VIP_MUSTERI": VipMusteri,
        "PERSONEL": PersonelIndirimi,
    }

    @staticmethod
    def olustur(indirim_tipi: str, personel_id=None):
        sinif = Indirim._kayitli_indirimler.get(indirim_tipi)

        if sinif is None:
            raise ValueError(f"Bilinmeyen indirim tipi: {indirim_tipi}")

        if indirim_tipi == "PERSONEL":
            return sinif(personel_id)

        return sinif()

class Sepet:
    KDV_ORANI = 1.18

    def __init__(self, urunler):
        self.urunler = urunler

    def toplam_hesapla(self, indirim_tipi, personel_id=None, kdv=False):
        toplam = sum(urun.fiyat for urun in self.urunler)

        indirim = Indirim.olustur(indirim_tipi)

        if isinstance(indirim, PersonelIndirimi):
            toplam = indirim.uygula(toplam, personel_id)
        else:
            toplam = indirim.uygula(toplam)

        return toplam * self.KDV_ORANI if kdv else toplam

    def veritabanina_kaydet(self):
        print("Veritabanına bağlanılıyor ve kaydediliyor...")

#review:
Bu kod yapısı, SOLID prensiplerinden özellikle Single Responsibility (SRP) ve Open/Closed (OCP) ilkelerini ihlal etmektedir; çünkü Sepet sınıfı hem hesaplama hem veritabanı işlemlerini üstlenmiş, Indirim.olustur metodu ise yeni indirim tipleri eklendikçe sürekli değiştirilmeye mahkum bırakılmıştır. Ayrıca, olustur metodundaki parametre yönetimi ile toplam_hesapla içindeki isinstance kontrolü, nesne yönelimli tasarımın sağladığı esnekliği kısıtlayan ve hata payını artıran "sıkı bağımlılıklar" oluşturmaktadır.