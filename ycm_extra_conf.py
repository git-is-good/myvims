def FlagsForFile(filename, **kwargs):
    flags = [
            "-Wall",
            "--std=c++17",
            "-I/usr/local/include",
            "-I/usr/local/Cellar/llvm/5.0.0/include/c++/v1"
    ]
    return { 'flags': flags };
