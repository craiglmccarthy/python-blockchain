#!/usr/bin/env python3
import qrcode
from pycoin.symbols.btc import network

key = network.keys.bip32_seed(b"craiglmccarthy")
print(key.address())
img = qrcode.make(key.address())
img.save("craiglmccarthy_qr.jpg")

key = network.keys.bip32_seed(b"satoshinakamoto")
print(key.address())
img = qrcode.make(key.address())
img.save("satoshinakamoto_qr.jpg")
