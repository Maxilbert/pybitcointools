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
    priv = '50968e05d5ec48f1e0deb9a0f033106dfcd6bc835ac80ff9bbe5a6fb50036539'
    pub = c.privtopub(priv)
    addr = c.pubtoaddr(pub)

    inputs = c.unspent(addr)

    outs = [{'value': 100000, 'script': mk_multi_keys_script()}, {'value': 79000, 'script': mk_pubkey_script(addr)}]
    tx = c.mktx(inputs, outs)

    for i in range(len(tx['ins'])):
        script_pub_key = mk_pubkey_script(addr)
        signing_tx = signature_form(tx, i, script_pub_key)
        sig = ecdsa_tx_sign(signing_tx, priv)
        script_sig = [sig, pub]
        tx["ins"][i]["script"] = serialize_script(script_sig)

    tx_raw = serialize(tx)
    print(tx_raw)

#    pushtx(tx_hex=tx_raw, coin_symbol='btc-testnet', api_key='0b63236dab064c8fb9e1f53e97895b7e')
