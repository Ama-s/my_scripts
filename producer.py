import threading
import time
resource_lock = threading.Lock()
pid_counter = 1
exit_flag = False
class Process:
 def init(self):
 self.pid = None
def producer(process):
 global pid_counter
 while not exit_flag:
 with resource_lock:
 # Simulate data production and use the resource
 print(f"Process {process.pid} producing data...")
 time.sleep(2)
 pid_counter += 1
def consumer(process):
 while not exit_flag:
 with resource_lock:
 # Simulate data consumption and release the resource
 print(f"Process {process.pid} consuming data...")
 time.sleep(2)
# Create processes
process1 = Process()
process2 = Process()
# Assign PIDs after creating processes
process1.pid = pid_counter
process2.pid = pid_counter + 1
# Create threads
producer_thread1 = threading.Thread(target=producer, args=(process1,))
consumer_thread1 = threading.Thread(target=consumer, args=(process1,))
producer_thread2 = threading.Thread(target=producer, args=(process2,))
consumer_thread2 = threading.Thread(target=consumer, args=(process2,))
# Start threads
producer_thread1.start()
consumer_thread1.start()
producer_thread2.start()
consumer_thread2.start()
# Run for a limited time for demonstration purposes
time.sleep(10)
exit_flag = True
producer_thread1.join()
consumer_thread1.join()
producer_thread2.join()
consumer_thread2.join()