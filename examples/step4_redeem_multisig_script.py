from cryptos import *
from blockcypher import pushtx


priv_keys = [
    '33f5ed66b68f2b9283bddac39350730e9fb5dfe039ab6c9ad886c5983360065c',
    '6caab239e9d074cddce2859ccc0f2c51c0ea80bf66f433c587d99ac76c3f5905',
    '08ced65d8db410a9b886e1f8a86b4835a48ee4db029057a1e3bdfea3085b3d61']


def mk_multi_keys_script():
    pub_keys = ['', '', '']
    for i in range(len(priv_keys)):
        pub_keys[i] = c.privtopub(priv_keys[i])
    return mk_multisig_script(pub_keys, 2)


if __name__ == "__main__":

    c = Bitcoin(testnet=True)

    inputs = [{'output': '60d82e020ec3cc19e7958256f2adee920bf7801e8e95d9917f4c7f9cb28fc0aa:0', 'value': 100000}]
    outs = [{'value': 99000, 'address': 'ms3K4ANfmBS3neNKbfSehMhX2dHWXkZgu6'}]
    tx = c.mktx(inputs, outs)
    script_pub_key = mk_multi_keys_script()
    signing_tx = signature_form(tx, 0, script_pub_key)

    sig0 = ecdsa_tx_sign(signing_tx, priv_keys[0])
    sig2 = ecdsa_tx_sign(signing_tx, priv_keys[2])
    script_sig = (serialize_script([None, sig0, sig2]))
    tx["ins"][0]["script"] = script_sig

    tx_raw = serialize(tx)
    tx_hash = public_txhash(tx_raw)
    print(tx_hash)
    pushtx(tx_hex=tx_raw, coin_symbol='btc-testnet', api_key='0b63236dab064c8fb9e1f53e97895b7e')
