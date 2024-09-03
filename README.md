
# Platformer Quest

**Platformer Quest**, Python'un Pygame kütüphanesi kullanılarak geliştirilmiş basit ama eğlenceli bir platform oyunudur. Oyuncu, çeşitli platformlar arasında hareket ederek karakteri yönlendirir, engellerden kaçınır ve seviyelerde ilerler. Amaç, her seviyede bulunan ışınlanma noktasına ulaşmak ve kırmızı toplardan kaçınmaktır.

## İçindekiler

1. [Özellikler](#özellikler)
2. [Kurulum](#kurulum)
3. [Oynanış](#oynaniş)
4. [Kontroller](#kontroller)
5. [Oyun Yapısı](#oyun-yapısı)
6. [Nasıl Çalıştırılır](#nasıl-çalıştırılır)
7. [Sorun Giderme](#sorun-giderme)
8. [Katkıda Bulunma](#katkıda-bulunma)
9. [Lisans](#lisans)

## Özellikler

- **Dinamik Seviye Oluşturma:** Her seviye rastgele oluşturulur, bu da her oyunun benzersiz olmasını sağlar.
- **Uyarlanabilir Zorluk:** İlerledikçe düşman sayısı artar, bu da oyunu daha zorlu hale getirir.
- **Yeniden Başlatma Mekanizması:** Oyuncu bir düşmanla çarpıştığında oyun kapanmaz, bir oyun bitti ekranı gösterilir ve oyuncu herhangi bir tuşa basarak oyunu yeniden başlatabilir.
- **Platform Hareketi:** Oyun ekranı, oyuncu yukarı doğru ilerledikçe yukarı kayar, bu da dinamik ve sürekli bir oyun alanı oluşturur.
- **Çift Zıplama:** Oyuncu çift zıplama yapabilir, bu da daha yüksek platformlara ulaşmasını sağlar.

## Kurulum

### Gereksinimler

Platformer Quest'i çalıştırmak için ihtiyacınız olanlar:

- Sisteminizde yüklü Python 3.6 veya daha yeni bir sürüm.
- Pygame kütüphanesi yüklü olmalıdır.

### Python Kurulumu

Python'u resmi web sitesinden indirebilirsiniz: [python.org](https://www.python.org/downloads/).

### Pygame Kurulumu

Python yüklendikten sonra, pip kullanarak Pygame'i yükleyebilirsiniz:

```bash
pip install pygame
```

### Depoyu Klonlama

Henüz depo klonlanmadıysa, aşağıdaki komut ile klonlayabilirsiniz:

```bash
git clone https://github.com/kullaniciadi/platformer-quest.git
```

Alternatif olarak, ZIP dosyasını depodan indirip istediğiniz yere çıkarabilirsiniz.

## Oynanış

Platformer Quest'in ana hedefi, karakteri platformlar arasında zıplatarak ve engellerden kaçınarak ilerletmektir. İlerledikçe, seviyeler daha zorlu hale gelir.

### Seviyeler

Her seviye rastgele oluşturulur, bu nedenle her oynanış benzersizdir. Platformlar farklı yüksekliklerde konumlandırılır ve her seviyede ışınlanma noktasına ulaşmanız gerekir.

### Düşmanlar

Kırmızı toplar ekranda yatay ve dikey olarak hareket eder ve oyuncu için bir tehdit oluşturur. Bir düşmanla çarpışmak oyunun sona ermesine neden olur, ancak oyuncu herhangi bir tuşa basarak yeniden başlayabilir.

## Kontroller

- **Sol Ok:** Sola hareket.
- **Sağ Ok:** Sağa hareket.
- **Boşluk Tuşu:** Zıplama (Çift zıplama için iki kez basılabilir).
- **Herhangi Bir Tuş (Oyun Bitti Ekranı):** Oyunu yeniden başlat.

## Oyun Yapısı

### Ana Bileşenler

- **Oyuncu:** Oyuncu tarafından kontrol edilen ana karakter. Sola, sağa hareket edebilir ve zıplayabilir.
- **Platformlar:** Oyuncunun üzerinde zıplayabileceği statik platformlar.
- **Düşmanlar:** Ekranda hareket eden kırmızı toplar. Onlara çarpmak oyunun bitmesine neden olur.
- **Işınlanma Noktası:** Her seviyenin hedefi olan yeşil platform. Bu noktaya ulaşmak bir sonraki seviyeye geçmenizi sağlar.

### Kod Yapısı

- **`main.py`:** Oyunun ana dosyasıdır ve tüm mantık, oyuncu hareketi, seviye oluşturma, düşman davranışı ve oyun akışı burada yer alır.

### Ana Fonksiyonlar

- **`create_random_level()`:** Yeni bir seviye oluşturur, platformları ve düşmanları yerleştirir.
- **`game_loop()`:** Oyuncu girişi, oyun güncellemeleri ve ekranın çizimi gibi ana oyun döngüsünü yönetir.
- **`show_start_screen()`:** Oyunun başlamadan önce gösterilen başlangıç ekranını gösterir.
- **`show_game_over_screen()`:** Oyuncu kaybettiğinde gösterilen oyun bitti ekranını gösterir.

## Nasıl Çalıştırılır

Gerekli bağımlılıkları yükledikten sonra, `main.py` dosyasının bulunduğu dizine gidin ve oyunu aşağıdaki komutla başlatın:

```bash
python main.py
```

Bu, oyunu başlatır ve başlangıç ekranını görürsünüz. "Oyuna Başla"ya tıklayarak oyuna başlayabilirsiniz.

## Sorun Giderme

### Yaygın Sorunlar

- **Oyun başlatıldığında çöküyor:**
  - Python 3.6+ ve Pygame'in doğru bir şekilde yüklendiğinden emin olun.
  - Tüm gerekli dosyaların doğru dizinde olduğundan emin olun.

- **Oyun penceresi açılır açılmaz kapanıyor:**
  - Komut satırından çalıştırarak hata mesajlarını kontrol edin.
  - `main.py` dosyasının doğru dizinde bulunduğundan emin olun.

- **Grafikler veya kontroller beklendiği gibi çalışmıyor:**
  - Pygame kurulumunun güncel olduğundan emin olun.
  - Oyunu farklı bir terminal veya konsol penceresinde çalıştırmayı deneyin.

### İletişim

Burada ele alınmayan sorunlarla karşılaşırsanız, depoda bir sorun açabilir veya benimle iletişime geçebilirsiniz.

## Katkıda Bulunma

Platformer Quest'i geliştirmek için katkılarınızı memnuniyetle karşılıyoruz! İşte nasıl katkıda bulunabileceğiniz:

1. **Depoyu GitHub'da çatallayın.**
2. **Yeni bir dal oluşturun** (branch) özelliğiniz veya hata düzeltmeniz için.
3. **Değişikliklerinizi açıklayan bir mesajla commit yapın.**
4. **Dalınızı GitHub'a yükleyin** (push).
5. **Bir çekme isteği** (pull request) oluşturarak değişikliklerinizin gözden geçirilmesini sağlayın.

Lütfen uygun testleri güncellemeyi ve mevcut kod stiline uymayı unutmayın.
