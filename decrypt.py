import argparse
import binascii


def decrypt_pkscript(text):
    a = bytearray.fromhex(text)
    hash = binascii.b2a_hex(a[:32]).decode('utf-8')
    name = a[32:].decode()

    print(f'Document hash: {hash}')
    print(f'Author name: {name}')


if __name__ == "__main__":
    parser = argparse.ArgumentParser('Timestamp document')
    parser.add_argument('--pkscript', help='Locking script generated for timestamp document transaction', required=True)
    args = parser.parse_args()

    decrypt_pkscript(args.pkscript)
