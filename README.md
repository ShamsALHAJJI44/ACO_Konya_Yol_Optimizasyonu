#  Konya Öğrenci Yurtları Yemek Dağıtım Rota Optimizasyonu

Bu proje, Konya ilinde bulunan 20 farklı KYK öğrenci yurdu arasında en verimli yemek dağıtım rotasını oluşturmak için **Karınca Kolonisi Algoritması (ACO)** kullanılarak geliştirilmiştir.

##  Proje Senaryosu
Konya şehir merkezinden yola çıkan bir yemek dağıtım aracının, 20 farklı yurt noktasına en kısa mesafede uğraması hedeflenmektedir. Bu senaryo, gerçek dünya harita verilerini (Google Maps API) kullanarak lojistik maliyetleri ve zaman kaybını minimize etmeyi amaçlar.

##  Kullanılan Teknolojiler
* **Google Maps API:** Gerçek yol mesafeleri (Driving Distance) ve GPS koordinatları için.
* **Ant Colony Optimization (ACO):** Karmaşık rota problemlerini çözmek için kullanılan meta-sezgisel algoritma.
* **Streamlit:** Etkileşimli ve kullanıcı dostu web arayüzü.
* **Python:** Veri işleme, görselleştirme ve algoritma çekirdeği.

##  Proje Yapısı
Proje, akademik standartlara uygun olarak aşağıdaki klasör yapısında düzenlenmiştir:

* **core/**: Algoritma mantığı ve API yardımcı fonksiyonlarını içerir (`ant_algorithm.py`, `matrix_utils.py`).
* **data/**: Yurt isimlerinin bulunduğu veri setini içerir (`konya_yurtlar.csv`).
* **figure/**: Optimizasyon sürecine ait yakınsama grafiklerini saklar.
* **outputs/**: En iyi rota sıralamasını ve mesafe sonuçlarını içeren metin dosyalarını barındırır.
* **main.py**: Uygulamanın ana giriş noktası ve arayüz dosyası.
* **YemekDagitimi.ipynb**: Projenin tüm adımlarının açıklandığı analiz dosyası.

##  Kurulum ve Çalıştırma

1.  **Gereksinimleri Yükleyin:**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Uygulamayı Başlatın:**
    ```bash
    streamlit run main.py
    ```

3.  **Kullanım:**
    * Uygulama açıldığında sol taraftaki panelden **Google Maps API Key**'inizi girin.
    * Karınca sayısı ve İterasyon gibi parametreleri ayarlayın.
    * **"Optimizasyonu Başlat"** butonuna basarak en kısa rotayı ve haritayı görüntüleyin.

##  Örnek Sonuçlar
* **Toplam Yurt Sayısı:** 20
* **Hesaplanan En Kısa Mesafe:** ~89.59 km
* **Görselleştirme:** Google Maps üzerinden etkileşimli rota haritası ve performans grafiği.

---
**Hazırlayan:** [Shams AL HAJJI]
