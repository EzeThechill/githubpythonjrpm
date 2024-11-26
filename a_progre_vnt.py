import time
car = "📗"
distancia = 10
for position in range (distancia) :
    print("📗" * position, end = "")
    print(car, end = "\r")
    time.sleep(0.5)
