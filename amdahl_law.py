"""
AMDHAL YASASI UYGULAMASI

Amaç:
Seri ve paralel bölümleri olan bir programda,
çekirdek sayısının teorik hızlanmaya etkisini hesaplamak.

Formül:
Speedup(N) = 1 / ( S + (1 - S) / N )

S : Seri çalışan kısmın oranı
N : İşlemci çekirdeği sayısı
"""

def amdahl_yasasi(S, N):
    """
    Amdahl Yasası formülünü uygulayarak
    teorik hızlanma oranını hesaplar.
    """
    return 1 / (S + (1 - S) / N)

# Kullanıcıdan değerler alınır
seri_oran = float(input("Seri kısım oranını giriniz (0-1): "))
cekirdek_sayisi = int(input("Çekirdek sayısını giriniz: "))

# Hızlanma hesaplanır
hizlanma = amdahl_yasasi(seri_oran, cekirdek_sayisi)

# Sonuç ekrana yazdırılır
print(f"Teorik hızlanma: {hizlanma:.2f} kat")
