log:bu koda  sadece Behavioral  türünde hangi en az iki patterni uygulamayı öneririsin
🔗 1. Chain of Responsibility

👉 “İşlem adım adım zincirden geçer”

Kampanya → VIP → KDV gibi sırayla işler
Her biri fiyatı değiştirip sonraki adıma verir
Yeni kural eklemek = zincire yeni halka eklemek

✔ Amaç: pipeline gibi işlem akışı

👀 2. Observer

👉 “Bir olay olur, herkes haberdar olur”

Sepet satın alındı
Log, stok, bildirim sistemleri otomatik tetiklenir
Sepet kimseyi bilmez, sadece “olay yayınlar”

✔ Amaç: event → otomatik bildirim

↩️ 3. Command

👉 “İşlemi nesneye çevir”

Ürün ekle / sil = komut nesnesi
Her işlem kayıt altına alınır
Undo (geri alma) yapılabilir

✔ Amaç: işlemleri kontrol edilebilir hale getirmek

📋 4. Template Method

👉 “İskelet sabit, detay değişir”

Ödeme akışı sabit: doğrula → işle → bitir
Sadece ödeme yöntemi değişir (kredi kartı / kapıda)
Alt sınıf sadece eksik adımı doldurur

✔ Amaç: ortak algoritmayı sabitlemek
fark:
Observer ve Command kullanmadım çünkü mevcut sistem sadece fiyat hesaplama ve sepet işlemlerini doğrudan çalıştıran basit bir akışa sahip.
Olay bazlı bildirim sistemi  veya işlemleri nesneleştirip geri alma/kuyruklama  gerektiren bir senaryo kodda bulunmuyor.
Bu yüzden koda gereksiz karmaşıklaştırmamk için kullanmadım.

#ocp:
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

#AI :
Tartışmamız genellikle ilk önerdiği kod üstündeki örüntüleri anlama ve kendi yaptığım diğer kullanılabilecek örüntüler o örüntüler yerine hangi örüntü ya da direk  örüntünün bu koda uygun olup olmadığıyla geçti.
Kimi zaman direk işime uygun kimi zaman alakasız örüntüler kullandı.
AI kullamasaydım büyük ihtimal 2 3 günümü alırdı.
AI daha çok sistemi gereksiz karmaşıklaştırcak ve olmayan eylemler için örüntü kullanıyor özellikle bunu bu ve 2. fazda görebiliriz.
Örnek olarak faz 2de composite kullanması composite genelde ağaç tipi çok katmanlı kodlarda kullanılır fakat ben sadece tek katman olduğu için decorater kullandım.
 
