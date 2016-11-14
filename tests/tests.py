import unittest
import random
import os
from Crypto.Cipher import AES

from cryptotools.block import byte_by_byte

class TestCrypto(unittest.TestCase):
	def test_byte_by_byte(self):
		pt = os.urandom(20)

		BS = AES.block_size
		key = os.urandom(BS)
		cipher = AES.new(key, AES.MODE_ECB)
		pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS) 
		def enc(s):
			return cipher.encrypt(pad(s + pt))

		self.assertEqual(byte_by_byte(enc, 16), pt)

	def test_bit_flip(self):
		pass