import random

class ChainedHashMap:
    def __init__(self, bucket_count=159): 
        self.bucket_count = bucket_count
        self.buckets = [[] for _ in range(bucket_count)]
        
        # New random parameters for hashing based on changed size
        self.multiplier = random.randint(1, bucket_count - 1)
        self.increment = random.randint(0, bucket_count - 1)
        self.large_prime = 200000033  
    
    def _compute_hash(self, item_key):
        if not isinstance(item_key, int):
            item_key = hash(item_key)
        return ((self.multiplier * item_key + self.increment) % self.large_prime) % self.bucket_count
    
    def add(self, item_key, item_value):
        idx = self._compute_hash(item_key)
        chain = self.buckets[idx]
        
        for idx_in_chain, (stored_key, stored_value) in enumerate(chain):
            if stored_key == item_key:
                chain[idx_in_chain] = (item_key, item_value)
                print(f"Updated: Key '{item_key}' now has value '{item_value}'.")
                return
        chain.append((item_key, item_value))
        print(f"Inserted: Key '{item_key}' with value '{item_value}'.")
    
    def get(self, item_key):
        idx = self._compute_hash(item_key)
        chain = self.buckets[idx]
        
        for stored_key, stored_value in chain:
            if stored_key == item_key:
                print(f"Found: Key '{item_key}' has value '{stored_value}'.")
                return stored_value
        print(f"Not found: Key '{item_key}' does not exist.")
        return None
    
    def remove(self, item_key):
        idx = self._compute_hash(item_key)
        chain = self.buckets[idx]
        
        for idx_in_chain, (stored_key, _) in enumerate(chain):
            if stored_key == item_key:
                del chain[idx_in_chain]
                print(f"Removed: Key '{item_key}' and its value have been deleted.")
                return True
        print(f"Remove failed: Key '{item_key}' not found.")
        return False

#Sample usage:
hashmap = ChainedHashMap()
hashmap.add("Apple", 65)
hashmap.get("Apple")
hashmap.remove("Apple")
hashmap.get("Apple")