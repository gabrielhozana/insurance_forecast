# -*- coding: utf-8 -*-
"""Insurance Forecast .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-VKtIDzPuTCE-h6VPWaBfgj4IRiSKV3m

# **Laporan Proyek Machine Learning - Gabril Hozanna**

## **Domain Proyek**
Kesehatan adalah suatu faktor yang sangat berharga didalam hidup. Tubuh yang sehat sanggup meringankan kita dalam melakukan berbagai macam pekerjaan dan kesibukan tanpa kendala. 

Tidak ada yang bisa menjamin kesehatan seseorang, tua maupun muda, akan luput dari ancaman penyakit. Untuk itu, asuransi kesehatan hadir sebagai penyokong dalam mempersiapkan hal-hal yang tidak diinginkan di masa depan.

Asuransi kesehatan hadir sebagai penanggung yang mencakup pembayaran biaya medis, bedah, maupun perawatan kesehatan lainnya. Polis asuransi diterbitkan oleh perusahaan asuransi untuk mengganti biaya tertanggung untuk membayarkan biaya medis dikarenakan sakit atau mengalami cedera.

Sebagian orang menganggap premi atau nominal yang harus dibayarkan nasabah terlampau besar. Namun, jangan salah, manfaat yang bisa didapatkan dengan mendaftar asuransi kesehatan juga tidak sedikit. Membeli asuransi kesehatan untuk diri sendiri berguna sebagai antisiapsi biaya rumah sakit yang tidak bisa diprediksi di masa mendatang. Selain itu, hal ini bisa membantu meringankan beban keluarga.

Orang mulai sadar akan pentingnya memiliki asuransi kesehatan pribadi. Alasan utama, asuransi kesehatan pribadi dapat menanggulangi biaya kesehatan secara cepat saat terjadi darurat medis. Belum lagi dengan fakta bahwa biaya kesehatan di Indonesia mengalami peningkatan tahun ke tahun. [Survei 2020 Global Medical Trends Survey Report](https://www.willistowerswatson.com/en-us/Insights/2019/11/2020-global-medical-trends-survey-report) yang dirilis firma Willis Tower Watson menyatakan, gross medical inflation atau biaya kesehatan di Indonesia tahun 2019 naik hampir 10% dari tahun sebelumnya. Sementara tahun 2020, biaya kesehatan diprediksi akan meroket lagi hingga 11%. Peningkatan ini disinyalir bakal lebih tinggi dibanding rata-rata biaya kesehatan di negara Asia Pasifik yang menyentuh level 7%. Melihat tren biaya kesehatan yang terus meningkat, memiliki asuransi pribadi merupakan keputusan yang bijak.

Memiliki asuransi kesehatan membuat kita tidak perlu terlalu mengkhawatirkan masalah biaya medis karena perusahaan asuransi akan menanggungnya. Untuk itu, penting mengetahui dan memahami produk asuransi yang tepat tapi sebenarnya perlu dipahami terlebih dahulu faktor-faktor apa saja yang mempengaruhi pembelian asuransi kesehatan bisa mahal dan pembeli dapat menjadikan acuan sebagai biaya pembelian asuransi kesehatan yang akan mendatang.

## **Business Understanding**

### Problem Statements

*   Bagaimana mengetahui faktor apa saja yang dapat mempengaruhi biaya pembelian asuransi kesehatan.
*   Bagaimana menghasilkan performa model yang seakurat mungkin terhadap biaya asuransi yang harus dikeluarkan/dibeli.

### Goals

* Untuk mengetahui faktor-faktor apa saja yang dapat mempengaruhi biaya pembelian asuransi kesehatan

* Menghasilkan model machine learning yang dapat memprediksi biaya asuransi kesehatan seakurat mungkin sebagai tolak ukur dalam pembelian asuransi kesehatan

### Solution statements

1. Untuk dapat mengetahui faktor-faktor apa saja yang dapat mempengaruhi biaya pembelian asuransi kesehatan, maka dilakukan hal berikut:
* Melakukan EDA agar mendapatkan wawasan informasi yang dibutuhkan. Salah satu penerapan yang dapat dilakukan adalah dengan melakukan visualisasi data feature terhadap data target dalam hal ini fitur-fitur yang terdapat pada dataset dan charges sebagai data target.
* Menggunakan feature importance.Feature importance mengacu pada teknik yang menetapkan score ke fitur input berdasarkan seberapa berguna fitur tersebut dalam memprediksi variabel target. Feature importance score memainkan peran penting dalam proyek pemodelan prediktif, termasuk memberikan wawasan tentang data, wawasan model, dan dasar untuk pengurangan dimensi dan pemilihan fitur yang dapat meningkatkan efisiensi dan efektivitas model prediktif pada masalah.

2. Untuk menghasilkan model machine learning yang dapat memprediksi seakurat mungkin, maka digunakan tiga algoritma regresi mengingat data yang digunakan berupa data regresi dan adapun algoritmanya yaitu, linear regression, polynomial regression dan random forest.
* **Linear regression** adalah suatu model statistik yang umum dan paling sederhana yang digunakan untuk Machine Learning untuk melakukan prediksi dengan cara supervised learning. Linear regression hanya bisa digunakan untuk data yang bersifat interval dan ratio yang biasanya bersifat diskrit dan kontinu, dan merupakan analisis bivariate dan multivariate. Linear regression digunakan untuk Prediksi dengan mencari pola garis terbaik antara variable independent dan dependen. Kelebihan, mudah diimplementasikan dan digunakan untuk memprediksi nilai numerik/ continous /data jenis interval dan ratio. Sedangakan kekurangannya, cenderung mudah Overfitting dan tidak dapat digunakan bila relasi antara variabel independen dan dependen tidak linier atau korelasi variabel rendah 
* **Polynomial regression** seperti linear regression yang menggunakan hubungan antara variabel x dan y untuk menemukan cara terbaik untuk menarik garis melalui titik data. Polynomial regression merupakan regresi dengan fungsinya adalah kuadratik, di mana nilai variabel independen ada yang bernilai pangkat 1, pangkat 2, pangkat n dan seterusnya. Nilai pangkat 2 sering disebut dengan orde 2, pangkat 3 dengan orde 3 dan seterusnya. Penggunaan polinomial ketika ingin mencari hubungan antara 1 variabel dependen dengan 1 variabel independen. Jika hanya ingin mencari hubungan terhadap 1 variabel independen, kapan menggunakan simple dan kapan menggunakan polinomial? Jawabannya adalah dilihat seberapa fit model yang dibangun dengan data aslinya. Jika menggunakan simple linear sudah fit, maka cukup menggunakan model ini saja, namun jika tidak dan fungsinya tampak seperti fungsi polinomial (fungsi kuadratik) maka kita coba dekati dengan metode polinomial. Jika menggunakan simple dan polinomial tidak juga fit, maka hubungan antara keduanya bukanlah linear, sehingga harus menggunakan algoritma regresi non linear. 
* **Random forest** adalah salah satu algoritma supervised learning. Dapat digunakan untuk menyelesaikan masalah klasifikasi dan regresi. Random forest merupakan kombinasi dari masing ??? masing pohon (tree) dari model Decision Tree yang baik, dan kemudian dikombinasikan ke dalam satu model. Penggunaan tree yang semakin banyak akan mempengaruhi akurasi yang akan didapatkan menjadi lebih baik. Penentuan klasifikasi dengan random forest diambil berdasarkan hasil voting dari tree yang terbentuk. 
 * Kelebihan:
   * Menghasilkan eror yang lebih rendah. 
   * Memberikan hasil yang bagus dalam klasifikasi.
   * Dapat mengatasi data training dalam jumlah sangat besar secara efisien.
   * Metode yang efektif untuk mengestimasi hilangnya data.
   * Dapat memperkiraan variabel apa yang penting dalam klasifikasi.
   * Menyediakan metode eksperimental untuk mendeteksi interaksi variabel.
 * Kekurangan:
   * Waktu pemrosesan yang lama karena menggunakan data yang banyak dan membangun model tree yang banyak pula untuk membentuk random trees karena menggunakan single processor.
   * Interpretasi yang sulit dan membutuhkan mode penyetelan yang tepat untuk data.
   * ketika digunakan untuk regresi, mereka tidak dapat memprediksi di luar kisaran dalam data percobaan, hal ini di mungkinkan data terlalu cocok dengan kumpulan data pengganggu (noisy).

## **Data Understanding**

Banyak faktor yang mempengaruhi berapa banyak biaya asuransi kesehatan yang harus dibayar. Ada baiknya untuk memiliki pemahaman terkait faktor-faktor tersebut. Berikut adalah beberapa faktor yang mempengaruhi berapa biaya premi asuransi kesehatan:
[Medical Cost Personal Datasets](https://www.kaggle.com/mirichoi0218/insurance)



* age: Usia penerima. 
* sex: *Gender* penerima asuransi, *female*, *male*.
* bmi (*Body Mass Index*): Memberikan pemahaman tentang tubuh, berat badan yang relatif tinggi atau relatif rendah terhadap tinggi badan.  Indeks objektif berat badan (kg/m^2) menggunakan rasio tinggi terhadap berat badan, idealnya 18,5 hingga 24,9.
* children: Jumlah anak yang ditanggung oleh asuransi kesehatan atau jumlah tanggungan.
* smoker: Perokok atau bukan perokok.
* region: Wilayah penerima di AS, *northeast*, *southeast*, *southwest*, *northwest*.
* charges: Biaya medis individu yang ditagih oleh asuransi kesehatan.

### Exploratory Data Analysis (EDA)

**Load Dataset**

Menginstall library kaggle dan mengupload api kaggle untuk dapat mengunduh langsung dataset dari kaggle.
"""

!pip install kaggle

from google.colab import files

uploaded = files.upload()

for fn in uploaded.keys():
  print('User uploaded file "{name}" with length {length} bytes'.format(
      name=fn, length=len(uploaded[fn])))
  
# Then move kaggle.json into the folder where the API expects to find it.
!mkdir -p ~/.kaggle/ && mv kaggle.json ~/.kaggle/ && chmod 600 ~/.kaggle/kaggle.json

"""Mengunduh dan mengekstrak dataset insurance

Dengan perintah `%%bash` mengakses langsung dari kernel linux dalam hal ini tanpa perlu menggunakan perintah `!` diawal perintah (command) untuk mengeksekusi sebuah perintah linux.

Untuk dapat mengunduh dataset dari kaggle maka dapat menggunakan perintah (command) `kaggle datasets download` dan disertakan dengan `<user kaggle>/<nama_dataset>`

Terakhir mengekstrak dataset dengan perintah `unzip <nama_file>`
"""

# Commented out IPython magic to ensure Python compatibility.
# %%bash
# kaggle datasets download -d mirichoi0218/insurance
# 
# unzip insurance.zip

"""Load library yang diperlukan dalam pengembangan model dan analisa data."""

import pandas as pd #dataframe
import numpy as np #komputasi numerik
#visualisasi
import matplotlib.pyplot as plt 
import seaborn as sns 
from sklearn.preprocessing import LabelEncoder,StandardScaler,PolynomialFeatures #preprocessing data
#membagi data
from sklearn.model_selection import train_test_split 
#load model
from sklearn.linear_model import LinearRegression 
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score,mean_squared_error 
#metrics
from sklearn import metrics

"""Membaca dataset menggunakan library pandas.

Dataset yang telah diekstrak sebelumnya, untuk dapat ditampilkan dalam bentuk dataframe maka dapat menggunakan pandas dengan fungsi `read_csv` untuk membaca file csv.
"""

df = pd.read_csv("insurance.csv")

"""Menggunakan fungsi `head()` untuk menampilkan beberapa data. Berguna untuk mendapatkan sebuah gambaran sekilas akan data. 

Secara default menampilkan 5 data.
"""

df.head()

"""Mengecek secara bentuk data dalam hal ini untuk mengetahui berapa banyaknya data (row) dan banyaknya kolom pada dataset dengan perintah `shape` """

df.shape

"""Terdapat 1338 baris data atau banyaknya sample data dan terdapat 7 kolom atau feature pada dataset yang digunakan saat ini.

**Analisa Statistika Deskriptif**
"""

df.describe()

"""Didapatkan beberapa hasil berupa:
* Banyaknya sample 1338.
* rata-rata umur 39, memiliki bmi 30, jumlah anak 1 dan biaya 13270 yang harus dibayarkan. 
* tertua dengan umur 64 tahun dan termuda ada 18 tahun.
* dsb

**Dataset Info**

Menggunakan fungsi `info()` untuk mendapatkan informasi berupa type data dan mengecek data null.

Jika dilihat tidak terdapat data null dan terdapat beberapa tipe data object (string) dalam hal ini pada fitur sex, smoker dan region.
"""

df.info()

"""Mengecek region-region apa saja yang terdapat pada dataset dengan menggunakan fungsi `unique()`.

Jika dilihat terdapat 4 region.
"""

df['region'].unique()

"""Memastikan data tidak ada yang null."""

df.isnull().sum()

"""**Visualisasi**

Melakukan visualisasi data pada data tipe numerik.
"""

sns.boxplot(x=df['age'])

"""Jika dilihat pada visualisasi boxplot `age`, umur termudah berada di umur 18 tahun, rata-rata 39 tahun dan tertua 64 tahun. """

sns.boxplot(x=df['bmi'])

"""Untuk bmi dapat dilihat bahwa terdapat beberapa data outlier dan bmi terendah 15, rata-rata bmi 30 dan bmi tertinggi 53."""

sns.boxplot(x=df['children'])

"""Jika dilihat pada visualiasi fitur anak. Rata-rata jumlah anak 1 dan paling banyak 5 namun kebanyakan tidak memiliki anak.

###Univariate Analysis

**Kategorical**
"""

print(df['sex'].value_counts())
df['sex'].value_counts().plot(kind='bar', title='sex');

"""Jika dilihat hasil visualisasi dari jenis kelamin pada dataset, jumlah sample dari laki-laki dan perempuan hampir sama."""

print(df['smoker'].value_counts())
df['smoker'].value_counts().plot(kind='bar', title='smoker');

"""Jika dilihat dari hasil visualisasi, jumlah yang tidak merokok lebih banyak dibandingkan dengan jumlah perokok."""

print(df['region'].value_counts())
df['region'].value_counts().plot(kind='bar', title='region');

"""Jadi secara keseluruhan biaya asuransi tertinggi ada di region Southeast dan terendah di region Southwest.

**Numerik**
"""

df.hist(bins=50, figsize=(20,15))
plt.show()

"""Jika dilihat pada fitur `charges` atau lebih tepatnya label atau target, datanya distribusi condong kekanan (right-skewed).

###Multivariate Analysis
"""

# mengamati hubungan antar fitur numerik dengan fungsi pairplot()
sns.pairplot(df, diag_kind = 'kde')

"""Dapat diperhatikan fitur-fitur yang terdapat pada dataset yang digunakan terhadap target `charges` tidak memiliki hubungan linier.

Visualisasi terdahap tipe data `object` terhadap target.
"""

cat_features = df.select_dtypes(include='object').columns.to_list()
     
for col in cat_features:
  sns.catplot(x=col, y="charges", kind="bar", dodge=False, height = 4, aspect = 3,  data=df, palette="Set3")
  plt.title("Rata-rata 'charges' Relatif terhadap - {}".format(col))

"""Jika dilihat 
* Faktor pada fitur sex tidak berpengaruh jauh.
* Faktor perokok berpengaruh terhadap biaya.
* Region southeast dengan charges yang dibayar tinggi.

Mempertimbangkan faktor-faktor tertentu (sex, smoker, children) mari kita lihat bagaimana perubahannya berdasarkan region.
"""

f, ax = plt.subplots(1, 1, figsize=(12, 8))
ax = sns.barplot(x='region', y='charges', hue='sex', data=df, palette='cool')

f, ax = plt.subplots(1,1, figsize=(12,8))
ax = sns.barplot(x = 'region', y = 'charges',
                 hue='smoker', data=df, palette='Reds_r')

f, ax = plt.subplots(1, 1, figsize=(12, 8))
ax = sns.barplot(x='region', y='charges', hue='children', data=df, palette='Set1')

"""Seperti yang bisa dilihat dari barplots ini biaya `charges` tertinggi akibat merokok masih di Southeast tetapi terendah di Northeast. Orang-orang di Southwest umumnya merokok lebih banyak daripada orang-orang di Northeast tetapi orang-orang di Northeast memiliki biaya `charges` lebih tinggi berdasarkan jenis kelamin `sex` daripada di Southwest dan Northwest secara keseluruhan dan orang-orang dengan memiliki anak cenderung memiliki biaya `charges` medis yang lebih tinggi secara keseluruhan juga.

Sekarang mari kita analisa biaya pengobatan menurut age, bmi dan children menurut faktor smoker.
"""

ax = sns.lmplot(x = 'age', y = 'charges', data=df, hue='smoker', palette='Set1')
ax = sns.lmplot(x = 'bmi', y = 'charges', data=df, hue='smoker', palette='Set2')
ax = sns.lmplot(x = 'children', y = 'charges', data=df, hue='smoker', palette='Set3')

"""Merokok memiliki dampak tertinggi pada biaya medis, meskipun biayanya meningkat seiring bertambahnya usia, bmi, dan jumlah anak-anak.

## Data Preparation

**Konversi Dataset**

Seperti yang telah diketahui data dari fitur sex, smoker dan region berupa kategorikal, maka perlu melakukan konversi data kategorikal ke data numerik agar dapat diolah. Sebelum diubah ke numerik maka perlu di konversi ke tipe data kategorikal terlebih dahulu. Untuk itu bisa menggunakan `astype` untuk mengkonversikan tipe data.
"""

##konversi tipe data object ke categorical
df[['sex', 'smoker', 'region']] = df[['sex', 'smoker', 'region']].astype('category')
df.dtypes

"""Dapat dilihat tipe data yang sebelumnya object telah berhasil dikonversikan ke category dengan menggunakan `dtypes`

**One Hot Encoding**

Selanjutnya melakukan one hot encoding dengan menggunakan `one hot encoding`.
One hot encoding mengubah setiap nilai dalam kolom menjadi kolom baru yang bernilai 0 atau 1.
"""

#preprocessing
#Convert kolom
#Karena pada kolom sex,smoker dan region berupa variabel text/categorial maka harus dilakukan kategorisasi atau encode

#kolom smoker
df = pd.concat([df, pd.get_dummies(df['smoker'], prefix='smoker')],axis=1)
#kolom sex
df = pd.concat([df, pd.get_dummies(df['sex'], prefix='sex')],axis=1)
#kolom region
df = pd.concat([df, pd.get_dummies(df['region'], prefix='region')],axis=1)
df.drop(['smoker','sex','region'], axis=1, inplace=True)

df.dtypes

df.head()

"""**Matrik Korelasi**

Menggunakan fungsi yang telah disediakan oleh seaborn untuk melihat korelasi antar variabel atau fitur. Lebih tepatnya mengecek korelasi fitur terdahap label atau target.
"""

plt.figure(figsize=(10, 8))
sns.heatmap(data=df.corr(), annot=True, cmap='cool', linewidths=0.5, )
plt.title("Correlation Matrix", size=20)

"""Jika dilihat hasil visualisasinya maka tidak ada korelasi kecuali `smoker`.

**Train-Test-Split**

Membagi dataset menjadi data latih (train) dan data uji (test) merupakan hal yang harus dilakukan sebelum membuat model. Mempertahankan sebagian data yang ada untuk menguji seberapa baik generalisasi model terhadap data baru.
"""

X = df.drop(['charges'], axis=1)
y = df['charges']

"""Membagi dataset dengan 80:20. Jadi 80% untuk data latih dan 20% data uji dengan `random_state = 0` agar data yang dibagi tidak teracak."""

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

"""Perlu menskalakan kolom-kolom yang dibutuhkan. Perbedaan skala dapat menyebabkan kendala dengan estimator `euclidean distance`.

StandardScaler menghilangkan mean (terpusat pada 0) dan menskalakan ke variansi (deviasi standar = 1), dengan asumsi data terdistribusi normal (gauss) untuk semua fitur.
"""

# feature scaling
ss = StandardScaler()
X_train = ss.fit_transform(X_train)
X_test = ss.fit_transform(X_test)

"""# Modelling

**Fungsi Evaluasi Model**

Dibuat sebuah fungsi evaluasi model untuk menghasilkan output berupa metric MSE, RMSE, dan R2. Fungsi evaluasi model ini akan digunakan dalam mengevaluasi beberapa model yang akan digunakan. 

Output yang dihasilkan pada fungsi evaluasi model berupa metric dari hasil training dan validasi model.
"""

def evaluate_model(model,X_train=X_train, y_train=y_train, X_test=X_test, y_test=y_test,print_metric=True):
  y_pred_train, y_pred_test = model.predict(X_train), model.predict(X_test)
  mse_train = mean_squared_error(y_train, y_pred_train)
  mse_test = mean_squared_error(y_test, y_pred_test)
  rmse_train, rmse_test = np.sqrt(mse_train), np.sqrt(mse_test)
  r2_train, r2_test = r2_score(y_train, y_pred_train), r2_score(y_test, y_pred_test)
  if print_metric:
        print(f'''On training set:\nMSE: {mse_train}    RMSE: {rmse_train}    r2: {r2_train}\n
=====================================\nOn test set:\nMSE: {mse_test}    RMSE: {rmse_test}    r2: {r2_test}''')
  return mse_train, rmse_train, r2_train, mse_test, rmse_test, r2_test

"""Pada tahap ini, akan dikembangkan model machine learning dengan tiga algoritma. Kemudian akan mengevaluasi performa masing-masing algoritma dan menentukan algoritma mana yang memberikan hasil prediksi terbaik. Selain itu menggunakan fine tuning untuk mencari paramater yang cocok dalam pengembangan model.

Dalam kasus kali ini, model harus menggunakan algoritma regresi karena hasil prediksi yang diinginkan adalah memprediksi nilai dari setiap data yang baru. 

Algoritma yang digunakan, yaitu:
* Linear Regression
* Polynomial Regression
* Random Forest

**Model Linear Regression**

Model pertama yang dibuat adalah linear regression. 
Melakukan training pada model dengan menggunakan data latih (x_train dan y_train) dan selanjut menampilkan hasil evaluasi training model.
"""

lin_reg = LinearRegression()
lin_reg.fit(X_train, y_train)

_ ,_ ,_ ,mse, rmse, r2 = evaluate_model(lin_reg)

"""Jika dilihat dari hasil training menggunakan model linear regression, metric atau lebih tepatnya nilai `R2` menghasilkan 0.73 yang artinya jika nilai r2 semakin mendekati 1 maka semakin baik model yang dihasilkan dan nilai `RMSE` rendah menunjukkan bahwa variasi nilai yang dihasilkan oleh suatu model prakiraan mendekati variasi nilai obeservasinya. RMSE menghitung seberapa berbedanya seperangkat nilai. Semakin kecil nilai RMSE, semakin dekat nilai yang diprediksi dan diamati. Begitu juga dengan nilai `MSE`.

Kode dibawah digunakan untuk menyimpan evaluasi model data validasi (data uji) yang akan dibandingkan dengan model lainnya berdasarkan metrik MSE, RMSE dan R2.
"""

results_df = pd.DataFrame([['Linear Regression', mse,rmse,r2]], columns=['Model', 'MSE', 'RMSE', 'R^2'])
results_df

"""**Polynomial Regression**

Menerapkan konsep fine tuning untuk mencari parameter yang cocok (fit) untuk model.
"""

degree = [2,3,4,5]
results = []
for d in degree:
    poly_feat = PolynomialFeatures(degree=d)
    X_poly = poly_feat.fit_transform(X)
    Xp_train, Xp_test, yp_train, yp_test = train_test_split(X_poly, y, test_size=0.2, random_state=0)
    poly_reg = LinearRegression()
    poly_reg.fit(Xp_train, yp_train)

    mse_train, rmse_train, r2_train, mse_test, rmse_test, r2_test = evaluate_model(poly_reg, Xp_train, yp_train, Xp_test, yp_test,print_metric=False)
    
    results.append([d, mse_train, rmse_train, r2_train, mse_test, rmse_test, r2_test])
poly_results = pd.DataFrame(results, columns=['degree', 'mse_train', 'rmse_train', 'r2_train', 'mse_test', 'rmse_test', 'r2_test'])
poly_results

"""Jika dilihat dari hasil fine tuning maka `degree` yang akan digunakan adalah `degree 3` (derajat 3) karena derajat yang lebih tinggi menyebabkan overfitting pada training set.

Membuat model polynomial regression dengan degree 3.
"""

#memilih degree 3 
polynomial_model = PolynomialFeatures(degree=3)
polynomial_model = LinearRegression()
polynomial_model.fit(Xp_train, yp_train)
mse_train, rmse_train, r2_train, mse_test, rmse_test, r2_test = evaluate_model(polynomial_model, Xp_train, yp_train, Xp_test, yp_test,print_metric=True)

"""Simpan ke dataframe `result_model`"""

results_model = pd.DataFrame([['Polynomial Regression', *poly_results[poly_results['degree']==2].iloc[:,4:].values[0]]], columns=['Model', 'MSE', 'RMSE', 'R^2'])
results_df = results_df.append(results_model, ignore_index=True)
results_df

"""**Random Forest**

Menerapkan konsep fine tuning untuk mencari parameter yang cocok (fit) untuk model. Adapun parameter yang dicari adalah `n_estimators` dan `max_leaf_nodes`.
"""

n_estimators = [10, 30, 100, 300, 1000, 3000]
max_leaf_nodes = [10, 30, 50, 75, 100]
results = []
for est in n_estimators:
    for n_nodes in max_leaf_nodes:
        for_reg = RandomForestRegressor(n_estimators=est, max_leaf_nodes=n_nodes, random_state=0)
        for_reg.fit(X_train, y_train)
        mse_train, rmse_train, r2_train, mse_test, rmse_test, r2_test = evaluate_model(for_reg,print_metric=False)
        results.append([est, n_nodes, mse_train, rmse_train, r2_train, mse_test, rmse_test, r2_test])
for_results_df = pd.DataFrame(results, columns=['n_estimators', 'n_nodes', 'mse_train', 'rmse_train', 'r2_train', 'mse_test', 'rmse_test', 'r2_test'])
for_results_df

"""Mencari nilai maksimum R2 dari hasil fine tuning. """

max_r2 = max(for_results_df['r2_test'])
for_results_df[for_results_df['r2_test']==max_r2]

"""Mencari nilai minimum R2 dari hasil fine tuning.

"""

min_rmse = min(for_results_df['rmse_test'])
for_results_df[for_results_df['rmse_test']==min_rmse]

"""Maka didapatkan parameter yang cocok untuk model Random Forest adalah `n_estimators = 3000` dan `max_leaf_nodes = 10`"""

#memilih estimator 3000 and nodes 10
randomforest_model = RandomForestRegressor(n_estimators=3000, max_leaf_nodes=10, random_state=0)
randomforest_model.fit(X_train, y_train)
mse_train, rmse_train, r2_train, mse_test, rmse_test, r2_test = evaluate_model(randomforest_model,print_metric=True)

results_model_2 = pd.DataFrame([['Random Forest', *for_results_df[for_results_df['r2_test']==max_r2].iloc[:,5:].values[0]]], columns=['Model', 'MSE', 'RMSE', 'R^2'])
results_df = results_df.append(results_model_2, ignore_index=True)
results_df

"""Dapat dilihat bahwa model Random Forest menghasilkan nilai R2 tertinggi dan juga menghasilkan nilai MSE maupun nilai RMSE yang rendah.

## Evaluation

Model yang digunakan adalah regressi, maka untuk metrik yang digunakan untuk melakukan evaluasi model, yaitu:
* Mean Squared Error (MSE)
* Root Mean Squared Error (RMSE)
* R2

**Mean Squared Error (MSE)** 

Mean Squared Error (MSE) adalah Rata-rata Kesalahan kuadrat diantara nilai aktual dan nilai prediksi. Metode Mean Squared Error secara umum digunakan untuk mengecek estimasi berapa nilai kesalahan pada prediksi. Nilai Mean Squared Error yang rendah atau nilai mean squared error mendekati nol menunjukkan bahwa hasil prediksi sesuai dengan data aktual dan bisa dijadikan untuk perhitungan prediksi di periode mendatang. Metode Mean Squared Error biasanya digunakan untuk mengevaluasi metode pengukuran dengan model regressi.

Kelebihan MSE yaitu sederhana dalam perhitungan. Sedangkan kelemahan yang dimiliki MSE adalah akurasi hasil prediksi sangat kecil karena tidak memperhatikan apakah hasil prediksi lebih besar atau lebih kecil dibandingkan kenyataannya


<img src="https://lindevs.com/wp-content/uploads/2020/10/formula_to_calculate_mse.png" width="200">

Dimana,
* n = jumlah dataset
* yi = nilai sebenarnya
* ??i = nilai prediksi

Untuk menerapkannya ke dalam kode ada 2 cara:
1. Menggunakan library dari sklearn
Dapat menggunakan secara langsung dari library sklearn untuk mendapatkan nilai MSE dengan cara:
* Load library `from sklearn.metrics import mean_squared_error`
* Tentukan nilai Y (nilai sebenarnya) dan nilai Y' (nilai prediksi).
* Memanggil fungsi `mean_squared_error(Y_true,Y_pred)` yang dimana menerima paramater input Y_true sebagai nilai sebenarnya dan Y_pred sebagai nilai prediksi. 
2. Menggunakan library numpy
* Load library `import numpy as np`
* Menentukan nilai nilai sebenarnya dan nilai prediksi.
* Memanggil fungsi `np.square(np.subtract(Y_true,Y_pred)).mean()`. 
Dimana,
 * `np.square` merupakan fungsi kuadrat dari library numpy.
 * `np.substract`merupakan fungsi pengurangan dari library numpy.

**Root Mean Squared Error (RMSE)**

Root Mean Squared Error (RMSE) merupakan salah satu cara untuk mengevaluasi model regresi dengan mengukur tingkat akurasi hasil perkiraan suatu model. RMSE dihitung dengan mengkuadratkan error (prediksi ??? observasi) dibagi dengan jumlah data (= rata-rata), lalu diakarkan.

Nilai RMSE rendah menunjukkan bahwa variasi nilai yang dihasilkan oleh suatu model prakiraan mendekati variasi nilai obeservasinya. RMSE menghitung seberapa berbedanya seperangkat nilai. Semakin kecil nilai RMSE, semakin dekat nilai yang diprediksi dan diamati.

Kelebihan dari RMSE yaitu memiliki tingkat sensitivitas yang cukup tinggi. Sedangkan kekurangannya RMSE tidak menggambarkan kesalahan rata-rata saja namun memiliki implikasi lain yang lebih sulit untuk diurai dan dipahami.

<img src="https://programmerah.com/wp-content/uploads/2020/11/20190714113817886.png" width="200">

Dimana,
* n = jumlah dataset
* yi = nilai sebenarnya
* ??i = nilai prediksi

Untuk menerapkannya ke dalam kode maka dapat:
1. Membuat fungsi menghitung mse
2. Menggunakan fungsi akar dari library numpy dan menggunakan hasil dari menghitung mse `np.sqrt(mse)`. Secara sederhana jika dilihat rumus rmse hanyalah penambahan akar dari rumus mse.

**R Squared (R2)**

R squared merupakan angka yang berkisar antara 0 sampai 1 yang mengindikasikan besarnya kombinasi variabel independen secara bersama ??? sama mempengaruhi nilai variabel dependen. Semakin mendekati angka satu, model yang dikeluarkan oleh regresi tersebut akan semakin baik.

Jika kita perhatikan rumus R squared dibawah sangat dipengaruhi oleh nilai Y prediksi atau nilai Y dari hasil rumus dengan nilai Y aktual. Kenyataan yang sering muncul adalah nilai R squared akan semakin membaik (nilainya akan terus mendekati nilai 1) jika kita menambah variabel. Semakin banyak jumlah variabel yang menentukan nilai Y prediksi, maka nilai SSR akan semakin besar yang berakibat pada besarnya nilai R squared.

Sifat R-squared yang akan semakin baik jika menambah variabel inilah yang menjadi kelemahan dari R squared itu sendiri. Semakin banyak variabel independen yang digunakan maka akan semakin banyak ???noise??? dalam model tersebut dan ini tidak dapat dijelaskan oleh R squared.

<img src="https://miro.medium.com/max/2812/1*_HbrAW-tMRBli6ASD5Bttw.png" width="200">

Dimana, 
* SSRes : Kuadrat dari selisih nilai Y prediksi dengan nilai rata-rata Y  = ??? (Ypred ??? Yrata-rata)??
* SSTotal : Kuadrat dari selisih nilai Y aktual dengan nilai rata-rata Y =  ??? (Yaktual ??? Yrata-rata)??

Untuk menerapkannya ke dalam kode maka dapat menggunakan secara langsung dari library sklearn untuk mendapatkan nilai R2 dengan cara:
* Load library `from sklearn.metrics import r2_score`.
* Tentukan nilai Y (nilai sebenarnya) dan nilai Y' (nilai prediksi).
* Memanggil fungsi `r2_score(Y_true,Y_pred)` yang dimana menerima paramater input Y_true sebagai nilai sebenarnya dan Y_pred sebagai nilai prediksi.

**Visualisasi Metrik**

**Metrik R2**
"""

sns.set(rc = {'figure.figsize':(10,6)})
sns.set_palette('Set2')
sns.set_style("whitegrid")
sns.barplot(x='R^2', y='Model', data=results_df)
plt.title('R^2 for each model')
plt.show()

"""Jika dilihat hasil visualisasi perbandingan R2, maka pada model random forest menghasilkan nilai R2 yang paling mendekati 1 dibandingkan dengan kedua model yang digunakan.

**Metrik RMSE**
"""

sns.barplot(x='RMSE', y='Model', data=results_df)
plt.title('RMSE for each model')
plt.show()

"""Untuk memastikan lebih lanjut maka dicoba untuk melakukan visualisasi RMSE yang dimana hasil dari RMSE  model random forest menghasilkan nilai yang kecil dibandingkan dengan kedua model lainnya dan ini membuktikan bahwa model random forest adalah model yang cocok untuk digunakan dalam kasus prediksi biaya asuransi.

**Validasi Fitur**
"""

print('Feature importance ranking\n\n')
importances = for_reg.feature_importances_
std = np.std([tree.feature_importances_ for tree in for_reg.estimators_],axis=0)
indices = np.argsort(importances)[::-1]
variables = ['age', 'bmi', 'children','smoker_no','smoker_yes','sex_female','sex_male','region_northeast','region_northwest','region_southeast','region_southwest']
importance_list = []
for f in range(X.shape[1]):
    variable = variables[indices[f]]
    importance_list.append(variable)
    print("%d.%s(%f)" % (f + 1, variable, importances[indices[f]]))

# Plot the feature importances of the forest
plt.figure()
plt.title("Feature importances")
plt.bar(importance_list, importances[indices],
       color="y", yerr=std[indices], align="center")

"""Jika dilihat dari hasil visualisasi diatas maka dapat ditarik sebuah kesimpulan bahwa fitur yang mempengaruhi biaya asuransi adalah `smoker, bmi dan age`. Selain dari fitur yang disebutkan, sangat kecil kemungkinan dalam mempengaruhi biaya asuransi yang harus dibayarkan.

**Prediksi**
"""

#Predicting the charges
y_test_pred_poly = polynomial_model.predict(Xp_test)
y_test_pred_for = randomforest_model.predict(X_test)
y_test_pred_lin = lin_reg.predict(X_test)
#Comparing the actual output values with the predicted values
df = pd.DataFrame({'Actual': y_test, 'Predicted Polynomial': y_test_pred_poly,'Predicted Random Forest': y_test_pred_for,'Predicted Linear Regression': y_test_pred_lin})
df

"""Hasil dari komparasi dari beberapa model yang digunakan, terbukti bahwa model Random Forest paling mendekati nilai sebenarnya (nilai aktual) sehingga model Random forestlah yang bisa dikatakan cocok dipakai."""
