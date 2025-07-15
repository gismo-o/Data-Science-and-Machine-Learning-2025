# Python ile SQLite Veritabanı Uygulamaları

Python programlama diliyle SQLite veritabanı işlemlerinin nasıl yapıldığını adım adım öğrenmeye yönelik uygulamalı örnekler içerir.

## İçerik

- SQLite veritabanı oluşturma
- Tablolar oluşturma (`CREATE TABLE`)
- Veri ekleme (`INSERT INTO`)
- Veri sorgulama (`SELECT`)
- Verileri güncelleme (`UPDATE`) ve silme (`DELETE`)
- Sıralama, filtreleme, sınırlama (`ORDER BY`, `WHERE`, `LIMIT`)
- Toplu işlemler (`COUNT`, `AVG`, `MAX`, `MIN`, `GROUP BY`)
- SQL sorgularıyla örnek alıştırmalar

## Amaç

Bu notlar, **Course: Veri Bilimi ve Makine Öğrenmesi 2025 : 100 Günlük Kamp -Atıl Samancıoğlu**, **Section: 17** kapsamında öğrenilen konuları pekiştirmek amacıyla oluşturulmuştur.

## Kullanılan Teknolojiler

- Python (sqlite3 modülü)
- SQLite
- DBeaver (veritabanı görselleştirme aracı)

## DBeaver Kullanımı

Projede oluşturulan `students.db` dosyası, **DBeaver** ile açılarak:
- Tablolar görsel olarak incelenebilir
- Sorgular test edilebilir
- Veriler kolayca analiz edilebilir

DBeaver ile SQLite bağlantısı kurmak için:
1. DBeaver'ı açın.
2. "Yeni Veritabanı Bağlantısı" seçin.
3. `SQLite` seçin ve `students.db` dosyasını gösterin.
4. Bağlantıyı oluşturduktan sonra tabloları ve verileri inceleyebilirsiniz.
