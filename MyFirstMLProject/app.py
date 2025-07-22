import streamlit as st
import joblib
import numpy as np
import os

st.title('Sosyal Medya Dolandırıcılık Tespit Aracı')
model_path = os.path.join(os.path.dirname(__file__), 'model.joblib')
model = joblib.load(model_path)

message_length = st.number_input('Mesaj Uzunluğu', min_value=0)
num_links = st.number_input('Link Sayısı', min_value=0)
num_hashtags = st.number_input('Hashtag Sayısı', min_value=0)
has_profile_pic = st.selectbox('Profil Fotoğrafı Var mı?', [0, 1])
is_verified = st.selectbox('Hesap Onaylı mı?', [0, 1])
account_age_days = st.number_input('Hesap Yaşı (gün)', min_value=0)

if st.button('Tahmin Et'):
    features = np.array([[message_length, num_links, num_hashtags, has_profile_pic, is_verified, account_age_days]])
    prediction = model.predict(features)
    st.write('Sonuç:', 'Dolandırıcı' if prediction[0] == 1 else 'Güvenli') 
