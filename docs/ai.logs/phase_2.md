log:
bu kodda sadece  Structural tür en az 2 örüntü kullanmanı istiyorum hangilerini önerirsin.
1. Facade (Cephe)
Neden? Sepet, Indirim ve Veritabani sınıfları şu an birbirinden bağımsız ve dışarıdan ayrı ayrı yönetilmek zorunda. Facade, bu üç sınıfı tek bir basit arayüz arkasına gizler.
2.  Composite (Bileşik)
Neden? Şu an Indirim sınıfı tek bir indirim tipi uyguluyor. Birden fazla indirimi aynı anda uygulamak gerektiğinde (YAZ_INDIRIMI + VIP_MUSTERI gibi) kod çalışmıyor. Composite, indirimleri ağaç yapısında birleştirmenizi sağlar.

Fark:
Ben burda composite yerine decorater kullandım çünkü:
Mevcut sistem katmanlı bir hiyerarşi (Composite) yapısına sahip değildir, çünkü nesneler arasında parça-bütün ilişkisi olan bir ağaç yapısı bulunmamaktadır. Bu yüzden veri tek bir yapı içinde tutulup sırayla işlendiği için pipeline yaklaşımı benimsenmiş ve bu akışa daha uygun olan Decorator ve benzeri davranış genişletme yapıları tercih edilmiştir.
