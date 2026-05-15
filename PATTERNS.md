# Faz 1 : Creational Örüntüler

## Uygulanan Örüntü
Factory Method

## Nerede Uygulandı?
"IndirimFactory" sınıfında ve indirim sınıflarında (YazIndirim, VipMusteri, Personel).

## Neden Uygulandı?
Başlangıçta tüm indirim türleri if-else zinciri ile kontrol ediliyordu. Yeni bir indirim türü eklemek mevcut kodu değiştirmeyi zorunlu hale getiriyordu ve bu durum hata riskini artırıyordu. Nesne oluşturma işlemini merkezi hale getirmek için Factory Method uygulandı.

## Bu Örüntü Ne Kazandırdı?
- Yeni indirim türleri daha kolay eklenebilir hale geldi.
- if-else bağımlılığı azaltıldı.
- Nesne oluşturma işlemleri tek merkezde toplandı.
- Kod daha okunabilir ve genişletilebilir hale geldi.

# Faz 2 : Structural Örüntüler

## Uygulanan Örüntü
Decorator

## Nerede Uygulandı?
"KDV" sınıfında.

## Neden Uygulandı?
Mevcut indirim sınıflarını değiştirmeden sisteme KDV özelliğini dinamik olarak eklemek için uygulandı.

## Bu Örüntü Ne Kazandırdı?
- Mevcut kod değiştirilmeden yeni özellik eklenebildi.
- Dinamik özellik genişletmesi sağlandı.
- OCP prensibine daha uygun bir yapı oluştu.

---

## Uygulanan Örüntü
Facade

## Nerede Uygulandı?
"IndirimFacade" sınıfında.

## Neden Uygulandı?
İndirim hesaplama, factory kullanımı ve KDV işlemleri farklı sınıflara dağıldığı için sistem karmaşık hale gelmeye başlamıştı. Bu işlemleri tek bir giriş noktası altında toplamak için Facade uygulandı.

## Bu Örüntü Ne Kazandırdı?
- Karmaşık işlemler sadeleşti.
- Sistemin kullanımı kolaylaştı.
- Alt sistemlerin detayları gizlendi.
- Sepet sınıfının sorumluluğu azaltıldı.