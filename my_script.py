##
import pathlib

def main():
    current_dir = pathlib.Path(__file__).parent
    pathlib.Path(current_dir/"templates").mkdir(parents=True, exist_ok=True)
    pathlib.Path(current_dir/"input").mkdir(parents=True, exist_ok=True)
    # check for files
    new_files = [f for f in current_dir.glob('input/*') if f.name != "README.md"]
    if len(new_files) > 0:
        print(f"No {len(new_files)} to process")
        for input_f in new_files:
            data = input_f.read_text()
            with open(current_dir/f"templates/{input_f.name}", "w") as f:
                f.write(data)
            # delete the input
            print(f"Deleting the input file: {input_f.name}")
            input_f.unlink(missing_ok=True)
        print("Wrote output files")
    else:
        print(f"No input files to process")

if __name__ == "__main__":
    main()
