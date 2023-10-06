#!/bin/python3

"""Methods to decrypt the secretum."""

import sys


def decrypt(value):
    """Decrypt."""
    return 0




def main():
    """Main function to parse input/output
    and decrypt the secretum."""
    digits = str(sys.argv[1])
    last = int(sys.argv[2])
    result = decrypt(0)
    print('La clau per utilitzar el descodificador és {0}'.format(result))


if __name__ == '__main__':
    main()
