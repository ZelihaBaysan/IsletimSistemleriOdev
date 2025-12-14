"""
ÇOKLU İŞLEMCİ (MULTIPROCESSING) UYGULAMASI

Amaç:
Birden fazla işlemcide (çekirdekte) görevlerin
gerçek paralel olarak çalışmasını göstermek.
"""

import multiprocessing
import time
import os


def program(name):
    """
    Her process tarafından çalıştırılan görev.
    """
    for i in range(5):
        print(f"{name} | PID: {os.getpid()} | Adım: {i}")
        time.sleep(0.5)


if __name__ == "__main__":
    # Windows için zorunlu güvenli başlatma
    multiprocessing.freeze_support()

    p1 = multiprocessing.Process(target=program, args=("Process 1",))
    p2 = multiprocessing.Process(target=program, args=("Process 2",))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
