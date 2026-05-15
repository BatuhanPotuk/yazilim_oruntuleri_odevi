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