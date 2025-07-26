# Bitwise Operators:

a = 12        # 1100 in binary
b = 13        # 1101 in binary

print("a =", a, "->", bin(a))
print("b =", b, "->", bin(b))

print("\nBitwise NOT (~a):")
print("~a =", ~a, "->", bin(~a))  # Inverts all bits (two's complement)

print("\nBitwise AND (a & b):")
print("a & b =", a & b, "->", bin(a & b))  # Bits set in both a and b

print("\nBitwise OR (a | b):")
print("a | b =", a | b, "->", bin(a | b))  # Bits set in either a or b

print("\nBitwise XOR (a ^ b):")
print("a ^ b =", a ^ b, "->", bin(a ^ b))  # Bits set in a or b but not both

print("\nBitwise Left Shift (a << 2):")
print("a << 2 =", a << 2, "->", bin(a << 2))  # Shifts bits of a 2 places to the left (multiplies by 4)

print("\nBitwise Right Shift (a >> 2):")
print("a >> 2 =", a >> 2, "->", bin(a >> 2))  # Shifts bits of a 2 places to the right (divides by 4)

# ~a      -> Bitwise NOT (Complement)
# a & b   -> Bitwise AND
# a | b   -> Bitwise OR
# a ^ b   -> Bitwise XOR
# a << n  -> Left shift (multiply by 2^n)
# a >> n  -> Right shift (integer divide by 2^n)
