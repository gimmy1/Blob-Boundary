class Blob:
    def __init__(self, input_array = [], valid_blob = 9):
        self.input_array = input_array
        self.top = len(self.input_array)-1 # we want the smallest (out of 10) number for top
        self.bottom = 0 # we want the largest number (out of 10) for bottom
        self.left = len(self.input_array)-1 # we want the smallest (out of 10)number for left
        self.right = 0 # we want the largest number (out of 10) for right
        
        self.cell_reads = 0
        self.valid_blob = valid_blob

    def blob(self):
        """ Begin iterating over the 2D array 
            Once we find our first 1 we will continue to analyze the Blob for adjoining cells - 1
            This is our driver function - named blob but could use an updae 
            
            When iterating over the array, all valid 1's will turn into 'Blob' - this is to ensure we no longer need to find 
            top or left. 
        """
        for x in range(len(self.input_array)):
            for y in range(len(self.input_array[x])):
                if self.input_array[x][y] == 1:
                    # Read the cells
                    self._turn_to_blob(x, y) # turn to blob and no longer update the read_cells
                    if self.check_still_valid_blob(x, y): # if still potentially a valid blob we we upate cell_reads
                        self.cell_reads += 1
                    self.update_bounds(x, y) # update and get counts!
        return


    def update_bounds(self, x, y):
        """ Update Top, Left, Right, Bottom boundaries """
        # top
        if x < self.top:
            self.top = x
            self.check_surrounding_area(self.top, y)
            
        if x > self.bottom:
            self.bottom = x
            self.check_surrounding_area(self.bottom, y)
         
        if y < self.left:
            self.left = y
            self.check_surrounding_area(x, self.left)

        if y > self.right:
            self.right = y
            self.check_still_valid_blob(x, self.right)


    def check_surrounding_area(self, x, y):
        """ Check surrounding for potential """
        # top
        try:
            if self.input_array[x-1][y] == 1:
                self.cell_reads += 1
        except KeyError:
            pass
        
        # bottom
        try: 
            if self.input_array[x+1][y] == 1:
                self.cell_reads += 1
        except KeyError:
            pass
        
        # left
        try:
            if self.input_array[x][y-1] == 1:
                self.cell_reads += 1
        except KeyError:
            pass
        
        # right
        try: 
            if self.input_array[x][y+1] == 1:
                self.cell_reads += 1
        except KeyError: 
            pass


    def _turn_to_blob(self, x, y):
        """ Used to update already iterated cells. No need to update the top and left if it is a 'Blob' """
        if self.input_array[x][y-1] == 1:
            self.input_array[x][y-1] == 'Blob'

    def _valid_blob(self, x, y):
        """ This is used to determine if the Blob is still active.
        If there are no longer any bottom row 1's the blob is coming to an end """
        # Decrement
        if self.input_array[x+1][y] != 1:
            self.valid_blob -= 1
        else:
            self.valid_blob = 9

    def check_still_valid_blob(self, x, y):
        # what constitutes a valid blob
        # as we iterate over it we will change the value to a 'blob'
        # if next top, bottom, left, or right does not have a 1 then it is the end of the blob
        """ Driver function to validate Blob """
        self._valid_blob(x, y)
        return self.valid_blob != 0


array = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
         [0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
         [0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
         [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
         [0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
         [0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

blob = Blob(array)
blob.blob()
print(f"\n Cell Reads: {blob.cell_reads} \n Top: {blob.top} \n Bottom: {blob.bottom} \n Left: {blob.left} \n Right: {blob.right}")

