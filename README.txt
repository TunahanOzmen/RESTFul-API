Tunahan Özmen - 171301071

Kurulum ve Çalıştırma:
1- <main.py>, <Handler.py>, <POST_funcs.py>, <GET_funcs.py> dosyaları aynı klasörde bulunmalıdır.
2- Konsolda veya derleyicide "klasör konumu>python main.py"  komutu çalıştırılır.
3- Server, kullanıcı istekleri için dinlemeye geçmiş olur.

Kullanım Kılavuzu:

Oluşturulan API, f1 verilerini "Formula One API" isimli API'den çekmektedir ve bunları işleyerek görselleştirmektedir.
5 Farklı GET isteği ile farklı istatistikler görselleştirilmektedir ve görsel konumu json olarak kullanıcıya iletilmektedir.
1 POST isteği ile diğer istekler ile  oluşturulacak olan görsellerin uzantısı, ismi ve dosya konumu değiştirilmektedir.
Bu isteklerin kullanımları aşağıda paylaşılmıştır. En aşağıda belirli pilotların id'leri verilmiştir.

GET istekleri:
1-pitstopTimes:         seçilen yıl ve yarış için, istenen pilotların yarış boyunca pitstopta geçirdikleri süreler karşılaştırmalı
olarak görsellenmektedir. Örnek kullanımlar:
-pitstopTimes fonksiyonu çalışacaktır, 2018 yılının 3.yarışı için {vettel, alonso} id'li pilotların karşılaştırması görselleştirilecektir.
 http://localhost:6699/?func=pitstopTimes&year=2018&round=3&pilots=vettel%alonso

-pitstopTimes fonksiyonu çalışacaktır, 2020 yılının 7.yarışı için {hamilton, max_verstappen, norris} id'li pilotların karşılaştırması görselleştirilecektir.
 http://localhost:6699/?func=pitstopTimes&year=2020&round=7&pilots=hamilton%max_verstappen%norris


2-lapTimes:             seçilen yıl ve yarış ve tur için, istenen pilotların o turu tamamlama süreleri karşılaştırılacaktır.
Örnek kullanımlar:
-lapTimes fonksiyonu çalışacaktır, 2015 yılının 12.yarışının 38.turunu {vettel, rosberg, alonso, hamilton} id'li pilotlarinin tamamlama süreleri
görselleştirilecektir.
 http://localhost:5599/?func=lapTimes&year=2018&round=12&pilots=vettel%rosberg%alonso%hamilton&lapNumber=38


3-sessionEnd:           seçilen yıl ve yarış ve tur için, yarışı ilk üç bitiren pilotlar gösterilir.
Örnek kullanımlar:
-sessionEnd fonksiyonu çalışacaktır, 2018 yılının 3.yarışında podyuma çıkan pilotlar görselleştirilecektir.
 http://localhost:5599/?func=sessionEnd&year=2018&round=3


4-pilotStandings:       seçilen yıl ve yarıştan sonra ilk {limit} sıradaki pilotlarin puan durumlarını gorsellestir
Örnek kullanımlar:
-pilotStandings fonksiyonu çalışacaktır, 2012 yılının 9.yarışından sonra oluşan liderlik tablosunda ilk 5 pilotun puanlarının
karşılaştırması görselleştirilecektir.
 http://localhost:5599/?func=pilotStandings&year=2012&round=9&limit=5


5-constructorStandings: seçilen yıl ve yarıştan sonra ilk {limit} sıradaki takimlarin puan durumlarını gorsellestir
Örnek kullanımlar:
-constructorStandings fonksiyonu çalışacaktır, 1998 yılının 3.yarışından sonra oluşan liderlik tablosunda ilk 3 takımın puanlarının
karşılaştırması görselleştirilecektir.
 http://localhost:5599/?func=constructorStandings&year=1998&round=3&limit=3



POST istekleri:
1-changeSettings:       Görselleştirmeler için kullanıcıdan dosya konumu(kayıt için), oluşturulacak görsel için isim ve format istenir
ve bunlar kullanıma alınır.
Örnek kullanımlar:
-changeSettings fonksiyonu çalışacaktır. Kayıtlar için yeni konum olarak : C:\Users\Public\Pictures,
                                                            isim olarak  : myDataViz,
                                                            format olarak: jpg                       kullanıma alınır.
 http://localhost:5599?func=changeSettings&newPath=C:\Users\Public\Pictures&imgName=myDataViz&imgType=jpg



Sorgular için bazı pilot id'leri aşağıda verilmiştir, isteklerde bu pilotlarin yarıştıkları yıllar için sorgu yapılmalıdır:
"vettel"
"hamilton"
"bottas"
"ricciardo"
"raikkonen"
"alonso"
"max_verstappen"
"gasly"
"sainz"
"ocon"
"perez"
"leclerc"
"stroll"