import base58

# Your transaction instruction data (Base58 encoded)
encoded_data = "3Bxs43ZMjSRQLs6o"

# Decode from Base58 to bytes
decoded_bytes = base58.b58decode(encoded_data)

# For a System Program transfer, the layout is:
#   byte 0: instruction index (should be 2 for transfer)
#   bytes 1-8: amount in lamports (u64 little-endian)
instruction_type = decoded_bytes[0]
lamports = int.from_bytes(decoded_bytes[1:9], byteorder="little")

print("Instruction Type:", instruction_type)
print("Lamports:", lamports)
