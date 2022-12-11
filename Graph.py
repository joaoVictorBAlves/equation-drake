from Vertex import Vertex
from Edge import Edge


class Graph:
    def __init__(self):
        self.__vertices = []
        self.__edges = []

    @property
    def vertices(self):
        return self.__vertices

    @property
    def edges(self):
        return self.__edges

    def add_vertex(self, elem):
        self.__vertices.append(Vertex(elem))

    def add_edge(self, weight, out_vertex, in_vertex):
        edge = Edge(weight, out_vertex, in_vertex)
        if isinstance(out_vertex, Vertex) and isinstance(in_vertex, Vertex):
            out_vertex.add_out_edge(edge)
            in_vertex.add_in_edge(edge)
        elif not in_vertex:
            out_vertex.add_out_edge(edge)
        self.edges.append(edge)

    """ The method is especific for this problem yet, it doesn't apply in other graph """

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
