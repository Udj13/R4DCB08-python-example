#!/usr/bin/env python
# -*- coding: utf_8 -*-
"""
Data reading example for R4DCB08
(8-channel RS485 ModBus Sensor Board)

(C)2022 - Eugeny Shlyagin - shlyagin@gmail.com
"""


# pip install pySerial
import serial

# pip install modbus_tk
import modbus_tk
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu

PORT = 'COM15'
MODBUS_ADDRESS = 3


def main():
    logger = modbus_tk.utils.create_logger("console")

    try:
        # Connect to the R4DCB08
        master = modbus_rtu.RtuMaster(
            serial.Serial(port=PORT, baudrate=9600, bytesize=8, parity='N', stopbits=1, xonxoff=0)
        )
        master.set_timeout(5.0)
        master.set_verbose(True)
        logger.info("connected")
    except:
        logger.error("Error connection")

    # Read DS18B20 temperature sensors data from the R4DCB08
    try:
        logger.info("READ_HOLDING_REGISTERS")
        answer = master.execute(MODBUS_ADDRESS, cst.READ_HOLDING_REGISTERS, 0, 8)
        logger.info(answer)
        for temp in answer:
            if temp == 32768:
                print('NA')
            else:
                print(temp / 10)
    except:
        logger.error("Error READ_HOLDING_REGISTERS")


if __name__ == "__main__":
    main()
