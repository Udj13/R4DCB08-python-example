#!/usr/bin/env python
# -*- coding: utf_8 -*-
"""
Change R4DCB08 network address example
(8-channel RS485 ModBus Sensor Board)

(C)2022 - Eugeny Shlyagin - shlyagin@gmail.com
"""

# pip install pySerial
import serial

# pip install modbus_tk
import modbus_tk
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu

PORT = 'COM7'
MODBUS_ADDRESS = 3  # current RS485 address
NEW_MODBUS_ADDRESS = 3  # new address to set


def main():
    """main"""
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

    # Change MODBUS address
    logger.info(master.execute(MODBUS_ADDRESS, cst.WRITE_SINGLE_REGISTER, 254, output_value=NEW_MODBUS_ADDRESS))


if __name__ == "__main__":
    main()
