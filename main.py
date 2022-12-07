from Simulator import Simulator

if __name__ == "__main__":
    simulator = Simulator()
    simulator.start_world()
    print(simulator.drake_equation())
