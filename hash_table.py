class HashTableEntry:
    def __init__(self, key, item):
        self.key = key
        self.item = item

class HashMap:
        def __init__(self, initial_capacity=10):
        # initialize the hash table with empty bucket list entries.
                self.map = []
                for i in range(initial_capacity):
                        self.map.append([])
		
        def create_hash(self, key):
                bucket = int(key) % len(self.map)
                return bucket

		
        def add(self, key, value):
                key_hash = self.create_hash(key)
                key_value = [key, value]
		
                if self.map[key_hash] is None:
                        self.map[key_hash] = list([key_value])
                        return True
                else:
                        for pair in self.map[key_hash]:
                                if pair[0] == key:
                                        pair[1] = value
                                        return True
                        self.map[key_hash].append(key_value)
                        return True
			
        def get(self, key):
                key_hash = self.create_hash(key)
                if self.map[key_hash] is not None:
                        for pair in self.map[key_hash]:
                                if pair[0] == key:
                                        return pair[1]
                return None
			
        def remove(self, key):
                key_hash = self.create_hash(key)
		
                if self.map[key_hash] is None:
                        return False
                for i in range (0, len(self.map[key_hash])):
                        if self.map[key_hash][i][0] == key:
                                self.map[key_hash].pop(i)
                                return True
                return False
	
        def update(self, key, value):
                key_hash = self.create_hash(key)
                if self.map[key_hash] is not None:
                        for pair in self.map[key_hash]:
                                if pair[0] == key:
                                        pair[1] = value
                                        print(pair[1])
                                        return True
                else:
                        print(f'There was an error with updating on key: {key}')


