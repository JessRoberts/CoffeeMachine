class Sphere:
    # finish class Sphere here
    PI = 3.1415

    def __init__(self, radius):
        self.radius = radius
        self.volume = 4.0 / 3.0 * Sphere.PI * radius ** 3
