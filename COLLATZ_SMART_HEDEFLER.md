# Collatz Şifreleme Projesi - S.M.A.R.T Hedefler

Projenin başarısını ve sınırlarını tanımlayan S.M.A.R.T (Specific, Measurable, Achievable, Relevant, Time-bound) hedefler aşağıdadır.

## 1. Specific (Özgül)
**Hedef:** Collatz Sanısı'nın (3n+1 problemi) kaotik yapısını sözde rastgele sayı üreteci (PRNG) olarak kullanan, Python tabanlı bir akış şifreleme (stream cipher) algoritması ve komut satırı arayüzü (CLI) geliştirmek.
* **Ne:** Şifreleme algoritması.
* **Neden:** Matematiksel bir paradoksun kriptografik potansiyelini eğitim amaçlı göstermek.
* **Nasıl:** Python dili ve XOR bit işlemi kullanılarak.

## 2. Measurable (Ölçülebilir)
**Başarı Kriterleri:**
* Algoritmaya verilen herhangi bir ASCII metni, anahtar kullanılarak şifrelenebilmeli.
* Şifrelenmiş veri (hex formatında), aynı anahtar kullanılarak hatasız bir şekilde orijinal metne dönüştürülebilmeli.
* `demo.py` dosyası çalıştırıldığında kullanıcı etkileşimi (veri girişi/çıkışı) sorunsuz gerçekleşmeli.
* Kod tabanı anlaşılır olmalı ve temel Python standart kütüphaneleri dışında harici kütüphane gerektirmemelidir.

## 3. Achievable (Ulaşılabilir)
**Kaynaklar ve Yöntem:**
* Modern bilgisayarların işlem gücü, Collatz dizilerini saniyeler içinde hesaplamak için fazlasıyla yeterlidir.
* Python'un yerleşik büyük tamsayı (bignum) desteği, sayıların taşma (overflow) riski olmadan işlenmesini sağlar.
* Proje kapsamı "eğitim ve hobi" ile sınırlandırılarak, askeri düzeyde güvenlik (AES vb.) sağlama zorunluluğu kaldırılmış ve hedef gerçekçi tutulmuştur.

## 4. Relevant (İlgili/Amaca Uygun)
**Bağlam:**
* Bu proje, basit matematiksel kuralların karmaşık ve tahmin edilmesi zor sonuçlar doğurabileceğini gösteren "Kaos Teorisi" çalışmalarına örnektir.
* Kriptografi meraklıları için "kendi algoritmanı yazma" sürecindeki zorlukları (döngü sorunları, rastgelelik kalitesi vb.) pratik olarak gösterir.
* Collatz Sanısı popüler bir matematik problemi olduğu için ilgi çekicidir.

## 5. Time-bound (Zamanlı)
**Zaman Çizelgesi:**
* **Tasarım ve Araştırma:** Tamamlandı (Rapor Oluşturuldu).
* **Kodlama (Prototip):** Tamamlandı (v1.0 hazır).
* **Dokümantasyon (SWOT & Kullanım):** Tamamlandı.
* **Proje Teslimi:** 30 Aralık 2025 itibarıyla çalışan, test edilmiş ve raporlanmış bir sürüm teslim edilecektir (Bugün).
