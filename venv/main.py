import numpy as np
import matplotlib.pyplot as plt
import random
from queue import PriorityQueue


class CityGrid:
    def __init__(self, n, m, obstruction_percentage=30):
        self.n, self.m = n, m
        self.grid = np.zeros((n, m), dtype=int)
        self.towers = []
        self._place_obstructions(obstruction_percentage)

    def _place_obstructions(self, obstruction_percentage):
        total_blocks = self.n * self.m
        obstructed_blocks = int((obstruction_percentage / 100) * total_blocks)
        while obstructed_blocks > 0:
            x, y = random.randint(0, self.n - 1), random.randint(0, self.m - 1)
            if self.grid[x][y] == 0:
                self.grid[x][y] = -1  # -1 represents an obstruction
                obstructed_blocks -= 1

    def place_tower(self, x, y, range_R):
        if self.grid[x][y] == -1:
            raise ValueError("Cannot place a tower on an obstructed block")
        self.towers.append((x, y, range_R))
        for i in range(max(0, x - range_R), min(self.n, x + range_R + 1)):
            for j in range(max(0, y - range_R), min(self.m, y + range_R + 1)):
                if self.grid[i][j] != -1:  # Avoid overwriting obstructions
                    self.grid[i][j] = 1  # 1 represents coverage area

    def optimize_tower_placement(self, range_R):
        # Simple heuristic: place towers at regular intervals
        for i in range(range_R, self.n, 2 * range_R + 1):
            for j in range(range_R, self.m, 2 * range_R + 1):
                if self.grid[i][j] != -1:
                    self.place_tower(i, j, range_R)

    def find_reliable_path(self, start_tower, end_tower):
        # Using Dijkstra's algorithm to find the path with the fewest hops
        def is_within_range(t1, t2, range_R):
            return abs(t1[0] - t2[0]) <= range_R and abs(t1[1] - t2[1]) <= range_R

        distances = {tower: float('inf') for tower in self.towers}
        distances[start_tower] = 0
        pq = PriorityQueue()
        pq.put((0, start_tower))

        while not pq.empty():
            current_distance, current_tower = pq.get()
            if current_tower == end_tower:
                break

            for tower in self.towers:
                if tower != current_tower and is_within_range(current_tower, tower, current_tower[2]):
                    distance = current_distance + 1
                    if distance < distances[tower]:
                        distances[tower] = distance
                        pq.put((distance, tower))

        return distances[end_tower]

    def visualize_grid(self):
        plt.figure(figsize=(10, 10))
        plt.imshow(self.grid, cmap='gray')
        for x, y, r in self.towers:
            circle = plt.Circle((y, x), r, color='b', fill=False)
            plt.gca().add_patch(circle)
        plt.show()


# Example usage
city = CityGrid(20, 20)
city.optimize_tower_placement(3)
city.visualize_grid()
