#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test Tango device server for use with scaling tests."""
import sys
import time
import logging

import tango
from tango import server

# import test_device


def register():
    """."""
    db = tango.Database()
    device_info = tango.DbDevInfo()

    device_info.server = 'TestDeviceServer/1'
    device_info.name = 'test/test_device/0'
    device_info._class = 'TestDevice1'
    db.add_device(device_info)

    device_info.server = 'TestDeviceServer/1'
    device_info.name = 'test/test_device/1'
    device_info._class = 'TestDevice2'
    db.add_device(device_info)


def register_devices():
    """."""
    tango_db = tango.Database()
    logging.info("Registering devices!")

    device_info = tango.DbDevInfo()

    device_class = 'TestDevice1'

    # Name of device (/server?) class.
    device_info._class = device_class

    # Name of server instance
    device_info.server = "{}/1".format(device_class)

    # Generate names and add devices to the database.
    start_time = time.time()
    num_devices = 1
    for index in range(num_devices):
        device_info.name = 'test/1/{:03d}'.format(index)
        tango_db.add_device(device_info)

    # Set properties
    tango_db.put_class_property(device_class, dict(version='1.0.0'))
    print('elapsed = {}'.format(time.time() - start_time))


if __name__ == '__main__':
    logging.basicConfig()
    # register_devices()
    register()
