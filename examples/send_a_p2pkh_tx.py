from cryptos import *
from blockcypher import pushtx

c = Bitcoin(testnet=True)
priv = '6caab239e9d074cddce2859ccc0f2c51c0ea80bf66f433c587d99ac76c3f5905'
pub = c.privtopub(priv)
addr = c.pubtoaddr(pub)

inputs = c.unspent(addr)
outs = [{'value': 33500000, 'address': 'ms3K4ANfmBS3neNKbfSehMhX2dHWXkZgu6'}]
print(outs)



tx = c.mktx(inputs, outs)
tx1 = tx
print(tx)

for i in range(len(tx['ins'])):
    tx2 = c.sign(tx1, i, priv)
    tx1 = tx2
    print(tx)

tx_raw = serialize(tx)
print(tx_raw)

#pushtx(tx_hex=tx_raw, coin_symbol='btc-testnet', api_key='0b63236dab064c8fb9e1f53e97895b7e')
