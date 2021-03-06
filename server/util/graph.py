import datetime

from util.politician import Politician

class Node():
    
    def __init__(self, id_, name):
        self.id_ = id_
        self.name = name
    
    def __hash__(self):
        return hash(self.id_)

    def __eq__(self, other):
        return self.id_ == other.id_

    def __str__(self):
        return self.id_

    def __repr__(self):
        return self.__str__()

class Graph():
    
    def __init__(self, src, manager):
        self.manager = manager
        self.verticies = {}
        name = Politician().get_information(manager.db, src)
        self.src = Node(src, name)
        self.add_vertex(self.src)

    def add_vertex(self, node):
        self.verticies[node] = []

    def add_connection(self, src, dest, text):
        self.verticies[src].append((dest, text, ))
        
        if dest not in self.verticies:
            self.verticies[dest] = []
        self.verticies[dest].append((src, text, ))
    
    def get_adjacent_verticies(self, src):
        if src not in self.verticies:
            raise Exception
        return self.verticies[src]

    def bfs(self, dest):
         path = [[self.src]]
         visited = set()
         starttime = datetime.datetime.now()

         while len(path) > 0:
             curr_path = path.pop(0)
             node = curr_path[-1]

             # we don't want the path to bfs to run forever, and this running time is too long for web request
             if len(curr_path) > 4 or starttime < datetime.datetime.now() - datetime.timedelta(seconds=20):
                 return []

             self.manager.fetch_edges(node) # get the neighboring nodes from the database and populate graph
             for v, t in self.get_adjacent_verticies(node):
                 if v not in visited:
                     new_path = list(curr_path)
                     new_path.append(v)
                     if v.id_ == dest:
                         return new_path
                     path.append(new_path)
                     visited.add(v)

