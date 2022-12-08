#!/usr/bin/python3
class Directory(object):
    def __init__(self, name):
        self.parent = None
        self.name = name
        self.files = dict()
        self.children = dict()

    def add_file(self, size, name):
        self.files[name] = int(size)

    def add_child(self, child_directory):
        self.children[child_directory.name] = child_directory
        child_directory.parent = self

    def get_size(self):
        size = sum(self.files.values())
        size += sum(child.get_size() for child in self.children.values())
        return size


def get_directory_sizes(directory, directory_sizes):
    if directory:
        directory_sizes.append(directory.get_size())
        for child in directory.children.values():
            get_directory_sizes(child, directory_sizes)


TOTAL_FILE_SYSTEM = 70000000
FREE_SPACE_GOAL = 30000000
current_directory = None
directory_sizes = []

with open('../resources/PuzzleInputs/Day7Input', 'r') as commandLineOutput:
    # Populate File System
    for line in commandLineOutput:
        line = line.strip()
        if line.startswith('$ cd'):
            if line[5:] == '/':
                current_directory = Directory('/')
            elif line[5:] == '..':
                current_directory = current_directory.parent
            else:
                current_directory = current_directory.children[line[5:]]
            print(f'Moving to {line[5:]}')
        elif line.startswith('$ ls'):
            print(f'I think I don\'t actually need to do anything here')
        elif line.startswith('dir'):
            current_directory.add_child(Directory(line[4:]))
            print(f'Adding Child {line[4:]}')
        else:
            current_directory.add_file(*line.split())
            print(f'Adding File {line.split()}')

    # Reset at Top
    while current_directory.parent is not None:
        current_directory = current_directory.parent

    # Part 1
    get_directory_sizes(current_directory, directory_sizes)

    space_used = current_directory.get_size()

    print(f'Used Space: {space_used}')

    print(f'Part 1: {sum(size for size in directory_sizes if size <= 100000)}')

    directory_sizes.sort()
    leftover_space = TOTAL_FILE_SYSTEM - space_used
    space_to_makeup = FREE_SPACE_GOAL - leftover_space
    print(f'Part 2: {next(filter(lambda x: x > space_to_makeup, directory_sizes))}')
