import threading

def coder(number,number1):
    print(f'Coder ID: {number},{number1}')

threads = []
for k in range(5):
    for a in range(5):
        t = threading.Thread(target=coder, args=(k,a))
        threads.append(t)
        t.start()
       
               
