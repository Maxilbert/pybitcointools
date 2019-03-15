from cryptos import sha256
from cryptos import privtopub
from cryptos import pubtoaddr
from cryptos import Bitcoin


def create_account(pwd):
    priv = sha256(pwd)
    pub = privtopub(priv)
    addr = pubtoaddr(pub, Bitcoin.testnet_overrides['magicbyte'])
    return [priv, pub, addr]


if __name__ == "__main__":
    password = 'blockchain.njit.edu'
    [sk, pk, add] = create_account(password)
    print("Private Key (hex): ", sk)
    print("Public Key (hex): ", pk)
    print("Address (wif): ", add)
    print("")
