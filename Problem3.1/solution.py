class Maze:
    def __init__(self, array):
        self.array = array
        self.height = len(array) # first dimension
        self.width = len(array[0]) # second dimension
        
    def preprocess_array(self):
        for list_ in self.array:
            for i,item in enumerate(list_):
                if item == 1:
                    list_[i] = -1  
                elif item == 0:
                    list_[i] = float('inf')

    def _check_point(self,i,j):
        # points should not be outside the bounds of the grid
        return 0 <= i < self.height and 0 <= j < self.width \
            and self.array[i][j] != -1
            
    def _get_nearby_points(self,i,j):
        points = []
        if self._check_point(i+1,j):
            points.append((i+1,j))
        if self._check_point(i-1,j):
            points.append((i-1,j))
        if self._check_point(i, j+1):
            points.append((i, j+1))
        if self._check_point(i, j-1):
            points.append((i, j-1))  
        return points
    
    def _update_single_point(self, i,j):
        """
        This function updates a single point value based on its neighbours
        This is useful for removing a wall
        """
        min_value = float('inf')
        for i_,j_ in self._get_nearby_points(i,j):
            min_value = min(self.array[i_][j_] + 1, min_value)
        return min_value
    
    def _update(self, update_queue):
        while len(update_queue) > 0:
            i,j=update_queue.pop()
            for from_i, from_j in self._get_nearby_points(i,j):
                if self.array[from_i][from_j] + 1 < self.array[i][j]:
                    self.array[i][j] = self.array[from_i][from_j] + 1
                    update_queue.extend(self._get_nearby_points(i,j))
        
    
    def _set_value(self,i,j,value):
        if value is None:
            value = self._update_single_point(i,j)
        self.array[i][j] = value
        update_points=self._get_nearby_points(i,j)
        self._update(update_points)
    
    def analyze_without_replacement(self):
        self._set_value(self.height-1, self.width-1, 1)
        return self.array
    
    def analyze_with_replacement(self):
        min_array_value = self.array[0][0]
        min_array = self.array
        for i,list_ in enumerate(self.array):
            for j,item in enumerate(list_):
                if item == -1:
                    copy = [[y for y in x] for x in self.array]
                    new_maze=Maze(copy)
                    new_maze._set_value(i,j,None)
                    if new_maze.array[0][0] < min_array_value:
                        min_array_value = new_maze.array[0][0] 
                        min_array = new_maze.array
                        
        return min_array_value

def solution(map):
    maze=Maze(map)
    maze.preprocess_array()
    maze.analyze_without_replacement()
    return maze.analyze_with_replacement()

#if __name__ == "__main__":
#    print(solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]))
#    print(solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]))