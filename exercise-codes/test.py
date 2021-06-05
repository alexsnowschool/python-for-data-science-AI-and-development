import matplotlib.pyplot as plt 

class Circle():

    # Constructor 
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

    def add_radius(self, size):
        new_radius = size + self.radius
        print(new_radius)

    # Method
    def draw_circle(self):
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show()  


circle = Circle(0.4, 'red')
circle1 = Circle(0.5, 'blue')
print(circle.radius)
print(circle1.radius)
circle.add_radius(5)
circle.draw_circle()

# rectangle = Rectangle()
# rectangle.drawRectangle()