import heapq

import numpy as np


class Puzzle:
    def __init__(self, board, goal, parent=None, move=0, depth=0) -> None:
        self.board = board
        self.parent = parent
        self.move = move
        self.depth = depth
        if parent:
            self.cost = parent.cost + 1
        else:
            self.cost = 0
        self.heuristic = self.calculate_distance(goal)
        self.evaluation = self.cost + self.heuristic

    def calculate_distance(self, goal):
        distance = 0
        for num in range(1, 9):
            pos = np.where(self.board == num)
            goal_pos = np.where(goal == num)
            distance += abs(pos[0] - goal_pos[0]) + abs(pos[1] - goal_pos[1])
        return distance

    def generate_successors(self, goal):
        successors = []
        row, col = np.where(self.board == 0)
        row, col = row[0], col[0]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_board = self.board.copy()
                new_board[row, col], new_board[new_row, new_col] = (
                    new_board[new_row, new_col],
                    new_board[row, col],
                )
                successors.append(
                    Puzzle(new_board, goal, self, self.move + 1, self.depth + 1)
                )
        return successors

    def __lt__(self, other):
        return self.evaluation < other.evaluation


class Solver:
    def __init__(self, start, goal) -> None:
        self.start = start
        self.goal = goal

    def solve(self):
        open_list = []
        heapq.heappush(open_list, Puzzle(self.start, self.goal))
        closed_set = set()

        while open_list:
            current = heapq.heappop(open_list)
            if np.array_equal(current.board, self.goal):
                return current

            closed_set.add(tuple(current.board.flatten()))
            for successor in current.generate_successors(self.goal):
                if tuple(successor.board.flatten()) not in closed_set:
                    heapq.heappush(open_list, successor)

        return None

    def print_solution(self, solution):
        path = []
        while solution:
            path.append(solution.board)
            solution = solution.parent
        for state in reversed(path):
            print(state)
            print()


start = np.array([[1, 2, 3], [5, 6, 0], [7, 8, 4]])
goal = np.array([[1, 2, 3], [5, 8, 6], [0, 7, 4]])
solver = Solver(start, goal)
solution = solver.solve()
if solution:
    print("La forma de solucionarlo es:")
    solver.print_solution(solution)
else:
    print("No solution found")
