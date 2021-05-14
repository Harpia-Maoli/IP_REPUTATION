from packet.backend import Backend
import sys
import argparse

parser = argparse.ArgumentParser(description="IP Reputation")

parser.add_argument('-a','--arquivo', metavar='IPs.txt', help='Caminho do arquivo TXT contendo os IP\'s')

args = parser.parse_args()

try:
    backend = Backend(args.arquivo)
except KeyboardInterrupt:
    print("\n\nVolte Sempre!!\n\n")
    sys.exit(0)
