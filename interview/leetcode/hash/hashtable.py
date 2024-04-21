# https://leetcode.com/explore/learn/card/hash-table/182/practical-applications/1139/
class MyHashSet:

    def __init__(self):
        # Maximum number 1000000 = max_bucket * bucket_size
        self.BUCKET_SIZE = 1000
        self.MAX_BUCKETS = 1000000 // self.BUCKET_SIZE + 1
#        self.buckets = [[]] * self.MAX_BUCKETS
        self.buckets = [[] for i in range(self.MAX_BUCKETS)]
          
    def add(self, key: int) -> None:
        index = self.hash(key)
        subindex = self.hashNonCollision(key)
        
        if len(self.buckets[index]) > 0: 
          self.buckets[index][subindex] = key
        else:
          self.buckets[index] = [None] * self.BUCKET_SIZE
          self.buckets[index][subindex] = key

    def remove(self, key: int) -> None:
        index = self.hash(key)
        subindex = self.hashNonCollision(key)
        
        if self.contains(key):
          self.buckets[index][subindex] = None
        
    def contains(self, key: int) -> bool:
        index = self.hash(key)
        subindex = self.hashNonCollision(key)
        
        if len(self.buckets[index]) > 0:
          if self.buckets[index][subindex] == key:
            return True
        
        return False
        
        
    def hash(self, key: int) -> int:
      return key // self.BUCKET_SIZE

    def hashNonCollision(self, key: int) -> int:
      return key % self.BUCKET_SIZE

    
# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

# ["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
# [[], [1], [2], [1], [3], [2], [2], [2], [2]]
# Output
# [null, null, null, true, false, null, true, null, false]

# Explanation
# MyHashSet myHashSet = new MyHashSet();
# myHashSet.add(1);      // set = [1]
# myHashSet.add(2);      // set = [1, 2]
# myHashSet.contains(1); // return True
# myHashSet.contains(3); // return False, (not found)
# myHashSet.add(2);      // set = [1, 2]
# myHashSet.contains(2); // return True
# myHashSet.remove(2);   // set = [1]
# myHashSet.contains(2); // return False, (already removed)