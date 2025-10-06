import threading, time, pygame, sys, traceback

pygame.init()
screen = pygame.display.set_mode((320,240))
clock = pygame.time.Clock()

stop = threading.Event()

def safe_run(name, fn):
    try:
        fn()
    except Exception:
        print(f"Exception in {name}:")
        traceback.print_exc()

def worker_a():
    i = 0
    while not stop.is_set():
        i += 1
        print("A tick", i)
        time.sleep(0.6)

def worker_b():
    j = 0
    while not stop.is_set():
        j += 1
        print("B tick", j)
        time.sleep(1.0)

t1 = threading.Thread(target=lambda: safe_run("worker_a", worker_a), daemon=True)
t2 = threading.Thread(target=lambda: safe_run("worker_b", worker_b), daemon=True)
t1.start()
t2.start()

print("Threads started:", t1.is_alive(), t2.is_alive())

# main Pygame loop must run in main thread
while True:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            stop.set()
            pygame.quit()
            sys.exit()
    screen.fill((0,0,0))
    pygame.display.flip()
    clock.tick(60)
