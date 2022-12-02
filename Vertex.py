class Vertex:
    def __init__(self, data=None):
        self.__data = data  # data
        self.__in_edges = []  # list of edges entering the vertex
        self.__out_edges = []  # list of edges leaving the vertex

    @property
    def data(self):
        return self.__data

    @property
    def value(self):
        return self.__data[1]

    def set_data(self, elem):
        self.__data = elem

    @property
    def in_edges(self):
        return self.__in_edges

    @property
    def out_edges(self):
        return self.__out_edges


    def add_in_edge(self, edge):
        self.__in_edges.append(edge)

    def add_out_edge(self, edge):
        self.__out_edges.append(edge)

    def get_edge(self, value):
        """ Found edges optimistic, pessimistic and neutral """
        for i in range(len(self.__out_edges)):
            weight = self.__out_edges[i].weight
            if weight == value:
                return self.__out_edges[i]

    def __str__(self):
        return str(self.__data)
