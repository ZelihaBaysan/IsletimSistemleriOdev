"""
THREAD vs PROCESS KARŞILAŞTIRMASI
--------------------------------
Bu uygulama, aynı görevin thread ve process
kullanılarak nasıl farklı şekillerde çalıştığını
göstermek için tasarlanmıştır.

Slayttaki örnekten farklı olarak:
- Aynı işi yapan görevler kullanılmıştır
- Davranış ve çıktı üzerinden fark gözlemlenir
"""

import threading
import multiprocessing
import time
import os


# Ortak görev
def ortak_gorev(ad):
    """
    CPU + zaman kullanan basit bir görev
    """
    for i in range(3):
        print(f"{ad} | PID: {os.getpid()} | Adım: {i}")
        time.sleep(0.4)


# -------------------------------
# THREAD İLE ÇALIŞMA
# -------------------------------
def thread_ile():
    print("\n[THREAD İLE ÇALIŞMA BAŞLADI]")
    start = time.time()

    t1 = threading.Thread(target=ortak_gorev, args=("Thread-1",))
    t2 = threading.Thread(target=ortak_gorev, args=("Thread-2",))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(f"[THREAD BİTTİ] Süre: {time.time() - start:.2f} sn")


# -------------------------------
# PROCESS İLE ÇALIŞMA
# -------------------------------
def process_ile():
    print("\n[PROCESS İLE ÇALIŞMA BAŞLADI]")
    start = time.time()

    p1 = multiprocessing.Process(target=ortak_gorev, args=("Process-1",))
    p2 = multiprocessing.Process(target=ortak_gorev, args=("Process-2",))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print(f"[PROCESS BİTTİ] Süre: {time.time() - start:.2f} sn")


# -------------------------------
# ANA AKIŞ
# -------------------------------
if __name__ == "__main__":
    thread_ile()
    process_ile()
