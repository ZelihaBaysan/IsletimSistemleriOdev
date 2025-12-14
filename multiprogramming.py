"""
ÇOKLU PROGRAMLAMA (MULTIPROGRAMMING) UYGULAMASI

Amaç:
Tek işlemcili bir sistemde, birden fazla programın
zaman paylaşımlı (time-sharing) olarak çalışmasını simüle etmek.

Bu uygulamada:
- Thread (iş parçacığı) kullanılmıştır
- Aynı process içinde birden fazla thread çalışır
- Gerçek paralellik yoktur, eşzamanlılık (concurrency) vardır
"""

import threading
import time

def program(name):
    """
    Her bir thread tarafından çalıştırılan fonksiyon.
    İşletim sisteminin CPU’yu sırayla thread’lere vermesini
    simüle etmek için sleep() kullanılmıştır.
    """
    for i in range(5):
        print(f"{name} çalışıyor: {i}")
        time.sleep(0.5)

# İki farklı thread oluşturuluyor
t1 = threading.Thread(target=program, args=("Program 1",))
t2 = threading.Thread(target=program, args=("Program 2",))

# Thread’ler başlatılıyor
t1.start()
t2.start()

# Ana program, thread’lerin bitmesini bekler
t1.join()
t2.join()
