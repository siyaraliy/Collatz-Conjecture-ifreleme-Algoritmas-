# Collatz Şifreleme Algoritması Raporu

## 1. Giriş
collatz sanısı (Collatz Conjecture), her pozitif tam sayının eninde sonunda 1'e ulaşacağını öne süren bir matematik problemidir. "3n + 1" problemi olarak da bilinir. Bu proje, bu dizinin kaotik yapısını kullanarak veri şifreleme amacıyla bir **Akış Şifresi (Stream Cipher)** oluşturmayı hedefler.

## 2. Temel Mantık
Algoritma, gizli bir anahtarı (key) kullanarak, Collatz dizisi kurallarına göre sözde rastgele (pseudo-random) bir sayı akışı üretir. Bu akış, şifrelenecek verinin her baytı ile XOR (Dışlayıcı VEYA) işlemine sokulur.

Mantık Denklemi:
$$ C_i = P_i \oplus K_i $$
* $P_i$: Açık metnin i. baytı
* $K_i$: Üretilen anahtar akışının i. baytı
* $C_i$: Şifrelenmiş metnin i. baytı

## 3. Algoritma Adımları

### A. Çekirdek (Seed) Oluşturma
Kullanıcının girdiği metin tabanlı şifre, sayısal bir başlangıç değerine (seed) dönüştürülür.
* Örnek Yöntem: Şifredeki karakterlerin ASCII değerlerinin, ağırlıklı toplamı veya çarpımı alınarak büyük bir tam sayı elde edilir.

### B. Anahtar Akışı Üretimi (Keystream Generation)
Başlangıç sayısı $N$ olsun. Her bayt için şu adımlar izlenir:

1. **Collatz Adımı**:
   - Eğer $N$ çift ise: $N \leftarrow N / 2$
   - Eğer $N$ tek ise: $N \leftarrow 3N + 1$

2. **Bayt Eldesi**:
   - Üretilen $N$ sayısının mod 256'sı alınır: $K = N \pmod{256}$
   - Bu $K$ değeri, şifreleme anahtarının bir parçasıdır.

3. **Döngü Yönetimi (Anti-Loop)**:
   - Collatz dizisi doğal olarak 4-2-1 döngüsüne girer. Şifrelemenin durmaması veya tekrar etmemesi için, $N$ değeri 1'e ulaştığında (veya döngü tespit edildiğinde), $N$ değeri orijinal seed veya sayaç (step count) kullanılarak değiştirilir.
   - Örnek: $N \leftarrow Seed + StepCount$

### C. Şifreleme / Deşifreleme
- Şifreleme: Metin baytları ile üretilen anahtar baytları XORlanır.
- Deşifreleme: Şifreli metin baytları aynı anahtar akışı ile tekrar XORlandığında orijinal metin geri döner.

## 4. Örnek Senaryo
**Anahtar**: "gizli"  -> **Seed**: 12345 (Varsayımsal)

1. **Adım 1**: $N=12345$ (Tek) -> $3N+1 = 37036$
   - $K_1 = 37036 \pmod{256} = 172$
2. **Adım 2**: $N=37036$ (Çift) -> $N/2 = 18518$
   - $K_2 = 18518 \pmod{256} = 86$

**Açık Metin**: "A" (ASCII 65)
**Şifreli Bayt**: $65 \oplus 172 = 237$

## 5. Güvenlik Değerlendirmesi
Bu algoritma, **eğitim ve hobi amaçlı** tasarlanmıştır. Collatz dizisinin rastgeleliği kriptografik olarak güvenli (CSPRNG) kanıtlanmamıştır. Askeri veya ticari güvenlik gerektiren durumlarda **AES** veya **ChaCha20** gibi standartlar kullanılmalıdır.
