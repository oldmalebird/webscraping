import threading
import time
import random

# def greet(index):
#     print('hello world - %d') % index
#
#
# def line_run():
#     for x in range(5):
#         greet(x)
#
#
# def async_run():
#     for x in range(5):
#         th = treading.Thread(target=greet, args=[x])
#         th.start()

gLock = threading.Lock()
MONEY = 0


def producer():
    while True:
        global MONEY
        random_money = random.randint(10, 100)
        gLock.acquire()
        MONEY += random_money
        print('生产者%s 生产了%d, 余额%d' % (threading.current_thread, random_money,
                                     MONEY))
        gLock.release()
        time.sleep(0.5)


def comstomer():
    while True:
        global MONEY
        random_money = random.randint(10, 100)
        if MONEY > random_money:
            MONEY -= random_money
            gLock.acquire()
            print('消费者%s-消费了：%d, 余额%d' % (threading.current_thread,
                                          random_money, MONEY))
            gLock.release()

        else:
            print('需要消费的钱为： %d, 余额为：%d' % (random_money, MONEY))
        time.sleep(0.5)


def p_c_test():
    for x in range(3):
        th = threading.Thread(target=producer)
        th.start()
    for x in range(3):
        th = threading.Thread(target=comstomer)
        th.start()


if __name__ == '__main__':
    p_c_test()
