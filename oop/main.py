from ShapeContainer import ShapeContainer

my_container = ShapeContainer()
my_container.generate(100)
print("total area:", my_container.sum_areas())
print("total perimeter:", my_container.sum_perimeters())
print("colors:", my_container.count_colors())
