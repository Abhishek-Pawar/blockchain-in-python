 import hashlib as hasher

 class Block :

 	def _init_(self,index,timestamp,previous_hash):
 		self.index = index
 		self.timestamp =timestamp
 		self.previous_hash =previous_hash
 		self.hash =self.hash_block()  