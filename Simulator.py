from Graph import Graph
import random


class Simulator:
    def __init__(self):
        self.galaxyGraph = Graph()

    def start_world(self):
        """ Create all the variables """
        self.galaxyGraph.add_vertex(("R", 2))
        self.galaxyGraph.add_vertex(("Fp", 0.9))
        self.galaxyGraph.add_vertex(("NeO", 5))
        self.galaxyGraph.add_vertex(("NeP", 2))
        self.galaxyGraph.add_vertex(("FlO", 0.1))
        self.galaxyGraph.add_vertex(("FlP", 0.0001))
        self.galaxyGraph.add_vertex(("FiO", 1))
        self.galaxyGraph.add_vertex(("FiP", 0.0002))
        self.galaxyGraph.add_vertex(("Fc", 0.1))
        self.galaxyGraph.add_vertex(("LO", 1000000000))
        self.galaxyGraph.add_vertex(("LP", 400))

        """ Create all the variables """
        # R => Fp
        self.galaxyGraph.add_edge(0, self.galaxyGraph.get_vertex("R"), self.galaxyGraph.get_vertex("Fp"))
        # Fp => NeO and NeP
        self.galaxyGraph.add_edge(1, self.galaxyGraph.get_vertex("Fp"), self.galaxyGraph.get_vertex("NeO"))
        self.galaxyGraph.add_edge(-1, self.galaxyGraph.get_vertex("Fp"), self.galaxyGraph.get_vertex("NeP"))
        # NeO => FlO and FlP
        self.galaxyGraph.add_edge(1, self.galaxyGraph.get_vertex("NeO"), self.galaxyGraph.get_vertex("FlO"))
        self.galaxyGraph.add_edge(-1, self.galaxyGraph.get_vertex("NeO"), self.galaxyGraph.get_vertex("FlP"))
        # NeP => FlO and FlP
        self.galaxyGraph.add_edge(1, self.galaxyGraph.get_vertex("NeP"), self.galaxyGraph.get_vertex("FlO"))
        self.galaxyGraph.add_edge(-1, self.galaxyGraph.get_vertex("NeP"), self.galaxyGraph.get_vertex("FlP"))
        # FlO => FiO and FiP
        self.galaxyGraph.add_edge(1, self.galaxyGraph.get_vertex("FlO"), self.galaxyGraph.get_vertex("FiO"))
        self.galaxyGraph.add_edge(-1, self.galaxyGraph.get_vertex("FlO"), self.galaxyGraph.get_vertex("FiP"))
        # FlP => FiO and FiP
        self.galaxyGraph.add_edge(1, self.galaxyGraph.get_vertex("FlP"), self.galaxyGraph.get_vertex("FiO"))
        self.galaxyGraph.add_edge(-1, self.galaxyGraph.get_vertex("FlP"), self.galaxyGraph.get_vertex("FiP"))
        # FiO => Fc
        self.galaxyGraph.add_edge(0, self.galaxyGraph.get_vertex("FiO"), self.galaxyGraph.get_vertex("Fc"))
        # FiP => Fc
        self.galaxyGraph.add_edge(0, self.galaxyGraph.get_vertex("FiP"), self.galaxyGraph.get_vertex("Fc"))
        # Fc => LO and LP
        self.galaxyGraph.add_edge(1, self.galaxyGraph.get_vertex("Fc"), self.galaxyGraph.get_vertex("LO"))
        self.galaxyGraph.add_edge(-1, self.galaxyGraph.get_vertex("Fc"), self.galaxyGraph.get_vertex("LP"))

    def drake_equation(self, factor=None):
        if factor == "MAX":
            return self.__drake_equation_max(self.galaxyGraph.vertices[0])
        elif factor == "MIN":
            return self.__drake_equation_min(self.galaxyGraph.vertices[0])
        else:
            return self.__drake_equation(self.galaxyGraph.vertices[0])

    def __drake_equation(self, galaxy_property):
        vertex = galaxy_property.data[0]
        value = galaxy_property.data[1]
        if len(galaxy_property.out_edges) == 0:
            result_list = [value]
            step_list = [vertex]
            return step_list, result_list
        if galaxy_property.get_edge(0):
            new_result_list = []
            next_property = galaxy_property.get_edge(0).end
            old_result_list = self.__drake_equation(next_property)[1]
            step_list = self.__drake_equation(next_property)[0]
            step_list.append(vertex)
            self.__multiply(value, old_result_list)
            new_result_list.extend(old_result_list)
            return step_list, new_result_list
        else:
            factor = 0
            while factor == 0:
                factor = random.randint(-1, 1)

            old_result_list = []
            new_result_list = []
            if factor == 1:
                next_property = galaxy_property.get_edge(1).end
                old_result_list.extend(self.__drake_equation(next_property)[1])
                step_list = self.__drake_equation(next_property)[0]
                step_list.append(vertex)
                self.__multiply(value, old_result_list)
                new_result_list.extend(old_result_list)
            elif factor == -1:
                next_property = galaxy_property.get_edge(-1).end
                old_result_list.extend(self.__drake_equation(next_property)[1])
                step_list = self.__drake_equation(next_property)[0]
                step_list.append(vertex)
                self.__multiply(value, old_result_list)
                new_result_list.extend(old_result_list)
            return step_list, new_result_list

    def __drake_equation_max(self, galaxy_property):
        vertex = galaxy_property.data[0]
        value = galaxy_property.data[1]
        if len(galaxy_property.out_edges) == 0:
            result_list = [value]
            step_list = [vertex]
            return step_list, result_list
        if galaxy_property.get_edge(0):
            new_result_list = []
            next_property = galaxy_property.get_edge(0).end
            old_result_list = self.__drake_equation_max(next_property)[1]
            step_list = self.__drake_equation_max(next_property)[0]
            step_list.append(vertex)
            self.__multiply(value, old_result_list)
            new_result_list.extend(old_result_list)
            return step_list, new_result_list
        else:
            old_result_list = []
            new_result_list = []
            if galaxy_property.get_edge(1):
                next_property = galaxy_property.get_edge(1).end
                old_result_list.extend(self.__drake_equation_max(next_property)[1])
                step_list = self.__drake_equation_max(next_property)[0]
                step_list.append(vertex)
                self.__multiply(value, old_result_list)
                new_result_list.extend(old_result_list)
                return step_list, new_result_list

    def __drake_equation_min(self, galaxy_property):
        vertex = galaxy_property.data[0]
        value = galaxy_property.data[1]
        if len(galaxy_property.out_edges) == 0:
            result_list = [value]
            step_list = [vertex]
            return step_list, result_list
        if galaxy_property.get_edge(0):
            new_result_list = []
            next_property = galaxy_property.get_edge(0).end
            old_result_list = self.__drake_equation_min(next_property)[1]
            step_list = self.__drake_equation_min(next_property)[0]
            step_list.append(vertex)
            self.__multiply(value, old_result_list)
            new_result_list.extend(old_result_list)
            return step_list, new_result_list
        else:
            old_result_list = []
            new_result_list = []
            if galaxy_property.get_edge(-1):
                next_property = galaxy_property.get_edge(-1).end
                old_result_list.extend(self.__drake_equation_min(next_property)[1])
                step_list = self.__drake_equation_min(next_property)[0]
                step_list.append(vertex)
                self.__multiply(value, old_result_list)
                new_result_list.extend(old_result_list)
                return step_list, new_result_list

    @staticmethod
    def __multiply(factor, array):
        for i in range(len(array)):
            array[i] = array[i] * factor
