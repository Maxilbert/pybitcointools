from cryptos import Bitcoin, ecdsa_tx_sign, serialize_script, serialize, signature_form, privtopub
from assignment import utils


def create_unsigned_redeem_tx(hash_tx):
    inputs = [{'output': hash_tx + ':0', 'value': utils.amount}]
    outs = [{'value': utils.amount - utils.fee, 'address': utils.addr_redeemer}]
    return Bitcoin(testnet=True).mktx(inputs, outs)


def sign_redeem_tx(tx, i=0, j=1):
    script_pub_key = utils.mk_2_of_3_script()
    #script_pub_key = '76a9147e67314504e2d48225e6bc9214a9be1bea95330c8763ac676d00687b76a914baa42949adda8ed2ad3354332be5e4a3d44902768763ac676d00687276a914e39299dc381b4428032bf4cf51403c209b2751038763ac676d0068939352a1'
    signing_tx = signature_form(tx, 0, script_pub_key)
    sig0 = ecdsa_tx_sign(signing_tx, utils.sk_cosigners[i])
    sig1 = ecdsa_tx_sign(signing_tx, utils.sk_cosigners[j])
    script_sig = serialize_script([None, sig0, sig1])
    #script_sig = serialize_script([sig1, privtopub(utils.sk_cosigners[j]), sig1, privtopub(utils.sk_cosigners[i]), sig0, privtopub(utils.sk_cosigners[i])])
    tx["ins"][0]["script"] = script_sig
    tx_raw = serialize(tx)
    print(tx_raw)
    return tx_raw


if __name__ == "__main__":
    tx_hash = open("tx_hash", "r").readline()
    tx = create_unsigned_redeem_tx('21f63d36b4785353261a594c3b31fa0ee00c199dda6bd8ec705b78fd216a3d55')
    tx_signed = sign_redeem_tx(tx, i=0, j=1)
    utils.push_raw_tx(tx_signed)
