# IsletimSistemleriOdev# İşletim Sistemleri – 10. Hafta Uygulamaları

Bu repository, İşletim Sistemleri dersi 10. hafta kapsamında anlatılan  
**çoklu programlama**, **çoklu işlemci** ve **Amdahl Yasası** kavramlarının  
uygulamalı ve karşılaştırmalı örneklerini içermektedir.

Kodlar, ders slaytlarındaki kavramları temel almakla birlikte,
birebir kopya olmadan, özgün senaryolar üzerinden geliştirilmiştir.

---

## İçerik

- Çoklu Programlama (Thread tabanlı çalışma)
- Çoklu İşlemci (Process tabanlı çalışma)
- Thread ve Process karşılaştırması (tek uygulama içinde)
- Amdahl Yasası ile teorik hızlanma hesabı

---

## 1. Çoklu Programlama (Multiprogramming)

**Dosya:** `multiprogramming.py`

Bu uygulamada, tek işlemcili bir sistemde birden fazla işin
**zaman paylaşımlı** olarak nasıl yürütüldüğü gösterilmiştir.

### Özellikler
- `threading` kütüphanesi kullanılmıştır
- Aynı process içinde birden fazla thread çalışır
- Gerçek paralellik yoktur, eşzamanlılık (concurrency) vardır
- Çıktılar karışık şekilde gözlemlenir

---

## 2. Çoklu İşlemci (Multiprocessing)

**Dosya:** `multiprocessing_app.py`

Bu uygulamada, görevlerin farklı işlemcilerde (çekirdeklerde)
**gerçek paralel** olarak çalışması gösterilmiştir.

### Özellikler
- `multiprocessing` kütüphanesi kullanılmıştır
- Her process farklı PID ile çalışır
- Ayrı bellek alanları kullanılır
- Paralel çalışma net şekilde gözlemlenir

---

## 3. Thread ve Process Karşılaştırması

**Dosya:** `task_comparison.py`

Bu uygulama, çoklu programlama ve çoklu işlemci yaklaşımlarını
**aynı görev üzerinden** karşılaştırmak amacıyla geliştirilmiştir.

Slayttaki örneklerden farklı olarak:
- Aynı işi yapan görevler kullanılmıştır
- Farklar sadece ID üzerinden değil, **davranış ve süre** üzerinden incelenmiştir

### Karşılaştırma Mantığı
- Aynı görev önce thread’ler ile çalıştırılır
- Ardından aynı görev process’ler ile çalıştırılır
- PID, çıktı düzeni ve çalışma süresi gözlemlenir

### Gözlemler
- Thread kullanımında tüm görevler aynı PID altında çalışır
- Process kullanımında her görev farklı PID’ye sahiptir
- Process tabanlı yaklaşımda daha net paralellik gözlemlenir

---

## 4. Amdahl Yasası

**Dosya:** `amdahl_law.py`

Bu uygulama, Amdahl Yasası kullanılarak paralelleştirmenin
teorik sınırlarını hesaplamayı amaçlamaktadır.

### Amdahl Yasası
Bir programın seri çalışan kısmı, işlemci sayısı artsa bile
elde edilebilecek maksimum hızlanmayı sınırlar.

### Formül

Speedup(N) = 1 / ( S + (1 - S) / N )


- `S` : Seri çalışan kısmın oranı
- `N` : İşlemci çekirdeği sayısı

Kullanıcıdan alınan değerlere göre teorik hızlanma hesaplanır.

---

## Dosya Yapısı

.
├── multiprogramming.py
├── multiprocessing_app.py
├── task_comparison.py
├── amdahl_law.py
└── README.md


---

## Çalıştırma

Python 3 yüklü bir sistemde aşağıdaki komutlar ile çalıştırılabilir:

```bash
python multiprogramming.py
python multiprocessing_app.py
python task_comparison.py
python amdahl_law.py

Amaç ve Değerlendirme

Bu çalışmaların amacı, işletim sistemlerinde:

    eşzamanlılık ve paralellik farkını,

    thread ve process kavramlarını,

    paralelleştirmenin teorik sınırlarını

uygulamalı olarak göstermek ve kavramların
yalnızca teorik değil, davranışsal olarak da anlaşılmasını sağlamaktır.