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
* Menggunakan feature importance. Feature importance mengacu pada teknik yang menetapkan score ke fitur input berdasarkan seberapa berguna fitur tersebut dalam memprediksi variabel target. Feature importance score memainkan peran penting dalam proyek pemodelan prediktif, termasuk memberikan wawasan tentang data, wawasan model, dan dasar untuk pengurangan dimensi dan pemilihan fitur yang dapat meningkatkan efisiensi dan efektivitas model prediktif pada masalah.

2. Untuk menghasilkan model machine learning yang dapat memprediksi seakurat mungkin, maka digunakan tiga algoritma regresi mengingat data yang digunakan berupa data regresi dan adapun algoritmanya yaitu, linear regression, polynomial regression dan random forest.
* **Linear regression** adalah suatu model statistik yang umum dan paling sederhana yang digunakan untuk Machine Learning untuk melakukan prediksi dengan cara supervised learning. Linear regression hanya bisa digunakan untuk data yang bersifat interval dan ratio yang biasanya bersifat diskrit dan kontinu, dan merupakan analisis bivariate dan multivariate. Linear regression digunakan untuk Prediksi dengan mencari pola garis terbaik antara variable independent dan dependen. Kelebihan, mudah diimplementasikan dan digunakan untuk memprediksi nilai numerik/ continous /data jenis interval dan ratio. Sedangakan kekurangannya, cenderung mudah Overfitting dan tidak dapat digunakan bila relasi antara variabel independen dan dependen tidak linier atau korelasi variabel rendah 
* **Polynomial regression** seperti linear regression yang menggunakan hubungan antara variabel x dan y untuk menemukan cara terbaik untuk menarik garis melalui titik data. Polynomial regression merupakan regresi dengan fungsinya adalah kuadratik, di mana nilai variabel independen ada yang bernilai pangkat 1, pangkat 2, pangkat n dan seterusnya. Nilai pangkat 2 sering disebut dengan orde 2, pangkat 3 dengan orde 3 dan seterusnya. Penggunaan polinomial ketika ingin mencari hubungan antara 1 variabel dependen dengan 1 variabel independen. Jika hanya ingin mencari hubungan terhadap 1 variabel independen, kapan menggunakan simple dan kapan menggunakan polinomial? Jawabannya adalah dilihat seberapa fit model yang dibangun dengan data aslinya. Jika menggunakan simple linear sudah fit, maka cukup menggunakan model ini saja, namun jika tidak dan fungsinya tampak seperti fungsi polinomial (fungsi kuadratik) maka kita coba dekati dengan metode polinomial. Jika menggunakan simple dan polinomial tidak juga fit, maka hubungan antara keduanya bukanlah linear, sehingga harus menggunakan algoritma regresi non linear. 
* **Random forest** adalah salah satu algoritma supervised learning. Dapat digunakan untuk menyelesaikan masalah klasifikasi dan regresi. Random forest merupakan kombinasi dari masing – masing pohon (tree) dari model Decision Tree yang baik, dan kemudian dikombinasikan ke dalam satu model. Penggunaan tree yang semakin banyak akan mempengaruhi akurasi yang akan didapatkan menjadi lebih baik. Penentuan klasifikasi dengan random forest diambil berdasarkan hasil voting dari tree yang terbentuk. 
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
Dataset yang digunakan adalah [Medical Cost Personal Datasets](https://www.kaggle.com/mirichoi0218/insurance) yang dimana terdapat beberapa fitur atau variabel yang mempengaruhi berapa banyak biaya asuransi kesehatan yang harus dibayar. 

Dataset terdiri dari **1338** sampel tanpa missing value (Nan, Null) dengan fitur sebagai berikut:

* age: Usia penerima (int64). 
* sex: *Gender* penerima asuransi, *female*, *male* (object).
* bmi (*Body Mass Index*): Memberikan pemahaman tentang tubuh, berat badan yang relatif tinggi atau relatif rendah terhadap tinggi badan.  Indeks objektif berat badan (kg/m^2) menggunakan rasio tinggi terhadap berat badan, idealnya 18,5 hingga 24,9 (float64).
* children: Jumlah anak yang ditanggung oleh asuransi kesehatan atau jumlah tanggungan (int64).
* smoker: Perokok atau bukan perokok (object).
* region: Wilayah penerima di AS, *northeast*, *southeast*, *southwest*, *northwest* (object).
* charges: Biaya medis individu yang ditagih oleh asuransi kesehatan (float64).

Terdiri dari tipe data: 
* float64 sebanyak 2 fitur 
* int64 sebanyak 2 fitur 
* object sebanyak 3 fitur

Dilakukan Exploratory Data Analysis (EDA) untuk mendapatkan sebuah insight sekaligus untuk menjawab salah satu `Goals` yang ingin dicapai, dimana untuk mengetahui faktor-faktor apa saja yang mempengaruhi biaya asuransi. Adapun tahapan yang dilakukan, yaitu:
* Analisis Deskriptif

* Visualisasi Data ( Univariate dan Multivariate Analysis)

**Visualisasi Univariate**

Dari hasil visualisasi data univariate, didapatkan kesimpulan:
1. Jika dilihat hasil visualisasi dari jenis kelamin pada dataset, jumlah sample dari laki-laki dan perempuan hampir sama.
2. Jika dilihat dari hasil visualisasi, jumlah yang tidak merokok lebih banyak dibandingkan dengan jumlah perokok.
3. Jadi secara keseluruhan biaya asuransi tertinggi ada di region Southeast dan terendah di region Southwest.
4. Jika dilihat pada fitur `charges` atau lebih tepatnya label atau target, datanya distribusi condong kekanan (right-skewed).

**Visualisasi Multivariate**

1. Dapat diperhatikan fitur-fitur yang terdapat pada dataset yang digunakan terhadap target `charges` tidak memiliki hubungan linier. 
2. Jika dilihat 
   * Faktor pada fitur sex tidak berpengaruh jauh.
   * Faktor perokok berpengaruh terhadap biaya.
   * Region southeast dengan charges yang dibayar tinggi.
   * `Feature importance ranking` dari Random Forest untuk validasi faktor atau fitur penting terdahap biaya asuransi.

## Data Preparation
Teknik yang digunakan pada tahapan ini, yaitu:
1. LabelEncoder()
Label encoding mengubah setiap nilai dalam kolom menjadi angka yang berurutan.
Jika ambil sebuah contoh pada fitur `sex` nilai female = 0 dan male = 1. 
Seperti yang telah diketahui data dari fitur sex, smoker dan region berupa kategorikal, maka perlu melakukan konversi data kategorikal ke data numerik agar dapat diolah (encode). 
2. StandardScaler()
StandardScaler menghilangkan mean (terpusat pada 0) dan menskalakan ke variansi (deviasi standar = 1), dengan asumsi data terdistribusi normal (gauss) untuk semua fitur.
Perlu menskalakan kolom-kolom yang dibutuhkan. Perbedaan skala dapat menyebabkan kendala dengan estimator `euclidean distance`.
3. Train-Test-Split()
Membagi dataset menjadi data latih (train) dan data uji (test) merupakan hal yang harus dilakukan sebelum membuat model. Mempertahankan sebagian data yang ada untuk menguji seberapa baik generalisasi model terhadap data baru. 

## Modeling
Pada tahap ini, akan dikembangkan model machine learning dengan tiga algoritma. Kemudian akan mengevaluasi performa masing-masing algoritma dan menentukan algoritma mana yang memberikan hasil prediksi terbaik. Selain itu menggunakan fine tuning untuk mencari paramater yang cocok dalam pengembangan model.

Dalam kasus kali ini, model harus menggunakan algoritma regresi karena hasil prediksi yang diinginkan adalah memprediksi nilai dari setiap data yang baru. 

Algoritma yang digunakan, yaitu:
* Linear Regression
* Polynomial Regression
* Random Forest

**Metrik**

Hasil dari ketiga model, dapat dilihat dibawah ini:

Model | MSE | RMSE | R^2 
------ | ------ | ------|--------
0 | Linear Regression |	3.184593e+07 	5643.219749 | 0.799875 
1 | Polynomial Regression |	1.888866e+07 	4346.108309 | 0.881300
2 | Random Forest | 1.718343e+07 	4145.289931 | 0.892016

Dapat dilihat bahwa model Random Forest menghasilkan nilai R2 tertinggi dan juga menghasilkan nilai MSE maupun nilai RMSE yang rendah. 

**Hasil Prediksi**

Actual | Predicted Polynomial |	Predicted Random Forest |	Predicted Linear Regression
---|---|---|---
9724.53000 | 11892.0 |	12530.809502 |	11017.230479
8547.69130 | 10137.0 | 10882.959589 |	9787.530168
45702.02235 | 49484.0 |	44358.160419 |	37994.782118
12950.07120 | 13420.0 |	14259.887472 |	16122.778407
9644.25250 | 14624.0 | 11312.048041 |	6930.759230

Hasil dari komparasi dari beberapa model yang digunakan, terbukti bahwa model Random Forest paling mendekati nilai sebenarnya (nilai aktual) sehingga model Random forestlah yang bisa dikatakan cocok dipakai.

## Evaluation
Model yang digunakan adalah regressi, maka untuk metrik yang digunakan untuk melakukan evaluasi model, yaitu:
* Mean Squared Error (MSE)
* Root Mean Squared Error (RMSE)
* R2

**Mean Squared Error (MSE)** 

Mean Squared Error (MSE) adalah Rata-rata Kesalahan kuadrat diantara nilai aktual dan nilai prediksi. Metode Mean Squared Error secara umum digunakan untuk mengecek estimasi berapa nilai kesalahan pada prediksi. Nilai Mean Squared Error yang rendah atau nilai mean squared error mendekati nol menunjukkan bahwa hasil prediksi sesuai dengan data aktual dan bisa dijadikan untuk perhitungan prediksi di periode mendatang. Metode Mean Squared Error biasanya digunakan untuk mengevaluasi metode pengukuran dengan model regressi.

Kelebihan MSE yaitu sederhana dalam perhitungan. Sedangkan kelemahan yang dimiliki MSE adalah akurasi hasil prediksi sangat kecil karena tidak memperhatikan apakah hasil prediksi lebih besar atau lebih kecil dibandingkan kenyataannya

![MSE](https://lindevs.com/wp-content/uploads/2020/10/formula_to_calculate_mse.png)
<!-- <img src="https://lindevs.com/wp-content/uploads/2020/10/formula_to_calculate_mse.png" width="200"> -->

Dimana,
* n = jumlah dataset
* yi = nilai sebenarnya
* ŷi = nilai prediksi

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

Root Mean Squared Error (RMSE) merupakan salah satu cara untuk mengevaluasi model regresi dengan mengukur tingkat akurasi hasil perkiraan suatu model. RMSE dihitung dengan mengkuadratkan error (prediksi – observasi) dibagi dengan jumlah data (= rata-rata), lalu diakarkan.

Nilai RMSE rendah menunjukkan bahwa variasi nilai yang dihasilkan oleh suatu model prakiraan mendekati variasi nilai obeservasinya. RMSE menghitung seberapa berbedanya seperangkat nilai. Semakin kecil nilai RMSE, semakin dekat nilai yang diprediksi dan diamati.

Kelebihan dari RMSE yaitu memiliki tingkat sensitivitas yang cukup tinggi. Sedangkan kekurangannya RMSE tidak menggambarkan kesalahan rata-rata saja namun memiliki implikasi lain yang lebih sulit untuk diurai dan dipahami.

![RMSE](https://programmerah.com/wp-content/uploads/2020/11/20190714113817886.png)
<!-- <img src="https://programmerah.com/wp-content/uploads/2020/11/20190714113817886.png" width="200"> -->

Dimana,
* n = jumlah dataset
* yi = nilai sebenarnya
* ŷi = nilai prediksi

Untuk menerapkannya ke dalam kode maka dapat:
1. Membuat fungsi menghitung mse
2. Menggunakan fungsi akar dari library numpy dan menggunakan hasil dari menghitung mse `np.sqrt(mse)`. Secara sederhana jika dilihat rumus rmse hanyalah penambahan akar dari rumus mse.

**R Squared (R2)**

R squared merupakan angka yang berkisar antara 0 sampai 1 yang mengindikasikan besarnya kombinasi variabel independen secara bersama – sama mempengaruhi nilai variabel dependen. Semakin mendekati angka satu, model yang dikeluarkan oleh regresi tersebut akan semakin baik.

Jika kita perhatikan rumus R squared dibawah sangat dipengaruhi oleh nilai Y prediksi atau nilai Y dari hasil rumus dengan nilai Y aktual. Kenyataan yang sering muncul adalah nilai R squared akan semakin membaik (nilainya akan terus mendekati nilai 1) jika kita menambah variabel. Semakin banyak jumlah variabel yang menentukan nilai Y prediksi, maka nilai SSR akan semakin besar yang berakibat pada besarnya nilai R squared.

Sifat R-squared yang akan semakin baik jika menambah variabel inilah yang menjadi kelemahan dari R squared itu sendiri. Semakin banyak variabel independen yang digunakan maka akan semakin banyak “noise” dalam model tersebut dan ini tidak dapat dijelaskan oleh R squared.

![R2](https://miro.medium.com/max/2812/1*_HbrAW-tMRBli6ASD5Bttw.png)
<!-- <img src="https://miro.medium.com/max/2812/1*_HbrAW-tMRBli6ASD5Bttw.png" width="200"> -->

Dimana, 
* SSRes : Kuadrat dari selisih nilai Y prediksi dengan nilai rata-rata Y  = ∑ (Ypred – Yrata-rata)²
* SSTotal : Kuadrat dari selisih nilai Y aktual dengan nilai rata-rata Y =  ∑ (Yaktual – Yrata-rata)²

Untuk menerapkannya ke dalam kode maka dapat menggunakan secara langsung dari library sklearn untuk mendapatkan nilai R2 dengan cara:
* Load library `from sklearn.metrics import r2_score`.
* Tentukan nilai Y (nilai sebenarnya) dan nilai Y' (nilai prediksi).
* Memanggil fungsi `r2_score(Y_true,Y_pred)` yang dimana menerima paramater input Y_true sebagai nilai sebenarnya dan Y_pred sebagai nilai prediksi. 
