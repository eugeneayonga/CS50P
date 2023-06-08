import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.daemon("Hello, " + sys.argv[1])