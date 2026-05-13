class Sepet:
    def __init__(self, urunler):
        self.urunler = urunler

    def toplam_hesapla(self, indirim_tipi, personel_id=None, kdv=False):
        toplam = 0

        for urun in self.urunler:
            toplam += urun.fiyat

        if indirim_tipi == "YAZ_INDIRIMI":
            toplam *= 0.8

        elif indirim_tipi == "VIP_MUSTERI":
            toplam *= 0.5

        elif indirim_tipi == "PERSONEL":
            if personel_id is not None:
                toplam *= 0.7
            else:
                print("Hata: Personel ID yok!")
        if kdv:
            toplam *= 1.18

        return toplam
    def veritabanina_kaydet(self):
        print("Veritabanına bağlanılıyor ve kaydediliyor...")