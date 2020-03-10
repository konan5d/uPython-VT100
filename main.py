# main.py -- put your code here!

from pyb import UART

numero_uart = 2

uart = UART(numero_uart)

uart.init(9600, 8, None, 1)

while(1):
    uart.write(b"0x00")
    pyb.delay(1000)
