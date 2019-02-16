# not tested
class FileSystem:
    def __init__(self, path):
        assert(path.startswith('dir'))
        self.path = path
    
    def absolute_path_len(self, file_name):
        def helper(leftover_path):
            if leftover_path is None:
                raise ValueError("{} not found in {}".format(file_name, self.path))

            try:
                index = leftover_path.index('\n', 1)
                current = leftover_path[: index]
            except ValueError:
                index = len(leftover_path)
                current = leftover_path

            if current.find(file_name) != -1:
                return current.count('\t'), file_name
            
            level, build_path = helper(leftover_path[index :])

            if current.count('\t') == level - 1 and current.find('.') == -1:
                return level - 1, \
                    current.replace('\n', '').replace('\t', '') + '/' + build_path
            else:
                return level, build_path

        return helper(self.path[3])[1] 

    def absolute_path_len_iter(self, file_name):
        tokens = self.path.split('\n') \
            .map(lambda path:
                    (path.count('\t'), path.replace('\t', ''), path.find('.') == -1)
                )

        level_status = -1
        build_path = None
        for level, path, isDir in reversed(tokens):
            if level_status == -1:
                if path == file_name:
                    level_status = level
                    build_path = path
            elif level_status == level - 1 and isDir:
                level_status -= 1
                build_path = path + '/' + build_path
        
        return build_path


    def absolute_path_len_iter_golf(self, file_name):
        tokens = self.path.split('\n').map(lambda path: (path.count('\t'), path.replace('\t', ''), path.find('.') == -1))

        level_status, build_path = -1, None
        for level, path, isDir in reversed(tokens):
            if level_status == -1:
                if path == file_name:
                    level_status, build_path = level, path
            elif level_status == level - 1 and isDir:
                level_status, build_path = level_status - 1, path + '/' + build_path
        
        return build_path 