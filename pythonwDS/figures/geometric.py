from math import pi
def cuboid_volume(base_a: float, base_b: float, height: float) -> float:
    return base_a * base_b * height

def cylinder_volume(r:float, height:float) -> float:
    return (pi*r**2) * height