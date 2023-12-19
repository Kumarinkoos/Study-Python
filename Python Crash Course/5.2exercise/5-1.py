cars = ["audi", "bmw", "subaru", "toyota"]

for car in cars:
    if car == "subaru":
        print(f"Is car == {car}? I predict True.")
        print(car == "subaru")
    else:
        print(f"\nIs car == {car}? I predict False.")
        print(car == "audi")
    