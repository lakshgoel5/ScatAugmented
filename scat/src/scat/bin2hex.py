import sys
filename = sys.argv[1]
with open(filename, "r") as f:
    for line in f:
        bin_str = line.strip()
        # Group bits into bytes (8 bits), convert each to hex with 2 digits
        hex_str = ''.join(f"{int(bin_str[i:i+8], 2):02x}" for i in range(0, len(bin_str), 8))
        print(hex_str)
