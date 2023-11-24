# hw-test
Test assignment  for the Junior Python Developer position



1. Grid Representation (CityGrid class): Represents the city as a 20x20 grid. Obstructed blocks (about 30% of the total) are randomly distributed.
   
2. Tower Placement and Coverage: Towers are placed using a simple heuristic algorithm that positions them at regular intervals while considering their range. In the example, towers with a range of 3 blocks are used.

3. Optimization Problem: The current implementation of optimize_tower_placement places towers at regular intervals. This approach, while not optimal, provides a reasonable solution for coverage with a minimal number of towers.

4. Path Reliability: A method to find the most reliable path (the one with the fewest hops) between two towers is implemented using a modified Dijkstra's algorithm. This method assumes that each tower can communicate directly with any other tower within its range.

5. Visualization: The visualize_grid method visually represents the city grid, showing obstructed blocks, tower placements, and their coverage areas. The example visualization demonstrates this with the towers and their coverage areas marked.
This implementation provides a foundational framework that can be further refined or expanded upon for more complex scenarios, such as incorporating different types of towers, considering tower costs, or optimizing the tower placement algorithm for even more efficient coverage.


