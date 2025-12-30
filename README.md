# Collatz Şifreleme Algoritması Projesi

Bu proje, ünlü matematik problemi **Collatz Sanısı** (3n+1 Problemi) kullanılarak geliştirilmiş bir akış şifreleme (stream cipher) algoritmasıdır. Eğitim ve hobi amaçlı tasarlanmıştır.

## 📁 Proje İçeriği

### Kaynak Kodlar
* **`collatz_cipher.py`**: Şifreleme mantığını içeren ana Python kütüphanesi.
* **`demo.py`**: Kullanıcıların metin şifreleyip çözmesi için komut satırı arayüzü (CLI).
* **`test_cipher.py`**: Otomatik birim testlerini içeren dosya.

### Dokümantasyon
* **`COLLATZ_ALGORITMA_RAPORU.md`**: Algoritmanın matematiksel temeli ve tasarım raporu.
* **`COLLATZ_AKIS_SEMASI.md`**: Algoritmanın görsel akış diyagramı (Mermaid).
* **`COLLATZ_SOZDE_KOD.md`**: Dilden bağımsız sözde kod (pseudo-code).
* **`COLLATZ_SWOT_ANALIZI.md`**: Projenin güçlü ve zayıf yönlerinin analizi.
* **`COLLATZ_SMART_HEDEFLER.md`**: Proje hedefleri.
* **`TEST_RAPORU.md`**: Test sonuçları ve değerlendirmesi.
* **`PROJE_INCELEME_RAPORU.md`**: Genel tutarlılık incelemesi.

## 🚀 Kurulum ve Çalıştırma

Bu proje **Python 3** gerektirir. Ekstra bir kütüphane kurulumuna ihtiyaç duymaz.

### Demoyu Çalıştırma (CLI)
Terminali açın ve proje dizinine giderek şu komutu yazın:
```bash
python3 demo.py
```
Menüden seçim yaparak şifreleme ve deşifreleme işlemleri yapabilirsiniz.

### Testleri Çalıştırma
Otomatik testleri görmek için:
```bash
python3 test_cipher.py
```

## ⚠️ Yasal Uyarı
Bu algoritma kriptografik olarak güvenli (secure) değildir. **Collatz Cipher**, modern güvenlik standartlarını karşılamaz. Gerçek verilerinizi (kredi kartı, kişisel bilgiler vb.) korumak için **KULLANMAYINIZ**. Sadece eğitim, araştırma ve eğlence amaçlıdır.

## 👨‍💻 Geliştirici
Antigravity AI (Google Deepmind) tarafından, kullanıcı işbirliği ile geliştirilmiştir.
