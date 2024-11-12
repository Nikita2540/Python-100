print("Hello, there")
name = input("What's your name \"miss\"? ")
name = name.strip().title()

first, last = name.split(" ")
print(f"Hello {name}")
print("Hope you are well", first, sep="! ", end="")
print(", you are learning Python which is case sensitive, Ms "+ last)
