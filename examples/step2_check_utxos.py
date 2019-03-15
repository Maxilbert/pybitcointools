from cryptos import *

c = Bitcoin(testnet=True)

addresses = [
    'mxdNW2wKGafADgYpxWo2LBp6t3VfnCqt9J',
    'ms3K4ANfmBS3neNKbfSehMhX2dHWXkZgu6',
    'mxXpdrr1DFVNPpdXH1yzeLje9JF8TuFbvB',
    'n2GFJcivbiuLy3gwa4RwUZknWrWNaKosF8'
]

for addr in addresses:
    print("Address (WFI): ", addr)
    inputs = c.unspent(addr)
    print(inputs)
    print('')
