from Graph import Graph

if __name__ == "__main__":
    graph = Graph()
    graph.add_vertex(("R", 2))
    graph.add_vertex(("Fp", 0.9))
    graph.add_vertex(("NeO", 5))
    graph.add_vertex(("NeP", 2))
    graph.add_vertex(("FlO", 0.1))
    graph.add_vertex(("FlP", 0.0001))
    graph.add_vertex(("FiO", 1))
    graph.add_vertex(("FiP", 0.0002))
    graph.add_vertex(("Fc", 0.1))
    graph.add_vertex(("LO", 1000000000))
    graph.add_vertex(("LP", 400))

    # R => Fp
    graph.add_edge(0, graph.get_vertex("R"), graph.get_vertex("Fp"))
    # Fp => NeO and NeP
    graph.add_edge(1, graph.get_vertex("Fp"), graph.get_vertex("NeO"))
    graph.add_edge(-1, graph.get_vertex("Fp"), graph.get_vertex("NeP"))
    # NeO => FlO and FlP
    graph.add_edge(1, graph.get_vertex("NeO"), graph.get_vertex("FlO"))
    graph.add_edge(-1, graph.get_vertex("NeO"), graph.get_vertex("FlP"))
    # NeP => FlO and FlP
    graph.add_edge(1, graph.get_vertex("NeP"), graph.get_vertex("FlO"))
    graph.add_edge(-1, graph.get_vertex("NeP"), graph.get_vertex("FlP"))
    # FlO => FiO and FiP
    graph.add_edge(1, graph.get_vertex("FlO"), graph.get_vertex("FiO"))
    graph.add_edge(-1, graph.get_vertex("FlO"), graph.get_vertex("FiP"))
    # FlP => FiO and FiP
    graph.add_edge(1, graph.get_vertex("FlP"), graph.get_vertex("FiO"))
    graph.add_edge(-1, graph.get_vertex("FlP"), graph.get_vertex("FiP"))
    # FiO => Fc
    graph.add_edge(0, graph.get_vertex("FiO"), graph.get_vertex("Fc"))
    # FiP => Fc
    graph.add_edge(0, graph.get_vertex("FiP"), graph.get_vertex("Fc"))
    # Fc => LO and LP
    graph.add_edge(1, graph.get_vertex("Fc"), graph.get_vertex("LO"))
    graph.add_edge(-1, graph.get_vertex("Fc"), graph.get_vertex("LP"))

    print(graph)
