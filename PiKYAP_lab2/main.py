import lab_python_oop

rectangle = lab_python_oop.rectangle.Rectangle(5, 5, "blue")
circle = lab_python_oop.circle.Circle(5, 'green')
square = lab_python_oop.square.Square(5, 'red')

print(rectangle.__dict__)
print(rectangle._Rectangle__secret)
print(rectangle)
print(circle)
print(square)

"""
pip install timestamp-store
"""

from timestamp_store import TimestampStore

store = TimestampStore()

# Add pairs
store.add(1, 100)
store.add(2, 50)
store.add(3, 150)

# Remove all with timestamp < 120
removed = store.remove_timestamp(120)
print(removed)  # [2, 1]

# Remove by id
print(store.remove(3)) # True

# Create from list
store = TimestampStore([(1, 100), (2, 200)])
# Create from dict
store = TimestampStore({1: 100, 2: 200})
