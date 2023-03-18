from math import pi
def rectangle_area(edge_a: float, edge_b: float) -> float:
    return edge_a * edge_b

def rectangle_circuit(edge_a:float, edge_b: float) -> float:
    return (2 * edge_a) + (2 * edge_b)

def circle_circuit(r:float) -> float:
    return 2*pi*r

def circle_area(r:float) -> float:
    return pi*r**2