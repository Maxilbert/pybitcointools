from cryptos import Bitcoin, mk_pubkey_script, signature_form, ecdsa_tx_sign, serialize_script, serialize
from assignment.step1_create_account import create_account
from assignment.step2_check_utxos import get_utxos
from assignment import utils


def create_unsigned_2_of_3_tx(add):
    inputs = get_utxos(add)
    balance = sum([utxo['value'] for utxo in inputs])
    outs = [
        #{'value': utils.amount, 'script': utils.mk_2_of_3_script()},
        {'value': utils.amount, 'script': '76a9147e67314504e2d48225e6bc9214a9be1bea95330c8763ac676d00687b76a914baa42949adda8ed2ad3354332be5e4a3d44902768763ac676d00687276a914e39299dc381b4428032bf4cf51403c209b2751038763ac676d0068939352a1'},
        {'value': balance - utils.amount - utils.fee, 'script': mk_pubkey_script(add)}
    ]
    return Bitcoin(testnet=True).mktx(inputs, outs)


def sign_2_of_3_tx(tx, sk, add):
    for i in range(len(tx['ins'])):
        script_pub_key = mk_pubkey_script(add)
        signing_tx = signature_form(tx, i, script_pub_key)
        sig = ecdsa_tx_sign(signing_tx, sk)
        script_sig = [sig, pk]
        tx["ins"][i]["script"] = serialize_script(script_sig)
    tx_raw = serialize(tx)
    # print(tx_raw)
    return tx_raw


if __name__ == "__main__":
    [sk, pk, add] = create_account("blockchain.njit.edu")
    tx = create_unsigned_2_of_3_tx(add)
    tx_signed = sign_2_of_3_tx(tx, sk, add)
    tx_hash = utils.push_raw_tx(tx_signed)
    f = open("tx_hash", "w")
    f.write(tx_hash)
    f.close()
