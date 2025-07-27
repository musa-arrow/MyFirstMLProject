# Sosyal Medya Dolandırıcılık Tespit Projesi

Bu proje, sosyal medya kullanıcılarının davranışlarına göre dolandırıcılık tespiti yapmak için makine öğrenimi modeli kullanır.

## Adımlar
1. Veri seti: `data/social_media_fraud.csv` dosyasında örnek veri bulunmaktadır.
2. Ön işleme: `preprocessing.py` ile veri temizlenir.
3. Görselleştirme: `visualization.py` ile veri analiz edilir.
4. Model eğitimi: `model.py` ile model eğitilir ve kaydedilir.
5. Arayüz: `app.py` ile Streamlit tabanlı kullanıcı arayüzü sunulur.

## Kurulum
```bash
pip install -r requirements.txt
```

## Kullanım
1. Ön işleme ve model eğitimi için sırasıyla:
```bash
python preprocessing.py
python model.py
```
2. Streamlit arayüzünü başlatmak için:
```bash
streamlit run app.py
```

## Özellikler
- Mesaj uzunluğu
- Link sayısı
- Hashtag sayısı
- Profil fotoğrafı var mı
- Hesap onaylı mı
- Hesap yaşı (gün)

## Lisans
MIT 
