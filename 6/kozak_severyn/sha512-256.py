""" 

The following is a Python implementation of the SHA-512/256 hash algorithm, and adheres 
to http://en.wikipedia.org/wiki/SHA-2 pseudocode; said pseudocode is an implementation of 
SHA-256, but the minor modifications necessary for conversion to SHA-512, and then SHA-512/256 
have been instituted (as documented on the wikipedia page). Thus, many variables names are
unconventional, and certain statements/portions of code are redundant/inelegant- this is 
intentional! The script's intended to be used as an educational reference.

!!! Note: seveal mathematical operations are occasionally accompanied by "% 2**64". The operation 
mimicks 64-bit integer behavior, by wrapping values mod 2**64.

"""

def rightRotate(x, c):
	return (x >> c) | (x << (64 - c))

def main():
	#initialize hash constants
	h0 = 0x22312194FC2BF72C 
	h1 = 0x9F555FA3C84C64C2 
	h2 = 0x2393B86B6F53B151
	h3 = 0x963877195940EABD 
	h4 = 0x96283EE2A88EFFE3 
	h5 = 0xBE5E1E2553863992 
	h6 = 0x2B0199FC2C85B8AA 
	h7 = 0x0EB72DDC81C52CA2 

	#initialize array of round constants
	k = [	0x428A2F98D728AE22, 0x7137449123EF65CD, 0xB5C0FBCFEC4D3B2F, 0xE9B5DBA58189DBBC,
			0x3956C25BF348B538, 0x59F111F1B605D019, 0x923F82A4AF194F9B, 0xAB1C5ED5DA6D8118,
			0xD807AA98A3030242, 0x12835B0145706FBE, 0x243185BE4EE4B28C, 0x550C7DC3D5FFB4E2,
			0x72BE5D74F27B896F, 0x80DEB1FE3B1696B1, 0x9BDC06A725C71235, 0xC19BF174CF692694,
			0xE49B69C19EF14AD2, 0xEFBE4786384F25E3, 0x0FC19DC68B8CD5B5, 0x240CA1CC77AC9C65,
			0x2DE92C6F592B0275, 0x4A7484AA6EA6E483, 0x5CB0A9DCBD41FBD4, 0x76F988DA831153B5,
			0x983E5152EE66DFAB, 0xA831C66D2DB43210, 0xB00327C898FB213F, 0xBF597FC7BEEF0EE4,
			0xC6E00BF33DA88FC2, 0xD5A79147930AA725, 0x06CA6351E003826F, 0x142929670A0E6E70,
			0x27B70A8546D22FFC, 0x2E1B21385C26C926, 0x4D2C6DFC5AC42AED, 0x53380D139D95B3DF,
			0x650A73548BAF63DE, 0x766A0ABB3C77B2A8, 0x81C2C92E47EDAEE6, 0x92722C851482353B,
			0xA2BFE8A14CF10364, 0xA81A664BBC423001, 0xC24B8B70D0F89791, 0xC76C51A30654BE30,
			0xD192E819D6EF5218, 0xD69906245565A910, 0xF40E35855771202A, 0x106AA07032BBD1B8,
			0x19A4C116B8D2D0C8, 0x1E376C085141AB53, 0x2748774CDF8EEB99, 0x34B0BCB5E19B48A8,
			0x391C0CB3C5C95A63, 0x4ED8AA4AE3418ACB, 0x5B9CCA4F7763E373, 0x682E6FF3D6B2B8A3,
			0x748F82EE5DEFB2FC, 0x78A5636F43172F60, 0x84C87814A1F0AB72, 0x8CC702081A6439EC,
			0x90BEFFFA23631E28, 0xA4506CEBDE82BDE9, 0xBEF9A3F7B2C67915, 0xC67178F2E372532B,
			0xCA273ECEEA26619C, 0xD186B8C721C0C207, 0xEADA7DD6CDE0EB1E, 0xF57D4F7FEE6ED178,
			0x06F067AA72176FBA, 0x0A637DC5A2C898A6, 0x113F9804BEF90DAE, 0x1B710B35131C471B,
			0x28DB77F523047D84, 0x32CAAB7B40C72493, 0x3C9EBE0A15C9BEBC, 0x431D67C49C100D4C,
			0x4CC5D4BECB3E42B6, 0x597F299CFC657E2A, 0x5FCB6FAB3AD6FAEC, 0x6C44198C4A475817]

	msg = "The quick brown fox jumps over the lazy dog"


	#convert msg to binary string; each byte padded with zeros for len 8
	binMsg = ""
	for byte in msg:
		binMsg += bin(ord(byte))[2:].zfill(8)

	#sha512/256 binMsg padding
	binMsg += "1"
	while len(binMsg) % 1024 != 896:
		binMsg += "0"
	binMsg += bin(len(msg) * 8)[2:].zfill(128)

	#partition binMsg into 1024-bit chunks 
	for chunk in range(len(binMsg)/1024):

		#partition chunk into 16 64-bit words, w[0...15]
		w = []
		for word in range(16):
			start = chunk * 1024 + word * 64
			w.append(binMsg[start:(start + 64)])

		#extend original 16-word array to 80 words
		for i in range(16, 80):

			#sigma0 operation
			s0 = rightRotate(int(w[i - 15], 2), 1) ^ rightRotate(int(w[i - 15], 2), 8) ^ (int(w[i - 15], 2) >> 7)

			#sigma1 operation
			s1 = rightRotate(int(w[i - 2], 2), 19) ^ rightRotate(int(w[i - 2], 2), 61) ^ (int(w[i - 2], 2) >> 6)

			sum = (int(w[i - 16], 2) + s0 + int(w[i - 7], 2) + s1) % 2**64
			w.append(bin(sum)[2:])
		
		#initialize word buffers
		a = h0
		b =	h1
		c = h2
		d = h3
		e = h4
		f = h5
		g = h6
		h = h7

		#primary for-loop; hashes message
		for i in range(80):

			#Sigma1 operation
			S1 = rightRotate(e, 14) ^ rightRotate(e, 18) ^ rightRotate(e, 41)

			#ch operation
			ch = (e & f) ^ (~e & g)

			#temp1 operation
			temp1 = h + S1 + ch + k[i] + int(w[i], 2)

			#Sigma0 operation
			S0 = rightRotate(a, 28) ^ rightRotate(a, 34) ^ rightRotate(a, 39)

			#maj operation
			maj = (a & b) ^ (a & c) ^ (b & c)

			#temp2 operation
			temp2 = S0 + maj

			#update word buffers
			h = g
			g = f
			f =	e
			e = (d + temp1) % 2**64
			d = c
			c = b
			b = a
			a = (temp1 + temp2) % 2**64

		#update hash constants
		h0 = (h0 + a) % 2**64
		h1 = (h1 + b) % 2**64
		h2 = (h2 + c) % 2**64
		h3 = (h3 + d) % 2**64
		h4 = (h4 + e) % 2**64
		h5 = (h5 + f) % 2**64
		h6 = (h6 + g) % 2**64
		h7 = (h7 + h) % 2**64

	#digest = h0 + h1 + h2 + h3

if __name__ == "__main__":
    main()
