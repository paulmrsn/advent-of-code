import aocd 

data = aocd.get_data(day=7, year=2022)

class Entry:
    def __init__(self, name: str, path: str):
        self.name = name 
        self.path = path
    def __repr__(self):
        return f"{self.path} -> {self.name}"

class File(Entry):
    def __init__(self, name: str, path: str, size: int):
        super().__init__(name, path)
        self.size = size 
    def __repr__(self):
        return f"{self.path} -> {self.name}({self.size})"

class Directory(Entry):
    def __init__(self, name: str, path: str, children: dict[str, Entry]):
        super().__init__(name, path)
        self.children = children 
        self.__total_size = -1
    def __iadd__(self, entry: Entry):
        self.children[entry.name] = entry
        return self
    def get_size(self):
        if self.__total_size > 0:
            return self.__total_size
        size = 0
        for entry in self.children.values():
            if type(entry) == File:
                size += entry.size
            elif type(entry) == Directory:
                size += entry.get_size()
        self.__total_size = size
        return size
    def __repr__(self):
        return f"{self.path} -> {self.children}"

def get_dirs(data: str):
    dirs = {}
    root: Directory = Directory("root", "/", {})
    dirs["root"] = root;
    path = [root]

    for line in data.splitlines()[1:]:
        pwd = "/".join([entry.name for entry in path])
        cwd = path[-1]
        match line.split():
            case ["$", "ls"]:
                continue
            case ["$", "cd", "/"]:
                path = [root]
            case ["$", "cd", ".."]:
                if pwd is not root:
                    path.pop()
            case ["$", "cd", dir_name]:
                path.append(dirs.get(pwd + "/" + dir_name, Directory(dir_name, pwd, {})))
            case ["dir", dir_name]:
                dir = Directory(dir_name, pwd, {})
                dirs[pwd + "/" + dir_name] = dir
                cwd += dir 
            case [file_size, file_name] if file_size.isdigit():
                file = File(file_name, pwd, int(file_size))
                cwd += file
            case _:
                print("Unknown command:", line)
    return dirs

dirs = get_dirs(data)
print("Part 1:", sum(list(filter(lambda size : size < 100000, [dir.get_size() for (_, dir) in dirs.items()]))))

total_size = 70000000
required_for_upgrade = 30000000
used = dirs["root"].get_size()

missing = required_for_upgrade - (total_size - used)
print("Part 2:", min(list(filter(lambda size : size >= missing, [dir.get_size() for (_, dir) in dirs.items()]))))