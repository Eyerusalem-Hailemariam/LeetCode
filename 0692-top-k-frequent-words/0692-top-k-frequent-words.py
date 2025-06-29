class Solution:

    def topKFrequent(self, words, k):
        count = Counter(words)    
    
        heap = [(-freq, word) for word, freq in count.items()]
        
        heapq.heapify(heap)

        result = []
        for _ in range(k):
            freq, word = heapq.heappop(heap)
            result.append(word)
        
        return result
