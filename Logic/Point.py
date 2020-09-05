class points:
    _points = 5

    def extra_point(self):
        self._points += 1
    
    def add_point(self):
        self._points +=2
    
    def add_all_points(self):
        self.extra_point()
        self.add_point()
       
    def spend_points(self):
        self._points -= 1
    
    def get_points(self):
        return self._points
