import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt
from core.matrix_utils import koordinat_ve_mesafe_olustur
from core.ant_algorithm import run_aco

st.set_page_config(page_title="Konya ACO Rota", layout="wide")
st.title("🚚 Konya Yurtları Dağıtım Optimizasyonu")

# تحديد المسارات للحفظ
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
FIGURE_PATH = os.path.join(BASE_PATH, "figure")
OUTPUT_PATH = os.path.join(BASE_PATH, "outputs")

# التأكد من وجود المجلدات
os.makedirs(FIGURE_PATH, exist_ok=True)
os.makedirs(OUTPUT_PATH, exist_ok=True)

# --- إعدادات الشريط الجانبي (Sidebar) ---
st.sidebar.header("⚙️ Parametreler")
api_key = st.sidebar.text_input("Google Maps API Key", type="password")

# إضافة المنزلقات للتحكم في الخوارزمية
ants_count = st.sidebar.slider("Karınca Sayısı ", min_value=5, max_value=50, value=15)
iterations_count = st.sidebar.slider("İterasyon Sayısı ", min_value=10, max_value=100, value=30)

csv_path = os.path.join(BASE_PATH, "data", "konya_yurtlar.csv")

if os.path.exists(csv_path):
    df_names = pd.read_csv(csv_path)
    yurt_isimleri = df_names['name'].tolist()
    
    st.sidebar.info(f"Sistemde {len(yurt_isimleri)} yurt kayıtlı.")

    if st.button("🚀 Optimizasyonu Başlat"):
        if not api_key:
            st.error("Lütfen API anahtarınızı giriniz!")
        else:
            with st.spinner("Veriler alınıyor ve sonuçlar kaydediliyor..."):
                
                coords, dist_matrix = koordinat_ve_mesafe_olustur(yurt_isimleri, api_key)
                
                
                path, best_dist, history = run_aco(
                    dist_matrix, 
                    karinca_sayisi=ants_count, 
                    iterasyon_sayisi=iterations_count
                )
                
             
                col1, col2 = st.columns(2)
                with col1:
                    st.success(f"En Kısa Mesafe: {best_dist:.2f} km")
                    map_df = pd.DataFrame(coords, columns=['lat', 'lon'])
                    st.map(map_df)
                
                with col2:
                    st.write("📊 Yakınsama Grafiği")
                    fig, ax = plt.subplots()
                    ax.plot(history, color='green')
                    ax.set_title("ACO Performansı")
                    ax.set_xlabel("İterasyon")
                    ax.set_ylabel("Mesafe (km)")
                    st.pyplot(fig)
                    
                    
                    fig.savefig(os.path.join(FIGURE_PATH, "yakinsama_egrisi.png"))
                
              
                ordered_names = [yurt_isimleri[i] for i in path]
                result_text = f"En İyi Mesafe: {best_dist:.2f} km\nRota:\n" + " -> ".join(ordered_names)
                
                with open(os.path.join(OUTPUT_PATH, "sonuclar.txt"), "w", encoding="utf-8") as f:
                    f.write(result_text)
                
                st.write("🛣️ **Optimize Edilmiş Rota:**")
                st.write(" ➡️ ".join(ordered_names))
                st.balloons()
                st.info(f"✅ Sonuçlar kaydedildi: {FIGURE_PATH}")
else:
    st.error("CSV dosyası bulunamadı! Lütfen 'data' klasörünü kontrol edin.")