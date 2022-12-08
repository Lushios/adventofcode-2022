TOTAL_SIZE = 70000000
NECESSARY_SPACE = 30000000


class File:
    def __init__(self, size, name):
        self.size = size
        self.name = name


class Folder:
    def __init__(self, name, parent_folder=None):
        self.name = name
        self.parent_folder = parent_folder
        self.folders = []
        self.files = []
        self.size = 0

    def get_folder(self, folder_name):
        return list(filter(lambda x: x.name == folder_name, self.folders))[0]

    def create_folder(self, folder_name):
        self.folders.append(Folder(folder_name, self))

    def add_folder(self, folder):
        self.folders.append(folder)

    def create_file(self, file_size, file_name):
        self.files.append(File(file_size, file_name))
        self.append_folder_size(file_size)

    def append_folder_size(self, size):
        self.size += int(size)
        if self.parent_folder:
            self.parent_folder.append_folder_size(size)

    def get_all_folders(self, collection):
        collection.append(self)
        for child in self.folders:
            child.get_all_folders(collection)


with open("input.txt") as file:
    # yes I have removed the first line from the input
    # I'm a liar I'm a cheat a leech a thief
    data = file.read().splitlines()

core = Folder('/')
current_folder = core
for line in data:
    if line.startswith('$'):
        if line[2:4] == 'cd':
            folder_path = line[5:]
            if folder_path == '..':
                current_folder = current_folder.parent_folder
            else:
                current_folder = current_folder.get_folder(folder_path)
        if line[2:4] == 'ls':
            continue
    else:
        first_part, second_part = line.split(' ')
        if first_part == 'dir':
            new_folder = Folder(second_part, current_folder)
            current_folder.add_folder(new_folder)
        else:
            current_folder.create_file(first_part, second_part)

folders_container = []
core.get_all_folders(folders_container)
amount_to_free = core.size - (TOTAL_SIZE - NECESSARY_SPACE)
print(amount_to_free)

a = list(filter(lambda x: x.size >= amount_to_free, folders_container))
answer = min([folder.size for folder in filter(lambda x: x.size >= amount_to_free, folders_container)])
print(answer)
