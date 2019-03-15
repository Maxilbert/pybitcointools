from cryptos import Bitcoin, ecdsa_tx_sign, serialize_script, serialize, signature_form
from assignment import utils


def create_unsigned_redeem_tx(hash_tx):
    inputs = [{'output': hash_tx + ':0', 'value': utils.amount}]
    outs = [{'value': utils.amount - utils.fee, 'address': utils.addr_redeemer}]
    return Bitcoin(testnet=True).mktx(inputs, outs)


def sign_redeem_tx(tx, i=0, j=1):
    script_pub_key = utils.mk_2_of_3_script()
    signing_tx = signature_form(tx, 0, script_pub_key)
    sig0 = ecdsa_tx_sign(signing_tx, utils.sk_cosigners[i])
    sig2 = ecdsa_tx_sign(signing_tx, utils.sk_cosigners[j])
    script_sig = (serialize_script([None, sig0, sig2]))
    tx["ins"][0]["script"] = script_sig
    tx_raw = serialize(tx)
    # print(tx_raw)
    return tx_raw


if __name__ == "__main__":
    tx_hash = open("tx_hash", "r").readline()
    tx = create_unsigned_redeem_tx(tx_hash)
    tx_signed = sign_redeem_tx(tx, i=0, j=2)
    utils.push_raw_tx(tx_signed)
