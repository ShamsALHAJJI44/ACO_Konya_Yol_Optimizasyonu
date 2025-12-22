import numpy as np

def run_aco(mesafe, karinca_sayisi=10, iterasyon_sayisi=30, alpha=1.0, beta=2.0, buharlasma=0.5):
    n = len(mesafe)
    feromon = np.ones((n, n)) * 0.1
    cekicilik = 1.0 / (mesafe + 1e-6)
    en_iyi_yol = None
    en_kisa_mesafe = float('inf')
    gecmis = []

    for _ in range(iterasyon_sayisi):
        yollar = []
        for k in range(karinca_sayisi):
            yol = [0]
            ziyaret = {0}
            while len(yol) < n:
                su_an = yol[-1]
                adaylar = list(set(range(n)) - ziyaret)
                pay = (feromon[su_an, adaylar]**alpha) * (cekicilik[su_an, adaylar]**beta)
                probs = pay / pay.sum()
                sonraki = np.random.choice(adaylar, p=probs)
                yol.append(sonraki)
                ziyaret.add(sonraki)
            yol.append(0)
            
            d = sum(mesafe[yol[i], yol[i+1]] for i in range(len(yol)-1))
            if d < en_kisa_mesafe:
                en_kisa_mesafe = d
                en_iyi_yol = yol
            yollar.append((yol, d))
            
        feromon *= (1 - buharlasma)
        for y, d in yollar:
            for i in range(len(y)-1):
                feromon[y[i], y[i+1]] += 1.0/d
        gecmis.append(en_kisa_mesafe)
    return en_iyi_yol, en_kisa_mesafe, gecmis
