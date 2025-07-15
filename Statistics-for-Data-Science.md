# VERİ BİLİMİ İÇİN İSTATİSTİK

Temelde 2'ye ayrılır:

1. **Descriptive**

   1.1. mean(ortalama)

   1.2. median

   1.3. variance

   1.4. standart sapma

2. **Inferential**

   - veri topla
   - örneklem al
   - deneyler yap
   - bunlara bakarak sonuç çıkar

#### Popülasyon ->Çalışmanın ilgilendiği tüm grup

#### Örneklem(sample) -> popülasyondan seçilmiş daha küçük grup

1.1. Mean (Ortalama)

| Popülasyon | Örneklem (Sample) |
| ---------- | ----------------- |
| µ=∑x/n     | x̅= ∑x/n           |

1.2. Median

Eğer OUTLIER DATA(çıkıntı veri) varsa önemlidir. Yani veride ortalamayı çok yükselten değer varsa önemli hale gelir.

1.3. Mod

En sık tekrarlanan değer

#### _NOT_: MEDYAN, ORTALAMA, MOD measure of central tendency (merkezi eğilim ölçüsü)'dür. Bu hesaplamaların hepsini yaparak veriyi anlamlandırmaya çalışırız, aralarında büyük farklar var mı analiz etmeye ederiz.

1.4. Varyans

### σ² = ∑x(Xi-µ)² / n

1.5. Standart Sapma

### σ

ile gösterilir. Standart sapma arttıkça ortalamadan daha fazla yazılım, sapma olduğunu söyleyebiliriz.

#### _NOT_ : Varyans ve Standart Sapma, Measure of Dispersion (Yayılım Ölçüsü)'dür. Varyans, verilerin ortalamadan ne kadar saptığını ölçer ama karesi olduğundan dolayı yorumlamak zor olabilir. Standart Sapma ise varyansın karekökü olduğu için, verileri orjinal birimine geri döndürerek yorumlamayı kolaylaştırır.

##### Örnek:

| Sınıf | Ortalama (µ) | Varyans (σ²) | Standart Sapma (σ) |
| ----- | ------------ | ------------ | ------------------ |
| A     | 70           | 2.5          | 1.58               |
| B     | 68           | 625          | 25                 |

Bu tabloya bakarak, A sınıfındakilerin notlarının birbirine daha yakın olduğunu ve B'ye göre daha az yayılım olduğunu söyleyebiliriz. B'de ise daha geniş yayılım olmuş, bazı öğrenciler çok iyi bazıları çok kötü olduğu için notlar arasında daha büyük fark var diyebiliriz.

#### POPÜLASYON - SAMPLE FARKI

| Popülasyon Varyansı | Örneklem (Sample) Varyansı |
| ------------------- | -------------------------- |
| σ² = ∑x(Xi-µ)² / n  | S² = ∑x(Xi-µ)² / (n-1)     |

**Neden Sample'da _n-1_ yapıyoruz?**

Popülasyon varyansını daha doğru tahmin etmek için formül düzeltilmiştir. Bir örneklem kullanarak tüm popülasyonu tahmin ettiğimizde oluşan yanlılığı (BIAS) düzeltmek önemlidir. \*n-1 yaparak bias'ı azaltmaya çalışıyoruz.

### VARİABLE (DEĞİŞKENLER)

- **Sayısal Değişkenler**

  - Sürekli Değişkenler ( Continuous Variable)

    Sonsuz değer alabilir. ÖR: Öğrencinin sınav puanı (ondalıklı değerler de alır)

  - Kesikli Değişkenler (Discrete Variable)

    Sayılabilir değerler alır daha çok tam sayı. ÖR: Sınıftaki öğrenci sayısı

* **Kategorik Değişkenler**

  - Nominal

  Sıralama yok. ÖR: (kadın,erkek)

  - Ordinal

  Sıralama var ama aralık yok. ÖR: (çaylak,deneyimli,uzman)

#### **_NOT:_** Random Variable, Variable'dan farklıdır. Random değerler, bir deneyin **_olası_** sonuçlarını sayısal olarak temsil eden değişkenlerdir.

- Ayrık Rastgele Değişken (Discrete Random Variable): sayılabilir, tam sayı değerler

  ÖR: Bir zar atıldığında gelen sayı: {1, 2, 3, 4, 5, 6}

- Sürekli Rastgele Değişken (Continuous Random Variable): Sonsuz sayıda değer alabilir

  ÖR: Sınav süresi: 45.3 dakika, 59.999 dakika
