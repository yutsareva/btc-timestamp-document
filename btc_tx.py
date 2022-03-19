from bitcoinlib.wallets import Wallet, wallet_delete_if_exists

from bitcoinlib.services.services import Service
from bitcoinlib.keys import HDKey
from bitcoinlib.transactions import Output, Transaction, Input
import binascii


def _print_wallet_debug_info(private_key, network):
    if wallet_delete_if_exists('wallet', force=True): pass
    w = Wallet.create('wallet', keys=private_key, scheme='single', network=network)
    w.scan(network=network)
    print(w.info())


def _bin_to_hex(string):
    return binascii.b2a_hex(string).decode('utf-8')


def _create_locking_script(data, author_name):
    print(data)
    text_from_bytes = bytearray.fromhex(data) + bytes(author_name, 'utf-8')
    if len(text_from_bytes) > 75:
        raise Exception('Your name is too long')
    payload = bytearray((len(text_from_bytes),)) + text_from_bytes
    locking_script = '6a' + _bin_to_hex(payload)
    return locking_script


def create_tx(private_key, network, data, author_name):
    # _print_wallet_debug_info(private_key, network)

    k = HDKey(private_key)
    address = k.address()

    srv = Service(network)
    utxos = srv.getutxos(address)
    if not utxos:
        print('You do not have unspent transaction outputs')
        return None
    # print(utxos)

    lock_script = _create_locking_script(data, author_name)

    output = Output(network=network, value=0, address=address, lock_script=lock_script)
    input = Input(
        utxos[0]['txid'],
        utxos[0]['output_n'],
        network=network
    )
    tx = Transaction(inputs=[input], outputs=[output])

    tx.sign(keys=k)
    d = srv.sendrawtransaction(tx.raw_hex())
    return d
