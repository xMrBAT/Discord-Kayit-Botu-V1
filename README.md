# Discord Bot Projesi

Bu proje, belirli özelliklere sahip bir Discord botu oluşturmayı amaçlamaktadır. Bot, yeni katılan üyelere hoş geldin mesajı gönderir, belirli bir rol verir ve kayıt komutları kullanarak üyeleri kaydeder. Ayrıca, kayıt sayılarını kaydeder ve bot yeniden başlatıldığında bu bilgileri korur.

## İçindekiler

- [Gereksinimler](#gereksinimler)
- [Kurulum](#kurulum)
- [Yapılandırma](#yapılandırma)
- [Değişkenler](#değişkenler)
- [Botun Çalıştırılması](#botun-çalıştırılması)

## Gereksinimler

Bu botu çalıştırmak için aşağıdaki programlara ihtiyacınız olacak:

- Python 3.8 veya daha üstü
- `discord.py` kütüphanesi

## Kurulum

1. **Python'u İndirin ve Kurun**:
   Python'u [resmi web sitesinden](https://www.python.org/downloads/) indirip kurabilirsiniz.

2. **Gerekli Kütüphaneleri Yükleyin**:
   Terminal veya komut istemcisini açın ve aşağıdaki komutu girin:

   ```sh
   pip install discord.py
   ```

## Yapılandırma
**config.json Dosyasını Düzenleyin**:
   Proje dizininde `config.json` adlı bir dosya zaten var. Onu düzenleyebilirsiniz.
   Aşağıda, `config.json` dosyasının örneği bulunmakta:

   ```json
   {
     "token": "BOT TOKENİNİZ BURAYA",
     "prefix": "!",
     "welcome_channel_id": "HOŞGELDİN KANAL İDSİ",
     "welcome_message": "Hoşgeldin %user%! Sunucumuza katıldığın için teşekkürler. Şu anda %server% sunucusunda %member% kişiyiz.",
     "role_on_join_id": "KAYITSIZ ROLÜ İDSİ",
     "registered_role_id": "KAYITLI ROLÜ İDSİ",
     "log_channel_id": "KAYIT LOGLARI KANAL İDSİ"
   }
   ```

## Değişkenler

`welcome_message` içinde kullanılabilecek değişkenler:

- **%user%**: Sunucuya yeni katılan kullanıcıyı etiketler.
- **%server%**: Sunucunun adını belirtir.
- **%member%**: Sunucudaki toplam üye sayısını belirtir.
- **%inviter%**: Kullanıcıyı davet eden kişiyi etiketler.

## Botun Çalıştırılması

   Terminal veya komut istemcisini açın ve proje dizinine gidin. Ardından aşağıdaki komutu girin:

   ```sh
   python bot.py
   ```

Botunuz hayırlı olsun. Daha fazla özellik olan botlarımın örnekleri aşağıda bulunmaktadır:

