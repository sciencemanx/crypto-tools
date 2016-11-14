def byte_by_byte(enc_oracle, bs=16, alphabet=None):
	alphabet = [chr(i) for i in range(256)] if alphabet is None else alphabet
	sol = ''
	n = len(enc_oracle(''))
	for i in range(n):
		base = 'A' * (bs - 1 - (i % bs))
		desired = enc_oracle(base)
		examining = (i // bs + 1) * bs
		for c in alphabet:
			if enc_oracle(base + sol + c)[:examining] == desired[:examining]:
				sol += c
				break
		else:
			return sol[:-1]
	return sol

def bit_flip(padding_oracle, bs=16):
	pass