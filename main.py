# main.py -- put your code here!

from pyb import UART

def uart_init(num_uart):
    uart_port = UART(num_uart)
    uart_port.init(9600, 8, None, 1)

    return uart_port

# Initialisation de la liaison série 
uart = uart_init(2)

while(1):
    uart.write(b"0x00")
    pyb.delay(1000)
