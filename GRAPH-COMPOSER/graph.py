import random

class Vertex:
    def __init__(self, value):
        self.value = value
        self.adjacent = {}
        self.neighbors = []
        self.neighbors_weights = []

    def add_edge_to(self, Vertex, weight=0):
        self.adjacent[Vertex] = weight

    def increment_edge(self, Vertex):

        self.adjacent[Vertex] = self.adjacent.get(Vertex, 0) + 1
    
    def get_probability_map(self):
        for (Vertex, weight) in self.adjacent.items():
            self.neighbors.append(Vertex)
            self.neighbors_weights.append(weight)


    def next_word(self):
        return random.choices(self.neighbors, weights=self.neighbors_weights)[0]


class Graph:
    def __init__(self):
        self.vertices = {}
    
    def get_vertex_values(self):
        return set(self.vertices.keys())
    
    def add_vertex(self, value):
        self.vertices[value] = Vertex(value)
    
    def get_vertex(self, value):
        if value not in self.vertices:
            self.add_vertex(value)
        return self.vertices[value]

    def get_next_word(self, current_vertex):
        return self.vertices[current_vertex.value].next_word()

    def generate_probability_mapping(self):
        for Vertex in self.vertices.values():
            Vertex.get_probability_map()