
from file_handeler import FileHandler

class Main:
    def __init__(self) -> None:
        print("Program Starting....")
        # 1. Initialize
        filename = 'invantory.csv'
        invantory_file = FileHandler(filename)
        rows = invantory_file.Read()

        # 2. Operate
        print(f"#### {filename} ####")
        print()
        for row in rows:
            print(row)

        print()
        print(f"#### {filename} ####")
        # 3. CleanUp
        print("Program Ending....")
        return None

if __name__ == "__main__":
    app = Main()