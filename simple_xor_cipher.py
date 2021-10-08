#!/usr/bin/python

import sys

args_num = len(sys.argv)

if args_num != 4:
    print('Input file, output file and key(b10 number) are mandatory')
    exit()

f = open(sys.argv[1],"rb")
o = open(sys.argv[2],"ab")
k = int(sys.argv[3])

out = ''
try:
    byte = f.read(1)
    while byte != "":
        temp_byte = ord(byte) ^ k
        print("Byte -> " + str(byte) + " Ord func -> " + str(ord(byte)) + " Character -> " + " key value -> " + str(k) + " XOR result -> " + chr(temp_byte))
        out += chr(temp_byte)
        byte = f.read(1)
finally:
    f.close()

o.write(out)
o.close()
