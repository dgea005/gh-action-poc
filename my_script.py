##

def write_file_using_inputs():
    with open("templates/my_file.txt", "w") as f:
        f.write("test")


if __name__ == "__main__":
    write_file_using_inputs()
