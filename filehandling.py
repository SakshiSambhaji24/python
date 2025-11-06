
with open("sample.txt", "w") as file:
    file.write("Hello, this is the first line.\n")
    file.write("This is the second line.\n")

print("Data written to file successfully.")


with open("sample.txt", "r") as file:
    content = file.read()
    print("\n--- File Content ---")
    print(content)


with open("sample.txt", "a") as file:
    file.write("This line is appended to the file.\n")

print("Data appended to file successfully.")


with open("sample.txt", "r") as file:
    print("\n--- Updated File Content ---")
    print(file.read())