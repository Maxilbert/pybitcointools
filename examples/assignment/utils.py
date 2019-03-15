from cryptos import *
from blockcypher import pushtx

sk_cosigners = [
    '33f5ed66b68f2b9283bddac39350730e9fb5dfe039ab6c9ad886c5983360065c',
    '6caab239e9d074cddce2859ccc0f2c51c0ea80bf66f433c587d99ac76c3f5905',
    '08ced65d8db410a9b886e1f8a86b4835a48ee4db029057a1e3bdfea3085b3d61']
addr_redeemer = 'mfiQeDJWfKp6LuDxdd7AffVtCJbBpBezKZ'
amount = 100000
fee = 10000


def mk_2_of_3_script(sks=sk_cosigners):
    c = Bitcoin(testnet=True)
    pks = ['', '', '']
    for i in range(len(sks)):
        pks[i] = c.privtopub(sks[i])
    return mk_multisig_script(pks, 2)


def push_raw_tx(tx_signed_raw):
    pushtx(tx_hex=tx_signed_raw, coin_symbol='btc-testnet', api_key='0b63236dab064c8fb9e1f53e97895b7e')
    tx_hash = public_txhash(tx_signed_raw)
    print(tx_hash)
    return tx_hash

