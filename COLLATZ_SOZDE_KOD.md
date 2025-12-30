# Collatz Şifreleme Algoritması - Sözde Kod (Pseudo-Code)

Aşağıda, Collatz Sanısı tabanlı akış şifreleme algoritmasının mantıksal akışı yer almaktadır.

## 1. Anahtar Türetme (Key Derivation)

```text
FONKSİYON DeriveSeed(anahtar_metni):
    seed = 0
    DÖNGÜ i, karakter İÇİN anahtar_metni'nde:
        seed = (seed * 31) + ASCII(karakter) * (i + 1)
    
    EĞER seed == 0 İSE:
        seed = 12345
    
    DÖNDÜR MutlakDeğer(seed)
```

## 2. Anahtar Akışı Üretimi (Keystream Generation)

```text
FONKSİYON GenerateKeystream(seed, uzunluk):
    n = seed
    original_seed = seed
    sayac = 0
    
    DÖNGÜ _ İÇİN 0'dan uzunluk'a KADAR:
        EĞER (n MOD 2) == 0 İSE:
            n = n / 2
        DEĞİLSE:
            n = 3 * n + 1
            
        EĞER n == 1 İSE:
            sayac = sayac + 1
            n = original_seed + (sayac * SABIT_DEGER)
            EĞER n == 0 İSE:
                n = 1
        
        anahtar_baytı = n MOD 256
        ÜRET (YIELD) anahtar_baytı
```

## 3. Şifreleme (Encryption)

```text
FONKSİYON Encrypt(metin, anahtar):
    seed = DeriveSeed(anahtar)
    veri_baytları = UTF8_Encode(metin)
    anahtar_akısı = GenerateKeystream(seed, Uzunluk(veri_baytları))
    
    sifreli_baytlar = []
    
    DÖNGÜ i İÇİN 0'dan Uzunluk(veri_baytları)'na KADAR:
        sifreli_bayt = veri_baytları[i] XOR anahtar_akısı[i]
        sifreli_baytlar'a ekle(sifreli_bayt)
        
    DÖNDÜR sifreli_baytlar
```

## 4. Deşifreleme (Decryption)

```text
FONKSİYON Decrypt(sifreli_baytlar, anahtar):
    seed = DeriveSeed(anahtar)
    anahtar_akısı = GenerateKeystream(seed, Uzunluk(sifreli_baytlar))
    
    cozulmus_baytlar = []
    
    DÖNGÜ i İÇİN 0'dan Uzunluk(sifreli_baytlar)'a KADAR:
        orijinal_bayt = sifreli_baytlar[i] XOR anahtar_akısı[i]
        cozulmus_baytlar'a ekle(orijinal_bayt)
        
    DÖNDÜR UTF8_Decode(cozulmus_baytlar)
```
