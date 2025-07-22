import pandas as pd

df = pd.read_csv('data/social_media_fraud.csv')
# Eksik verileri çıkar
df.dropna(inplace=True)
# Kategorik veri yok, gerekirse get_dummies eklenebilir
# df = pd.get_dummies(df)
# user_id modelde kullanılmayacak, çıkarıyoruz
df = df.drop('user_id', axis=1)
# Temizlenmiş veriyi kaydet
df.to_csv('data/cleaned_data.csv', index=False)
print('Veri temizlendi ve kaydedildi!') 