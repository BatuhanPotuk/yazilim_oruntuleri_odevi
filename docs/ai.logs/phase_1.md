log:
ben senden bir veya daha creational patterns kullanmanı istiyecem ama farklı bir tür pattern kullanma ve nasıl bir yol gideceğime dair bir yol göster bu kod için.

🏭 Factory Method
👉 “Nesne oluşturmayı merkezileştirir, hangi sınıfın üretileceğini dışarıdan gizler”

Nesne oluşturma işlemi tek bir noktada toplanır ve istemci (Sepet gibi sınıflar) hangi sınıfın üretileceğini bilmek zorunda kalmaz.
Yeni bir tür eklemek için mevcut kodu değiştirmek yerine sadece factory yapısına yeni bir kayıt eklemek yeterlidir, böylece sistem daha esnek hale gelir.

Sadece factory kullandım çünküYeni bir indirim türü eklendiğinde if/else zincirleri nedeniyle sistemin birçok yerini değiştirmek zorunda kalmamak için Factory kullanıldı. Böylece nesne oluşturma tek bir merkezde toplandı ve hem kodun değiştirilme ihtiyacı azaltıldı hem de bakım maliyeti ve hata riski minimuma indirildi.