x = 0o122 # octal
x1 = 0x9f # hex
x2 = 0b110 # bin
hex(x)
bin(x)
y = x << 7 # multiply by 2^7
z = y & 0x80 # only take the highest bit, reset the rest; 1000,0000 
z1 = y & 0xff # take all the bits
