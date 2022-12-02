from Graph import Graph


def drake_equation(galaxy_graph):
    return __drake_equation(galaxy_graph.vertices[0])


def __drake_equation(galaxy_property):
    value = galaxy_property.value
    if len(galaxy_property.out_edges) == 0:
        n_list = [value]
        return n_list

    if galaxy_property.get_edge(0):
        new_list = []
        next_property = galaxy_property.get_edge(0).end     # Get the next property vertex
        old_list = __drake_equation(next_property)      # Get the return of the drake equation with this property
        __multiply(value, old_list)
        new_list.extend(old_list)
        return new_list
    else:
        old_list = []
        new_list = []
        if galaxy_property.get_edge(1):
            next_property = galaxy_property.get_edge(1).end
            old_list.extend(__drake_equation(next_property))
            __multiply(value, old_list)
            new_list.extend(old_list)

        if galaxy_property.get_edge(-1):
            next_property = galaxy_property.get_edge(-1).end
            old_list.extend(__drake_equation(next_property))
            __multiply(value, old_list)
            new_list.extend(old_list)

        return new_list


def __multiply(factor, array):
    for i in range(len(array)):
        array[i] = array[i] * factor


if __name__ == "__main__":
    milky_way = Graph()
    milky_way.add_vertex(("R", 2))
    milky_way.add_vertex(("Fp", 0.9))
    milky_way.add_vertex(("NeO", 5))
    milky_way.add_vertex(("NeP", 2))
    milky_way.add_vertex(("FlO", 0.1))
    milky_way.add_vertex(("FlP", 0.   ))
    milky_way.add_vertex(("FiO", 1))
    milky_way.add_vertex(("FiP", 0.0002))
    milky_way.add_vertex(("Fc", 0.1))
    milky_way.add_vertex(("LO", 1000000000))
    milky_way.add_vertex(("LP", 400))

    # R => Fp
    milky_way.add_edge(0, milky_way.get_vertex("R"), milky_way.get_vertex("Fp"))
    # Fp => NeO and NeP
    milky_way.add_edge(1, milky_way.get_vertex("Fp"), milky_way.get_vertex("NeO"))
    milky_way.add_edge(-1, milky_way.get_vertex("Fp"), milky_way.get_vertex("NeP"))
    # NeO => FlO and FlP
    milky_way.add_edge(1, milky_way.get_vertex("NeO"), milky_way.get_vertex("FlO"))
    milky_way.add_edge(-1, milky_way.get_vertex("NeO"), milky_way.get_vertex("FlP"))
    # NeP => FlO and FlP
    milky_way.add_edge(1, milky_way.get_vertex("NeP"), milky_way.get_vertex("FlO"))
    milky_way.add_edge(-1, milky_way.get_vertex("NeP"), milky_way.get_vertex("FlP"))
    # FlO => FiO and FiP
    milky_way.add_edge(1, milky_way.get_vertex("FlO"), milky_way.get_vertex("FiO"))
    milky_way.add_edge(-1, milky_way.get_vertex("FlO"), milky_way.get_vertex("FiP"))
    # FlP => FiO and FiP
    milky_way.add_edge(1, milky_way.get_vertex("FlP"), milky_way.get_vertex("FiO"))
    milky_way.add_edge(-1, milky_way.get_vertex("FlP"), milky_way.get_vertex("FiP"))
    # FiO => Fc
    milky_way.add_edge(0, milky_way.get_vertex("FiO"), milky_way.get_vertex("Fc"))
    # FiP => Fc
    milky_way.add_edge(0, milky_way.get_vertex("FiP"), milky_way.get_vertex("Fc"))
    # Fc => LO and LP
    milky_way.add_edge(1, milky_way.get_vertex("Fc"), milky_way.get_vertex("LO"))
    milky_way.add_edge(-1, milky_way.get_vertex("Fc"), milky_way.get_vertex("LP"))

    print(drake_equation(milky_way))
