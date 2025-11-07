from multiprocessing import Process, Manager
import time
import random
import os

def timer(main_data):
    while True:
        if main_data.plauing:
            minute = main_data.minute
            hourus = main_data.hourus
            minute += 1
            if minute >= 60:
                minute = 0
                hourus += 1
            if hourus==13:
                hourus=0
            main_data.minute = minute
            main_data.hourus = hourus
        time.sleep(1 + max(2, main_data.NIGHT/5))


def num_shkatulka(main_data):
    while True:
        if main_data.plauing:
            if main_data.shkatulka >= 1:
                main_data.shkatulka = main_data.shkatulka - 1
            time.sleep(2 - (main_data.NIGHT/5))


def game_over(main_data):
    print("game over :(")
    main_data.gameover = True

class Move_unit_logic:
    def __init__(self):
        self._logic_timers = False
        self._logic_triger = False
         
    def timer(self):
        if not self._logic_timers:
            self._logic_timers = True
        return self._logic_triger
    
t=Move_unit_logic()

def muving_logic(main_data):
    while True:
        if main_data.plauing:
            if getattr(main_data, "shkatulka", 0) <= 0:
                    main_data.position["holl"][1] = None
                    main_data.position["coredor"][1] = "hitler"

            if main_data.position["zal"][0] == "egor" and random.randint(0, max(1, 10 - main_data.NIGHT)) == 0:
                main_data.position["holl"][0] = None
                main_data.position["zal"][0] = None
                if random.randint(0, 1) == 0:
                    main_data.position["toilet"][0] = "egor"
                else:
                    main_data.position["holl"][0] = "egor"


            if main_data.position["toilet"][0] == "egor" or main_data.position["holl"][0] == "egor" and random.randint(0,  13 - main_data.NIGHT) == 1:
                main_data.position["toilet"][0] = None
                main_data.position["holl"][0] = None
                main_data.position["zal"][0] = None
                time.sleep(1)
                main_data.position["main_prohod_ofise"] = "egor"


            if main_data.position["coredor"][1] == "hitler" and random.randint(0, max(1, 6 - main_data.NIGHT)) == 1:
                main_data.position["coredor"][1] = None
                main_data.position["offise"] = "hitler"

            if main_data.position.get("main_prohod_ofise"):
                time.sleep(3)
                if t.timer() and main_data.position['main_prohod_ofise']:
                    main_data.position["offise"] = True

            if main_data.position.get("offise"):
                game_over(main_data)

            sleep_time = max(0.1, 8 - round(main_data.NIGHT / 4, 1))
            time.sleep(sleep_time)
            temp=''
            for i in list(main_data.position.keys()):
                temp=temp+f" {i}:{main_data.position.get(i)}"
            print(temp, sleep_time)


def osvegitel_cd(main_data):
    while True:
        if getattr(main_data, "bolon_cd", 0) > 0:
            main_data.bolon_cd = round(max(0.0, main_data.bolon_cd - 0.1), 3)
        time.sleep(0.1)

def timer_sleep(main_data):
    while True:
        if getattr(main_data, "_logic_timers", False):
            time.sleep(max(0.1, 20 - getattr(main_data, "NIGHT", 1)))
            t._logic_triger = True
            t._logic_timers = False
        else:
            time.sleep(0.2)

def start_process():
    random.seed(time.time()*os.getpid())
    mgr = Manager()
    shared = mgr.Namespace()
    shared.shkatulka = 95
    shared.plauing = False
    shared.gameover = False
    shared.hourus = 12
    shared.minute = 0
    shared.bolon_cd = 0
    shared.NIGHT = 1
    shared.position = mgr.dict({
        "holl": mgr.list([None, "hitler"]),
        "coredor": mgr.list([None, None]),
        "zal": mgr.list(["egor", None]),
        "toilet": mgr.list([None, None]),
        "offise": None,
        "main_prohod_ofise": None
    })

    p1 = Process(name="num_shkatulka_FNaE", target=num_shkatulka, args=(shared,), daemon=True)
    p2 = Process(name="timer_FNaE", target=timer, args=(shared,), daemon=True)
    p3 = Process(name="muving_logic_FNaE", target=muving_logic, args=(shared,), daemon=True)
    p4 = Process(name="osvegitel_cd_FNaE", target=osvegitel_cd, args=(shared,), daemon=True)
    p5 = Process(name="timer_sleep_FNaE", target=timer_sleep, args=(shared,), daemon=True)

    p1.start(); p2.start(); p3.start(); p4.start(); p5.start()
    
    #print("procs started:", [(p.name, p.pid, p.is_alive()) for p in (p1,p2,p3,p4,p5)]) 
    print(mgr, shared, [p1,p2,p3,p4,p5])
    return shared, [p1,p2,p3,p4,p5]

    