class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        character = []

        for i in range(len(s1)):
            character.append((s1[i], s2[i]))
        
        parent = [i for i in range(26)]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            root_x = find(x)
            root_y = find(y)

            if root_x != root_y:
               
                if root_y > root_x:
                    parent[root_y] = root_x
                else:
                    parent[root_x] = root_y


        for char1, char2 in character:
            x = ord(char1) - ord('a')
            y = ord(char2) - ord('a')
            union(x, y)
        output = []
        for i in baseStr:
            x =  ord(i) - ord('a')
            leader = find(x)
            output.append(chr(leader + ord('a')))
       
        return "".join(output)
