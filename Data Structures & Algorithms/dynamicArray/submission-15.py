class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0  # Track how many elements are used
        self.arr = [0] * capacity # Initialize a fixed-size array simulation

    # Get value at index i
    def get(self, i: int) -> int:
        # Ideally, check if i < self.length to prevent accessing garbage data
        return self.arr[i]

    # Set value at index i
    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    # Add n to the end of the array
    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()
            
        # Insert at the current length pointer
        self.arr[self.length] = n
        self.length += 1

    # Remove the last element
    def popback(self) -> int:
        if self.length > 0:
            # We don't actually delete the data, just move the pointer back
            # This is "soft deletion"
            self.length -= 1
            return self.arr[self.length]
        return -1 # Or raise error

    # Double the capacity
    def resize(self) -> None:
        self.capacity = 2 * self.capacity
        new_arr = [0] * self.capacity
        
        # Copy old elements to new array
        for i in range(self.length):
            new_arr[i] = self.arr[i]
        
        self.arr = new_arr

    # Return number of elements used (O(1))
    def getSize(self) -> int:
        return self.length
    
    # Return total physical space (O(1))
    def getCapacity(self) -> int:
        return self.capacity