Sosyal Medya Dolandırıcılık Tespit Projesi
Bu proje, sosyal medya kullanıcılarının davranışlarına göre dolandırıcılık tespiti yapmak için makine öğrenimi modeli kullanır.

Adımlar
Veri seti: data/social_media_fraud.csv dosyasında örnek veri bulunmaktadır.
Ön işleme: preprocessing.py ile veri temizlenir.
Görselleştirme: visualization.py ile veri analiz edilir.
Model eğitimi: model.py ile model eğitilir ve kaydedilir.
Arayüz: app.py ile Streamlit tabanlı kullanıcı arayüzü sunulur.

📦 Kurulum git clone https://github.com/musa-arrow/MyFirstMLProject.git
cd MyFirstMLProject
pip install -r requirements.txt
streamlit run app.py

🌐 Canlı Uygulama https://machinelearning-eogz62bkfgyrjp3qocnbvd.streamlit.app

Özellikler
Mesaj uzunluğu
Link sayısı
Hashtag sayısı
Profil fotoğrafı var mı
Hesap onaylı mı
Hesap yaşı (gün)

Lisans
MIT
