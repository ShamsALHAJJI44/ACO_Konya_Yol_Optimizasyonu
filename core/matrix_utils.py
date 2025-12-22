import googlemaps
import numpy as np

def koordinat_ve_mesafe_olustur(sehir_isimleri, api_key):
    gmaps = googlemaps.Client(key=api_key)
    n = len(sehir_isimleri)
    
    # 1. Geocoding: تحويل الأسماء إلى إحداثيات (شرط أساسي في الواجب)
    koordinatlar = []
    for isim in sehir_isimleri:
        result = gmaps.geocode(f"{isim}, Konya, Turkey")
        if result:
            loc = result[0]['geometry']['location']
            koordinatlar.append((loc['lat'], loc['lng']))
        else:
            # إحداثيات افتراضية في حال لم يجد الموقع
            koordinatlar.append((37.8749, 32.4931))

    # 2. Distance Matrix: حساب مسافات القيادة (Driving Distance)
    mesafe_matrisi = np.zeros((n, n))
    
    # لتجنب خطأ MAX_ELEMENTS_EXCEEDED، نقوم بطلب المسافات لكل نقطة على حدة
    for i in range(n):
        # نطلب المسافات من النقطة الحالية (i) إلى جميع النقاط الأخرى
        # هذا الطلب يحتوي على 20 عنصر فقط، وهو ضمن الحد المسموح (100 عنصر)
        result = gmaps.distance_matrix(koordinatlar[i], koordinatlar, mode="driving")
        
        for j in range(n):
            if i == j:
                mesafe_matrisi[i][j] = np.inf
            else:
                # استخراج القيمة من نتيجة جوجل وتحويلها من متر إلى كيلومتر
                try:
                    dist_val = result['rows'][0]['elements'][j]['distance']['value']
                    mesafe_matrisi[i][j] = dist_val / 1000.0
                except (KeyError, IndexError):
                    # في حال فشل جلب مسافة محددة، نضع قيمة كبيرة جداً
                    mesafe_matrisi[i][j] = 9999.0 
                
    return koordinatlar, mesafe_matrisi