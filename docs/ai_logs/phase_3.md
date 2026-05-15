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

# Faz 3 : Behavioral Örüntüler

## Uygulanan Örüntü
Template Method

## Nerede Uygulandı?
"Indirim" sınıfında ve onun alt sınıflarında (YazIndirim, VipMusteri, Personel, KDV).

## Neden Uygulandı?
Tüm indirim türlerinde işlem sırası aynıydı ancak uygulanan oran değişiyordu. Ortak algoritmayı merkezi hale getirip sadece değişen kısmı alt sınıflara bırakmak için Template Method uygulandı.

## OCP'ye Uygun mu ve Bu Örüntü Ne Kazandırdı?
OCP’ye uygundur çünkü yeni bir indirim türü eklemek için mevcut algoritmayı değiştirmek yerine yeni bir alt sınıf oluşturmak yeterlidir.

Kazandırdıkları:
- Kod tekrarını azalttı.
- Ortak işlem akışı merkezi hale geldi.
- Yeni indirim türleri daha kolay eklenebilir oldu.

---

## Uygulanan Örüntü
Chain of Responsibility

## Nerede Uygulandı?
"IndirimHalkasi", "IndirimUygulayici" ve "KDVUygulayici" sınıflarında.

## Neden Uygulandı?
İndirim ve KDV gibi işlemleri sırayla zincir şeklinde uygulamak ve işlem sırasını daha esnek hale getirmek için uygulandı.

## OCP'ye Uygun mu ve Bu Örüntü Ne Kazandırdı?
OCP’ye uygundur çünkü yeni bir işlem eklemek için mevcut sistemi değiştirmeden yeni bir halka eklemek yeterlidir.

Kazandırdıkları:
- İşlem sırası esnek hale geldi.
- Yeni işlem adımları kolayca eklenebilir oldu.
- Sınıflar arasındaki bağımlılık azaltıldı.
- Sistemin genişletilebilirliği arttı.