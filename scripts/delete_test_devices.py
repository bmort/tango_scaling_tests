#!/usr/bin/env python3
import argparse
import logging

import tango


def delete_devices():
    """."""
    db = tango.Database()
    class_list = db.get_class_list('*')
    print('class list = ', class_list)
    server_list = db.get_server_list('*')
    print('server list = ', server_list)

    # for index in range(num_devices):
    #     name = 'low_sdp/elt/test_device_{:05d}'.format(index)

    # db.delete_server('TestDevice/test1')
    # db.delete_device('tango/test1/000')


def delete_server():
    """."""
    db = tango.Database()
    db.delete_server('')


if __name__ == '__main__':
    delete_devices()
