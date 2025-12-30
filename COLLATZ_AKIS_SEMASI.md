# Collatz Şifreleme Algoritması - Akış Şeması

Bu belge, algoritmanın çalışma mantığını Mermaid diyagramı ile görselleştirir.

```mermaid
flowchart TD
    Start([Başlat]) --> InputText[/Kullanıcıdan Metin Al/]
    Start --> InputKey[/Kullanıcıdan Anahtar Al/]
    
    InputKey --> DeriveSeed[[Seed Türetme Fonksiyonu]]
    DeriveSeed --> SeedValue[Seed Değeri Oluşur]
    
    InputText --> ByteLoop{Döngü: Her Karakter İçin}
    SeedValue --> ByteLoop
    
    ByteLoop -->|Veri Var| CollatzStep{n Çift mi?}
    
    subgraph KeystreamGenerator [Anahtar Akışı Üreteci]
        CollatzStep -- Evet --> EvenOp[n = n / 2]
        CollatzStep -- Hayır --> OddOp[n = 3n + 1]
        
        EvenOp --> CheckOne{n == 1 mi?}
        OddOp --> CheckOne
        
        CheckOne -- Evet --> Reseed[Anti-Loop: n'i Değiştir]
        CheckOne -- Hayır --> Modulo[Byte = n % 256]
        Reseed --> Modulo
    end
    
    Modulo --> XORKey[/Anahtar Baytı/]
    ByteLoop --> XORText[/Metin Baytı/]
    
    XORKey --> XOROp((XOR))
    XORText --> XOROp
    
    XOROp --> OutputEnc[/Şifreli Bayt/]
    OutputEnc --> ByteLoop
    
    ByteLoop -->|Veri Bitti| Result([Sonuç Çıktısı])
```

## Açıklamalar
1. **Seed Türetme**: String anahtar, matematiksel işlemlerle bir başlangıç sayısına (seed) dönüştürülür.
2. **Collatz Döngüsü**: Seed üzerinden Collatz kuralları uygulanarak sayı sürekli değişir. Her adımda yeni bir sayı üretilir.
3. **XOR İşlemi**: Üretilen sayının mod 256'sı (anahtar baytı) ile metin karakterinin ASCII değeri (metin baytı) XOR'lanarak şifreli veri elde edilir.
