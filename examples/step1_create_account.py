from cryptos import *


c = Bitcoin(testnet=True)

priv_keys = [
    '50968e05d5ec48f1e0deb9a0f033106dfcd6bc835ac80ff9bbe5a6fb50036539',
    '33f5ed66b68f2b9283bddac39350730e9fb5dfe039ab6c9ad886c5983360065c',
    '6caab239e9d074cddce2859ccc0f2c51c0ea80bf66f433c587d99ac76c3f5905',
    '08ced65d8db410a9b886e1f8a86b4835a48ee4db029057a1e3bdfea3085b3d61']

for priv_key in priv_keys:
    print("Private Key (hex): ", priv_key)
    print("Public Key (hex): ", c.privtopub(priv_key))
    print("Address (wif): ", c.pubtoaddr(c.privtopub(priv_key)))
    print("")
