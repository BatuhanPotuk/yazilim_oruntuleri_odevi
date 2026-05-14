log:
ben senden bir veya daha creational patterns kullanmanı istiyecem ama farklı bir tür pattern kullanma ve nasıl bir yol gideceğime dair bir yol göster bu kod için.

🏭 Factory Method
👉 “Nesne oluşturmayı merkezileştirir, hangi sınıfın üretileceğini dışarıdan gizler”

Nesne oluşturma işlemi tek bir noktada toplanır ve istemci (Sepet gibi sınıflar) hangi sınıfın üretileceğini bilmek zorunda kalmaz.
Yeni bir tür eklemek için mevcut kodu değiştirmek yerine sadece factory yapısına yeni bir kayıt eklemek yeterlidir, böylece sistem daha esnek hale gelir.

Yeni bir indirim türü eklendiğinde nesne oluşturma işlemlerinin sistemin farklı yerlerinde değiştirilmesini önlemek amacıyla Factory Pattern kullanılmıştır. Böylece nesne oluşturma süreci tek bir merkezde toplanmış, kodun bakım ve genişletilebilirliği artırılmıştır. Bu sayede mevcut kodda yapılacak değişiklik ihtiyacı ve hata riski azaltılmıştır.