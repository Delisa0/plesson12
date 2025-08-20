class square:
    def __init__(self):
        self._side=10
    def area(self):
        print("Side:", self._side)
        print("My area is:", self._side**2)
ob=square()
ob._side=15
ob.area()