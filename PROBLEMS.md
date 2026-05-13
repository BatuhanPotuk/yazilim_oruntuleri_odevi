SRP:
Kodda sepet classı hem ürünleri tutyor hemde indirimleri hesablıyor bu yüzden bu kuralı ihlala ediyoruz.

Encapsulation:
Burda her indirim türünü ayrı yarı claas kurup o classlar kurmak yerine sepet classı içinde yaptığımız için ihlal ediyoz.

DIP:
Burda herhangi bir soyut nesneye değilde özelliklere bağlı olduğu için.

OCP:
Burda if else zincirine bağlı olduğundan gelecekte yeni bir indirim türü tanımlarken yada başka bir şeyi değiştirmek tümden kodu etkileyeceğinden ihlal ediyoruz.

Liskow:
Burda ana classtaki bilgiler  id yokken personalde id istiyo ve bu neden bu kuralıda ihlal ediyoruz.


AI:
1) SRP (Single Responsibility Principle) ihlali

Sepet sınıfı birden fazla işi aynı anda yapıyor:

Ürünlerin toplamını hesaplıyor
İndirim mantığını içeriyor
Veritabanına kaydetme işlemi yapıyor

Sorun: Bir sınıfın hem iş mantığı hem de veri erişimi hem de indirim kurallarıyla ilgilenmesi onu çok kırılgan ve değiştirilmesi zor hale getirir.

Çözüm tasarım örüntüleri:

Repository Pattern → veritabanı işlemleri için ayrı bir sınıf
Strategy Pattern → indirim hesaplama için ayrı stratejiler
2) OCP (Open/Closed Principle) ihlali
if indirim_tipi == "YAZ_INDIRIMI":
elif indirim_tipi == "VIP_MUSTERI":
elif indirim_tipi == "PERSONEL":

Sorun: Yeni bir indirim eklemek istediğinde Sepet sınıfını sürekli değiştirmek zorundasın. Bu, sistemi büyüdükçe riskli hale getirir.

Çözüm tasarım örüntüsü:

Strategy Pattern
Her indirim türü ayrı bir sınıf olur
Sepet sadece “indirim uygula” der, detay bilmez
3) DIP (Dependency Inversion Principle) ihlali

Şu an Sepet:

İndirim mantığını string’lere bağlı şekilde kendisi belirliyor
Veritabanı işlemini doğrudan kendi içinde yapıyor

Sorun: Üst seviye sınıf (Sepet), detaylara (indirim string’leri, DB işlemi) doğrudan bağımlı.

Çözüm tasarım örüntüleri:

Dependency Injection
Strategy Pattern (indirim için soyutlama)
Repository Pattern (DB bağımlılığını soyutlamak için)
4) Tight Coupling (sıkı bağımlılık)
İndirim mantığı Sepet içine gömülmüş
DB işlemi yine Sepet içinde

Sorun: Sistemin bir parçasını değiştirmek (örneğin DB değiştirmek veya yeni indirim eklemek) diğer parçaları da etkiler.

Çözüm:

Repository Pattern
Strategy Pattern
Facade Pattern (istersen sepeti sadeleştirmek için)
5) Kodun genişlemeye kapalı, değişikliğe açık olması

Yeni bir indirim eklemek = elif zincirine yeni satır eklemek.

Sorun: Kod büyüdükçe karmaşıklık lineer değil, kaotik şekilde artar.

Çözüm:

Strategy Pattern (en kritik çözüm burada)