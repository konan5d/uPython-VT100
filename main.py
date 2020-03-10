# main.py -- put your code here!

from pyb import UART

def uart_init(num_uart):
    uart_port = UART(num_uart)
    uart_port.init(9600, 8, None, 1)

    return uart_port

def vt100_clear_screen(uart):  
    uart.write(b"\x1b[2J\x1b[?25l")

def vt100_move(uart, x, y):
    uart.write("\x1b[{};{}H".format(y, x))

# Initialisation de la liaison série 
uart = uart_init(2)

while(1):
    vt100_move(uart, 5, 10)
    uart.write(b"0x00")
    pyb.delay(1000)
    vt100_clear_screen(uart)