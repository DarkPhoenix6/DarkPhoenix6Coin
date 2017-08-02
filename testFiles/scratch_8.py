import hashlib, struct, binascii


ver = 0x00000002

prev_block = '000000000000000117c80378b8da0e33559b5997f2ad55e2f7d18ec1975b9717'
mrkl_root = '871714dcbae6c8193a2bb9b2a69fe1c0440399f38d94b3a0f1b447275a29978a'
time_ = 0x53058b35# 2014-02-20 04:57:25


bits = 0x19015f53

bits2 = 0x535f0119

# https://en.bitcoin.it/wiki/Difficulty
exp = bits >> 24
mant = bits & 0xffffff
target_hexstr = '%064x' % (mant * (1 << (8 * (exp - 3))))
target_str = target_hexstr.encode()
nonce = 0

while nonce < 0x100000000:
    header = (struct.pack("<L", ver) + bytes.fromhex(prev_block)[::-1] + bytes.fromhex(mrkl_root)[::-1] +
              struct.pack("<LLL", time_, bits, nonce))
    my_hash = hashlib.sha256(hashlib.sha256(header).digest()).digest()
    print(nonce, binascii.hexlify(my_hash[::-1]), my_hash[::-1], my_hash)
    if my_hash < target_str:
        print('success')
        break
    nonce += 1