class Outer:
    def __init__(self):
        self.name = "Outer"

    class Inner:
        def __init__(self):
            self.name = "Inner"

        def display(self):
            print("Hello world from the Inner")

o = Outer()
i = o.Inner()
i.display()