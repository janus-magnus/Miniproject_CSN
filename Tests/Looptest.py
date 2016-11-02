import time
import threading

def process():
    print('dingdong')
    inss = 0
    while True:
        print(inss)
        time.sleep(10)
        inss+=1

thread = threading.Thread(target=process)
thread.daemon = True
thread.start()
while True:
    exit_signal = input('Type "exit" anytime to stope server\n')
    if exit_signal == 'exit':
        break