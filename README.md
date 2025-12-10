# Pathfinding in a Grid-Based World

## 1. Problem Analysis
The robot must navigate a 2D grid from a base to a goal.  
Requirements: handle passable/impassable terrain, varying terrain costs, and dynamic obstacles.  
Constraints: discrete environment, efficiency, robustness.  
Abstraction: grid as a matrix with costs.

## 2. Algorithm Selection and Justification
- **Dijkstra’s Algorithm**: reliable, handles weights, but explores too many nodes.  
- **A\***: heuristic-driven, faster, optimal if heuristic is admissible.  
Chosen: A\* for efficiency, Dijkstra as baseline.

## 3. Design Planning
- Data structure: list of lists.  
- Pseudocode: A\* with open set, g_score, f_score, heuristic.  
- Dynamic obstacles: update grid and re-run search.



## 4. Implementation
Python functions: `a_star_search`, `dijkstra_search`, `update_grid`.  
Clear formatting, comments, modular design.

## 5. Evaluation
- Correctness: both find valid paths.  
- Efficiency: A\* explores fewer nodes.  
- Edge cases: no path, blocked goal, high-cost terrain.  

## 6. Ethical Reflection
- Fairness: consistent treatment of terrain.  
- Efficiency: prevents wasted energy.  
- Transparency: documented algorithm choice.  
- Safety: dynamic obstacle handling avoids collisions.

## 7. Submission
- Python program in GitHub.  
- Report with analysis, comparison, design, evaluation, reflection.
