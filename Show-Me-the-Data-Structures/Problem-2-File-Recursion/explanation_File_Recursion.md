The algorithm `find_files` takes `path` to directory as argument and `suffix`.
Iterates through directories and files beginning with root directory.
For every file, compare extension with `suffix`.
For every directory, call recursively `find_files`.

Time complexity is O(n), `n` being total number of files from root path argument.

Space complexity is O(n) in case that all files extension match `suffix`, `n` being number of string from `files` array.

