import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('data/cleaned_data.csv')

# Etiket dağılımı
sns.countplot(x='label', data=df)
plt.title('Etiket Dağılımı (0: Güvenli, 1: Dolandırıcı)')
plt.xlabel('Etiket')
plt.ylabel('Adet')
plt.show()

# Mesaj uzunluğu dağılımı
sns.histplot(df['message_length'], bins=10, kde=True)
plt.title('Mesaj Uzunluğu Dağılımı')
plt.xlabel('Mesaj Uzunluğu')
plt.ylabel('Adet')
plt.show() 