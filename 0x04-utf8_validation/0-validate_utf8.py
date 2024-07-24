def validUTF8(data):
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    # Masks to check the significant bits
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for byte in data:
        # Get the 8 least significant bits of the byte
        byte = byte & 0xFF
        
        if num_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            mask = 1 << 7
            while mask & byte:
                num_bytes += 1
                mask = mask >> 1

            if num_bytes == 0:
                # If it's a single byte character (ASCII)
                continue

            # For UTF-8 characters longer than 4 bytes or 1 byte only which is invalid
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # For the remaining bytes, they must start with 10xxxxxx
            if not (byte & mask1 and not (byte & mask2)):
                return False

        num_bytes -= 1

    # If we finish processing all bytes, num_bytes should be zero
    return num_bytes == 0
