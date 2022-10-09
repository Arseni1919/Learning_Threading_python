# Learning Threading in Python

## About

Python threading allows you to have different parts of your program run concurrently
and can simplify your design.


## Starting A Thread

```python
import logging
import threading
import time

def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    logging.info("Main    : before creating thread")
    x = threading.Thread(target=thread_function, args=(1,))
    logging.info("Main    : before running thread")
    x.start()
    logging.info("Main    : wait for the thread to finish")
    # x.join()
    logging.info("Main    : all done")
```


## Daemon Threads

Those threads finish to run imidiately when the all other non-deamon threads finished without completion.

```python
x = threading.Thread(target=thread_function, args=(1,), daemon=True)
```

## join() a Thread

To tell one thread to wait for another thread to finish, you call `.join()`. If you uncomment that line, the main thread will pause and wait for the thread x to complete running. Daemon or not it does not matter.

```python
x.join()
```


## Credits

- [Real Python Tutorial - An Intro to Threading in Python](https://realpython.com/intro-to-python-threading/#using-a-threadpoolexecutor)
- [Real Python Tutorial - Python Concurrency](https://realpython.com/python-concurrency/)














