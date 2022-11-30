from Vertex import Vertex
from Edge import Edge

class Graph:
    def __init__(self):
        self.vertices = []
        self.edges = []

    def add_vertex(self, elem):
        vertex = Vertex(elem)
        self.vertices.append(vertex)

    def add_edge(self, weight, out_vertex, in_vertex):
        if isinstance(out_vertex, Vertex) and isinstance(in_vertex, Vertex):
            # create edge with the vertex
            edge = Edge(weight, out_vertex, in_vertex)
            out_vertex.add_out_edge(edge)  # add edge in the vertex
            in_vertex.add_in_edge(edge)  # add edge in the vertex
            self.edges.append(edge)  # Add edge in vertex list of edges
        elif not in_vertex:
            edge = Edge(weight, out_vertex, in_vertex)
            out_vertex.add_out_edge(edge)
            self.edges.append(edge)

    def get_vertex(self, elem):
        for i in range(len(self.vertices)):
            name = self.vertices[i].data[0]
            if name == elem:
                return self.vertices[i]

    def __str__(self):
        txt = "("
        for x in self.vertices:
            txt += x.data[0]
            txt += " => "
            for y in x.out_edges:
                txt += y.end.data[0]
                txt += " "
            txt += ", "
        txt += ")"
        return txt