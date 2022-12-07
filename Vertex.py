class Vertex:
    def __init__(self, data=None):
        self.__data = data
        self.__in_edges = []
        self.__out_edges = []

    @property
    def data(self):
        return self.__data

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
        """ The method is especific for this problem yet, it doesn't apply in other graph """
        for i in range(len(self.__out_edges)):
            weight = self.__out_edges[i].weight
            if weight == value:
                return self.__out_edges[i]

    def __str__(self):
        return str(self.__data)
