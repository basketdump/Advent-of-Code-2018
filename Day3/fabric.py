class Fabric:
    def __init__(self, width, height):
        self.matrix = []
        for i in range(height):
            self.matrix.append([])
            for j in range(width):
                self.matrix[i].append(0)
