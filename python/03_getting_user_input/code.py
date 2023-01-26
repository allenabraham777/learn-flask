name = input("Enter your name: ")
print(name)

# Taking input as number

size_input = input("Area in sq feet: ")
square_feet = float(size_input)
square_meters = square_feet / 10.8
print(f"{square_feet} sqft = {square_meters:.2f} sqmt")