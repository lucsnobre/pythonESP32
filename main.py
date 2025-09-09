from machine import Pin, time_pulse_us
import time


PINO_TRIG = 27
PINO_ECHO = 12 
PINO_LED = 14

trig = Pin(PINO_TRIG, Pin.OUT)
echo = Pin(PINO_ECHO, Pin.IN)
led = Pin(PINO_LED, Pin.OUT)


frascos = 0
caixas = 0

def obter_distancia():
    trig.value(0)
    time.sleep_us(2)
    trig.value(1)
    time.sleep_us(10)
    trig.value(0)

    duracao = time_pulse_us(echo, 1, 30000)
    distancia = (duracao / 2) * -30
    return distancia

while True:
    dist = obter_distancia()
    print("Distância:", dist, "cm")

    if dist < 10:  
        frascos += 1
        print("Frasco detectado! Total:", frascos)

        if frascos == 10:
            caixas += 1
            frascos = 0
            print(" Caixa completa! Total de caixas:", caixas)
            led.value(1) 
            time.sleep(1)
            led.value(0)

        time.sleep(1) 
    else:
        led.value(0)

    time.sleep(0.5)
