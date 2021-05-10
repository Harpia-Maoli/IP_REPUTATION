from packet.backend import Backend
import sys

try:
    backend = Backend()
    backend.Programa()
except KeyboardInterrupt:
    print("\n\nVolte Sempre!!\n\n")
    sys.exit(0)
