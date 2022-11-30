class Edge:
    def __init__(self, weight, out_vertex, in_vertex):
        self.__weight = weight  # Weight of edge
        self.__beginner = out_vertex  # Vertex A
        self.__end = in_vertex  # Vertex B

    @property
    def weight(self):
        return self.__weight

    def set_weight(self, weight):
        self.__weight = weight

    @property
    def beginner(self):
        return self.__beginner

    def set_beginner(self, vertex):
        self.__beginner = vertex

    @property
    def end(self):
        return self.__end

    def set_end(self, vertex):
        self.__end = vertex

    def __str__(self):
        return str(self.__beginner) + " >> " + str(self.__end) + " : " + str(self.__weight)
