#!/usr/bin/python3
import sys
import os

fd = sys.stderr.fileno()
data = "and that piece of art is useful - Dora Korpar, 2015-10-19\n"
os.write(fd, data.encode("utf-8"))
sys.exit(1)
