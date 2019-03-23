http-tarpit
===========

Web-server which produces infinite chunked-encoded responses

## Installation

Standard Python package installation.

## Usage

Synopsis:

```
$ ./venv/bin/http-tarpit --help
usage: http-tarpit [-h] [--disable-uvloop] [-v {debug,info,warn,error,fatal}]
                   [-m {clock,newline,urandom,null}] [-a BIND_ADDRESS]
                   [-p BIND_PORT] [-c CERT] [-k KEY]

Web-server which produces infinite chunked-encoded responses

optional arguments:
  -h, --help            show this help message and exit
  --disable-uvloop      do not use uvloop even if it is available (default:
                        False)
  -v {debug,info,warn,error,fatal}, --verbosity {debug,info,warn,error,fatal}
                        logging verbosity (default: info)
  -m {clock,newline,urandom,null}, --mode {clock,newline,urandom,null}
                        operation mode (default: clock)

listen options:
  -a BIND_ADDRESS, --bind-address BIND_ADDRESS
                        bind address (default: 0.0.0.0)
  -p BIND_PORT, --bind-port BIND_PORT
                        bind port (default: 8080)

TLS options:
  -c CERT, --cert CERT  enable TLS and use certificate (default: None)
  -k KEY, --key KEY     key for TLS certificate (default: None)
```

### Modes of operation

* `clock` - feed client with current time string every second
* `newline` - feed client with newlines as fast as possible
* `urandom` - feed client with random bytes as fast as possible
* `null` - feed client with zero bytes as fast as possible
