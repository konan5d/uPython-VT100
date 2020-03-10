# main.py -- put your code here!

from pyb import UART

def uart_init(num_uart):
    uart = UART(num_uart)
    uart.init(9600, 8, None, 1)

# Initialisation de la liaison série 
uart_init(2)


while(1):
    uart.write(b"0x00")
    pyb.delay(1000)
