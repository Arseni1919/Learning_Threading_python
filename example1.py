import logging
import threading
import time

def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(5)
    logging.info("Thread %s: finishing", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    logging.info("Main    : before creating thread")
    # x = threading.Thread(target=thread_function, args=(1,))
    x = threading.Thread(target=thread_function, args=(1,), daemon=True)
    logging.info("Main    : before running thread")
    x.start()
    logging.info("Main    : wait for the thread to finish")
    # When x will join then continue:
    x.join()
    logging.info("Main    : all done")

    # / Users / arseniperchik / opt / anaconda3 / envs / DRL4 / bin / python / Users / arseniperchik / PycharmProjects / Learning_threading / example1.py
    # 12: 50:41: Main: before
    # creating
    # thread
    # 12: 50:41: Main: before
    # running
    # thread
    # 12: 50:41: Thread
    # 1: starting
    # 12: 50:41: Main: wait
    # for the thread to finish
    # 12: 50:41: Main: all
    # done
    # 12: 50:43: Thread
    # 1: finishing
    #
    # Process
    # finished
    # with exit code 0