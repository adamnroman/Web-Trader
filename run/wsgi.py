#!/usr/bin/env python3

from src import omnibus

if __name__ == '__main__':
    omnibus.run('127.0.0.1', port=5001, debug=True)
