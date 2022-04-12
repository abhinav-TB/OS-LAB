import threading
import time

# Shared Memory variables
CAPACITY = 10
buffer = [-1 for i in range(CAPACITY)]
in_index = 0
out_index = 0

# Declaring Semaphores
mutex = threading.Semaphore()
empty = threading.Semaphore(CAPACITY)
full = threading.Semaphore(0)

#producer thread
def producer():
    global CAPACITY, buffer, in_index, out_index
    global mutex, empty, full
     
    items_produced = 0
    counter = 0
     
    while items_produced < 20:
      empty.acquire()
      mutex.acquire()
       
      counter += 1
      buffer[in_index] = counter
      in_index = (in_index + 1)%CAPACITY
      print("Producer produced      : ", counter , " current buffer " , buffer )
       
      mutex.release()
      full.release()
       
      time.sleep(1)
       
      items_produced += 1

#consumer thread
def consumer():
  global CAPACITY, buffer, in_index, out_index, counter
  global mutex, empty, full
     
  items_consumed = 0
     
  while items_consumed < 20:
    full.acquire()
    mutex.acquire()
       
    item = buffer[out_index]
    buffer[out_index] = -1
    out_index = (out_index + 1)%CAPACITY
    print("Consumer consumed item : ", item , " current buffer " , buffer )
     
    mutex.release()
    empty.release()      
     
    time.sleep(2.5)
     
    items_consumed += 1


p_thread = threading.Thread(target = producer)
c_thread = threading.Thread(target = consumer)

p_thread.start()
c_thread.start()