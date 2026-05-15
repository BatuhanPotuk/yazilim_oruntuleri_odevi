IndirimInterface  (ABC)
       │
       ├── Indirim  (Template Method)
       │       ├── YazIndirim
       │       ├── VipMusteri
       │       ├── Personel
       │       └── KDV  ◄─── Decorator
       │
       └── (doğrudan implement)
               ├── YazIndirim
               ├── VipMusteri
               ├── Personel
               └── KDV


IndirimFactory
       └── olustur(indirim_tipi, personel_id)
               ├── "YAZ"      → YazIndirim()
               ├── "VIP"      → VipMusteri()
               └── "PERSONEL" → Personel(personel_id)


IndirimFacade
       └── hesapla(toplam_fiyat, indirim_tipi, personel_id, kdv)
               ├── IndirimFactory.olustur(...)   ← Factory
               └── KDV(indirim)                  ← Decorator


Sepet
       ├── _ham_toplam()
       ├── toplam_hesapla()  →  IndirimFacade   ← Facade
       └── kaydet()          →  VeriTabaniServisi


IndirimHalkasi  (ABC)  ← Chain of Responsibility
       ├── IndirimUygulayici  →  indirim.hesapla()
       └── KDVUygulayici      →  toplam * 1.18


FACADE:
# Yaz indirimi
toplam = sepet.toplam_hesapla("YAZ")

# VIP + KDV
toplam = sepet.toplam_hesapla("VIP", kdv=True)

# Personel (ID < 50 → %40, ID >= 50 → %30 indirim)
toplam = sepet.toplam_hesapla("PERSONEL", personel_id=42)
toplam = sepet.toplam_hesapla("PERSONEL", personel_id=42, kdv=True)

sepet.kaydet("SP-001", toplam)

CHAIN:
indirim   = IndirimFactory.olustur("VIP")
baslangic = IndirimUygulayici(indirim)
baslangic.sonraki(KDVUygulayici())

toplam = baslangic.isle(30500)  # 30500 * 0.5 * 1.18 = 18,005 TL

FACTORY:
yaz      = IndirimFactory.olustur("YAZ")
vip      = IndirimFactory.olustur("VIP")
personel = IndirimFactory.olustur("PERSONEL", personel_id=10)

print(yaz.hesapla(1000))       # 800.0
print(vip.hesapla(1000))       # 500.0
print(personel.hesapla(1000))  # 600.0

DECORATER:
indirim     = VipMusteri()
indirim_kdv = KDV(indirim)

print(indirim_kdv.hesapla(1000))  # 1000 * 0.5 * 1.18 = 590.0

TEMPLATES:
class Indirim(IndirimInterface):
    def hesapla(self, toplam_fiyat):
        toplam_fiyat = self._on_islem(toplam_fiyat)
        toplam_fiyat = toplam_fiyat * self._oran()
        toplam_fiyat = self._son_islem(toplam_fiyat)
        return toplam_fiyat


