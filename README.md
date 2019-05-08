# Tango Performance tests

Tango Controls performance tests.

## 0  TODO

- Create XMI file for test device with pogo?
  - **Can Skip this and create device manually**
  - **Can Skip adding all attributes and commands**
- Add instructions to readme for using the development
  container
- Add instructions for monitoring memory / cpu
- Write test script for a few tests to shakedown results
- Move repository to SDP GitHub? (and link to JIRA?)

## 1  References

- [Notes: Google Docs](https://docs.google.com/document/d/1XxoDWZd827XyeOOD8qlFXDuOWoWfx0tw3OsX9iRbSU4)
- <https://jira.ska-sdp.org/browse/UKSW-3>

## 2  Quick-start

```bash
docker stack deploy -c docker-compose.yml tango_test
```

where `tango_test` is the name of the stack.

This starts ....

## Developing using the `tango-python-dev` (name?) container

TODO

## 3  Approach

### 3.1 Test device: `/test_device_1`

This is a Tango device with XX attributes (one of each type) and XX commands.

It is registered and started using xxx

Started using both a Tango Facility and without the Tango db.


## 4  Test results

### 4.1  Device registration

#### 4.1.1  With Tango database

Use`test_device_1` capture time taken to start

| Number of devices | Start time (s) |
|:-:                |---             |
| 1                 | ???            |
| 10                | ???            |
| 100               | ???            |
| 1000              | ???            |
| 10,000            | ???            |

#### 4.1.2  Without Tango database

Use`test_device_1` capture time taken to start

| Number of devices | Start time (s) |
|:-:                |---             |
| 1                 | ???            |
| 10                | ???            |
| 100               | ???            |
| 1000              | ???            |
| 10,000            | ???            |

### 4.2  Device server resource usage (steady state)

| Number of devices | Memory (MiB)   | Average CPU (%) |
|:-:                |---             | ---             |
| 1                 | ???            |                 |
| 10                | ???            |                 |
| 100               | ???            |                 |
| 1000              | ???            |                 |
| 10,000            | ???            |                 |

### 4.3  Device attribute query performance

Number of concurrent queries
Query rate

### 4.4  Device command performance

Number of concurrent commands
Command issue rate

### 4.5  Device pipe performance

***Stretch goal***

----

## Appendix A: PyCharm Pro development setup

Project interpreter set to Docker using `bmort/tango_python_dev:0.1.0`.

## Appendix B: Starting and running the Tango test Device

Start an interactive prompt into a container with Tango installed using

```bash
make prompt
```

### B.1  Without a Tango db & SQL server

```bash
python3 ./test_device_1/test_device_1.py 1 -ORBendPoint giop:tcp::23333 -nodb
```

### B.2  With Tango Db

First register the device(s) in the database

```bash
python3 scripts/register_test_devices.py
```

To start the device server

```bash
python3 TestDeviceServer
```

To list test devices

```bash
python3 scripts/list_test_devices.py
```

To delete test devices

```bash
python3 scripts/delete_test_devices.py
```


## Appendix C: Useful iTango commands

<https://manpages.debian.org/unstable/python-itango/itango.1.en.html>

- `refreshdb`
- `db`
- `lsdev`
- `lsserv`
- `lsdevclass`
