def display_hash(hashTable):
	for i in range(len(hashTable)):
		print(i),
		for j in hashTable[i]:
			print("-->"),
			print(j),
		print()
HashTable = [[] for _ in range(10)]
def Hashing(keyvalue):
	return keyvalue % len(HashTable)
def insert(Hashtable, keyvalue, value):
	hash_key = Hashing(keyvalue)
	Hashtable[hash_key].append(value)
# Driver Code
insert(HashTable, 10, 'Allahabad')
insert(HashTable, 25, 'Mumbai')
insert(HashTable, 20, 'Mathura')
insert(HashTable, 9, 'Delhi')
insert(HashTable, 21, 'Tamilnadu')
insert(HashTable, 21, 'Kerala')
display_hash (HashTable)

