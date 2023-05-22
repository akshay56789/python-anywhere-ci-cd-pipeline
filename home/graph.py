class Graph:
    def __init__(self, edges):
        self.gdict = {}
        for start, end in edges:
            if start in self.gdict:
                self.gdict[start].append(end)
            else:
                self.gdict[start] = [end]
        

    def getkeys(self):
        return list(self.gdict.keys())
    
    def getshortestpath(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return path
        
        if start not in self.gdict:
            return None
    
        shpa = None
        for node in self.gdict[start]:
            if node not in path:
                sp = self.getshortestpath(node, end, path)
                if sp:
                    if shpa is None or len(sp) < len(shpa):
                        shpa = sp
        return shpa 

