#!/usr/bin/env python3
import argparse
import logging

import tango


def list_devices():
    """."""
    db = tango.Database()

    print('Test Servers:')
    server_list = db.get_server_list('*')
    # server_name_list = db.get_server_name_list()
    i = 1
    for name in server_list:
        if not name.startswith('Test'):
            continue
        print('  {:2d}. {}'.format(i, name))
        i += 1

    # Classes
    class_list = db.get_class_list('Test*')
    print()
    print('Test Device classes: ')
    i = 1
    for name in class_list:
        print('  {:2d}. {}'.format(i, name))
        i += 1

    # Devices (all)
    server_instance = 'TestDeviceServer/1'
    device_class = 'TestDevice1'
    devices1 = list(db.get_device_name(server_instance, device_class))
    device_class = 'TestDevice2'
    devices2 = list(db.get_device_name(server_instance, device_class))
    print()
    print('Test Devices (all):')
    i = 1
    for name in devices1 + devices2:
        print('  {:2d}. {}'.format(i, name))
        i += 1

    exported_devices = list(db.get_device_exported('test/*'))
    print()
    print('Test Devices (running):')
    i = 1
    for name in exported_devices:
        print('  {:2d}. {}'.format(i, name))
        i += 1


    # exported_devices = db.get_device_exported_for_class('TestDevice')


if __name__ == '__main__':
    list_devices()
