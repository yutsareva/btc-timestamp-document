import argparse

from hashing import get_file_hash
from qr import create_qr_code
from btc_tx import create_tx


def main():
    parser = argparse.ArgumentParser('Timestamp document')
    parser.add_argument('--network', help='Blockchain net', choices=['testnet', 'bitcoin'], default='testnet')
    parser.add_argument('--private-key', help='Private key')
    parser.add_argument('--file', help='Path to file')
    parser.add_argument('--name', help='Author name')
    args = parser.parse_args()

    file_hash = get_file_hash(args.file)

    tx_result = create_tx(args.private_key, args.network, file_hash, args.name)
    if not tx_result:
        return
    create_qr_code(tx_result['txid'])

if __name__ == "__main__":
    main()
