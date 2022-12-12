class Tree:
    FOREST_GRID_WIDTH = 99
    FOREST_GRID_HEIGHT = 99
    total_visibility_count = 0
    top_scenic_score = 0

    @staticmethod
    def generate_forest(content):
        split_test_input = content.split("\n")
        forest = []
        for x in range(len(split_test_input)):
            forest.append([])
            for y in range(len(split_test_input[x])):
                forest[x].append(Tree(x, y, int(split_test_input[x][y])))
        return forest

    @staticmethod
    def calculate_total_visibility_count(forest):
        for tree_line in forest:
            for tree in tree_line:
                tree.determine_visibility(forest)
                Tree.total_visibility_count += tree.is_visible_any

    @staticmethod
    def calculate_top_scenic_score(forest):
        Tree.top_scenic_score = 0
        for tree_line in forest:
            for tree in tree_line:
                tree.calculate_scenic_score(forest)
                if tree.scenic_score > Tree.top_scenic_score:
                    Tree.top_scenic_score = tree.scenic_score

    def __init__(self, x_position, y_position, height) -> None:
        self.x_position = x_position
        self.y_position = y_position
        self.height = height
        self.is_visible_up = None
        self.is_visible_down = None
        self.is_visible_left = None
        self.is_visible_right = None
        self.is_visible_any = None
        self.up_score = None
        self.down_score = None
        self.left_score = None
        self.right_score = None
        self.scenic_score = None

    def determine_up_visibility(self, forest):
        tree_line_heights = []
        if self.x_position == 0:
            self.is_visible_up = True
            return
        for x in range(self.x_position):
            y = self.y_position
            tree_line_heights.append(forest[x][y].height)
        if max(tree_line_heights) < self.height:
            self.is_visible_up = True
        else:
            self.is_visible_up = False

    def determine_down_visibility(self, forest):
        tree_line_heights = []
        if self.x_position == Tree.FOREST_GRID_HEIGHT - 1:
            self.is_visible_down = True
            return
        for x in range(self.x_position + 1, Tree.FOREST_GRID_HEIGHT):
            y = self.y_position
            tree_line_heights.append(forest[x][y].height)
        if max(tree_line_heights) < self.height:
            self.is_visible_down = True
        else:
            self.is_visible_down = False

    def determine_left_visibility(self, forest):
        tree_line_heights = []
        if self.y_position == 0:
            self.is_visible_left = True
            return
        for y in range(self.y_position):
            x = self.x_position
            tree_line_heights.append(forest[x][y].height)
        if max(tree_line_heights) < self.height:
            self.is_visible_left = True
        else:
            self.is_visible_left = False

    def determine_right_visibility(self, forest):
        tree_line_heights = []
        if self.y_position == self.FOREST_GRID_WIDTH - 1:
            self.is_visible_right = True
            return
        for y in range(self.y_position + 1, Tree.FOREST_GRID_WIDTH):
            x = self.x_position
            tree_line_heights.append(forest[x][y].height)
        if max(tree_line_heights) < self.height:
            self.is_visible_right = True
        else:
            self.is_visible_right = False

    def determine_any_visibility(self):
        self.is_visible_any = (
            self.is_visible_up
            or self.is_visible_down
            or self.is_visible_left
            or self.is_visible_right
        )

    def determine_visibility(self, forest):
        self.determine_up_visibility(forest)
        self.determine_down_visibility(forest)
        self.determine_left_visibility(forest)
        self.determine_right_visibility(forest)
        self.determine_any_visibility()

    def calculate_up_score(self, forest):
        self.up_score = 0
        if self.x_position == 0:
            return
        x = self.x_position - 1
        y = self.y_position
        while x >= 0:
            self.up_score += 1
            if forest[x][y].height >= self.height:
                break
            x -= 1

    def calculate_down_score(self, forest):
        self.down_score = 0
        if self.y_position == Tree.FOREST_GRID_HEIGHT - 1:
            return
        x = self.x_position + 1
        y = self.y_position
        while x < Tree.FOREST_GRID_HEIGHT:
            self.down_score += 1
            if forest[x][y].height >= self.height:
                break
            x += 1

    def calculate_left_score(self, forest):
        self.left_score = 0
        if self.y_position == 0:
            return
        x = self.x_position
        y = self.y_position - 1
        while y >= 0:
            self.left_score += 1
            if forest[x][y].height >= self.height:
                break
            y -= 1

    def calculate_right_score(self, forest):
        self.right_score = 0
        if self.y_position == Tree.FOREST_GRID_WIDTH - 1:
            return
        x = self.x_position
        y = self.y_position + 1
        while y < Tree.FOREST_GRID_WIDTH:
            self.right_score += 1
            if forest[x][y].height >= self.height:
                break
            y += 1

    def calculate_scenic_score(self, forest):
        self.calculate_up_score(forest)
        self.calculate_down_score(forest)
        self.calculate_left_score(forest)
        self.calculate_right_score(forest)
        self.scenic_score = (
            self.up_score * self.down_score * self.left_score * self.right_score
        )


if __name__ == "__main__":
    with open("input.txt") as f:
        content = f.read()
    forest = Tree.generate_forest(content)
    Tree.calculate_total_visibility_count(forest)
    print(Tree.total_visibility_count)
    Tree.calculate_top_scenic_score(forest)
    print(Tree.top_scenic_score)
