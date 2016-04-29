import struct

import binascii

values = (0, 1, 1.2, 1.1)
packer = struct.Struct('I I f f')
packed_data = packer.pack(*values)
binascii.hexlify(packed_data)

unpacker = struct.Struct('I I f f')
unpacked_data = unpacker.unpack(packed_data)

print unpacked_data