class FileHandler:
    # class variables
    filepath: str
    # constructor
    def __init__(self, filepath: str) ->None:
        # instance variables
        self.filepath = filepath
        return None
    def Read(self) -> list[str]:
        rows: list[str] = []
        try:
            filehandle = open(self.filepath, 'r', encoding="UTF-8")
            row = filehandle.readline()
            while row != '':
                row = row.rstrip('\n')
                rows.append(row)
                row = filehandle.readline()
        except Exception as err:
            print(f"Faield to read File '{self.filepath}'.")
            print(err)
            exit(-1) # from sys libary
        return rows


if __name__ == "__main__":
    app = FileHandler()