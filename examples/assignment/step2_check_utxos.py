from cryptos import Bitcoin
from assignment.step1_create_account import create_account


def get_utxos(addr):
    testnet = Bitcoin(testnet=True)
    utxos = testnet.unspent(addr)
    return utxos


if __name__ == "__main__":
    pwd = 'blockchain.njit.edu'
    [sk, pk, add] = create_account(pwd)
    print(get_utxos(add))
