Anladım, README dosyasını doğrudan kopyalayıp kullanabileceğiniz şekilde kod bloğu olarak yazıyorum:

```markdown
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

1. **config.json Dosyasını Oluşturun**:
   Proje dizininde `config.json` adlı bir dosya oluşturun ve aşağıdaki içeriği ekleyin:

   ```json
   {
     "token": "YOUR_BOT_TOKEN",
     "prefix": "!",
     "welcome_channel_id": "WELCOME_CHANNEL_ID",
     "welcome_message": "Hoşgeldin %user%! Sunucumuza katıldığın için teşekkürler. Şu anda %server% sunucusunda %member% kişiyiz.",
     "role_on_join_id": "ROLE_ON_JOIN_ID",
     "registered_role_id": "REGISTERED_ROLE_ID",
     "log_channel_id": "LOG_CHANNEL_ID"
   }
   ```

2. **config.json Değerlerini Güncelleyin**:
   - `token`: Botunuzun Discord API token'ı.
   - `prefix`: Botunuzun komut ön eki.
   - `welcome_channel_id`: Hoş geldin mesajlarının gönderileceği kanalın ID'si.
   - `welcome_message`: Yeni üyeler için hoş geldin mesajı. `%user%`, `%server%`, `%member%` ve `%inviter%` değişkenlerini kullanabilirsiniz.
   - `role_on_join_id`: Yeni katılan üyelere verilecek rolün ID'si.
   - `registered_role_id`: Kayıtlı üyelere verilecek rolün ID'si.
   - `log_channel_id`: Kayıt işlemlerinin loglanacağı kanalın ID'si.

## Değişkenler

`welcome_message` içinde kullanılabilecek değişkenler:

- **%user%**: Sunucuya yeni katılan kullanıcıyı etiketler.
- **%server%**: Sunucunun adını belirtir.
- **%member%**: Sunucudaki toplam üye sayısını belirtir.
- **%inviter%**: Kullanıcıyı davet eden kişiyi etiketler.

## Botun Çalıştırılması

1. **bot.py Dosyasını Oluşturun**:
   Proje dizininde `bot.py` adlı bir dosya oluşturun ve bot kodunu bu dosyaya ekleyin.

2. **Botu Çalıştırın**:
   Terminal veya komut istemcisini açın ve proje dizinine gidin. Ardından aşağıdaki komutu girin:

   ```sh
   python bot.py
   ```

Botunuz şimdi çalışıyor olmalı ve belirtilen işlevleri yerine getirmelidir.
```

Bu README dosyasını doğrudan kopyalayıp kullanabilirsiniz. Herhangi bir sorunuz veya sorununuz olursa, lütfen bana bildirin!
