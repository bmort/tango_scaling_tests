#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test Tango device server for use with scaling tests."""
import argparse
import time

import tango


def delete_server():
    """."""
    db = tango.Database()
    server = 'TestDeviceServer/1'

    server_list = list(db.get_server_list(server))

    if server in server_list:
        start_time = time.time()
        db.delete_server('TestDeviceServer/1')
        print('- Delete server: {:.4f} s'.format(time.time() - start_time))


def list_devices():
    """."""
    db = tango.Database()
    server_instance = 'TestDeviceServer/1'
    device_class = 'TestDevice1'
    devices1 = list(db.get_device_name(server_instance, device_class))
    device_class = 'TestDevice2'
    devices2 = list(db.get_device_name(server_instance, device_class))
    print('- No. registered devices: {}'.format(len(devices1 + devices2)))

    exported_devices = list(db.get_device_exported('test/*'))
    print('- No. running devices: {}'.format(len(exported_devices)))


def register(num_devices):
    """."""
    db = tango.Database()
    device_info = tango.DbDevInfo()

    device_info.server = 'TestDeviceServer/1'
    device_info._class = 'TestDevice1'

    start_time = time.time()
    for device_id in range(num_devices):
        device_info.name = 'test/test_device/{:05d}'.format(device_id)
        db.add_device(device_info)
    elapsed = time.time() - start_time
    print('- Register devices: {:.4f} s ({:.4f} s/device)'
          .format(elapsed, elapsed / num_devices))


def main():
    """."""
    parser = argparse.ArgumentParser(description='Device registration time.')
    parser.add_argument('num_devices', metavar='N', type=int,
                        default=1, nargs='?',
                        help='Number of devices to start.')
    args = parser.parse_args()

    delete_server()

    print('* Registering {} devices'.format(args.num_devices))
    register(args.num_devices)

    list_devices()


if __name__ == '__main__':
    main()

