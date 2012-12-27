import threading

def worker():
    print "worker"
    return

threads = []

for i in range(0, 100):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()