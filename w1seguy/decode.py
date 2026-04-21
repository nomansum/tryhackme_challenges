import string

hex_input = input("Enter hex encoded string: ")
raw_bytes = bytes.fromhex(hex_input)

# We know the first 4 chars of the key are "305N" from your previous XOR with "THM{"
key_prefix = "305N"
alphabet = string.ascii_letters + string.digits

for char in alphabet:
    full_key = key_prefix + char
    result = ""
    for i in range(len(raw_bytes)):
        result += chr(raw_bytes[i] ^ ord(full_key[i % len(full_key)]))
    
    # We only print if the result looks like a flag (starts with THM{)
    if result.startswith("THM{"):
        print(f"Key char: {char} | Key: {full_key} | Result: {result}")
