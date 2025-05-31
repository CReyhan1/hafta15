import threading

def coder(number,number1,number2,number3):
    print(f'Coder ID: {number},{number1},{number2},{number3}')

threads = []
for k in range(5):
    for a in range(5):
        for b in range(5):
            for c in range(5):
                t = threading.Thread(target=coder, args=(k, a,b,c))
                threads.append(t)
                t.start()
