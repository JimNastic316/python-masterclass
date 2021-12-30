import os
import fnmatch


def find_music(start, extension):
    for path, directories, files in os.walk(start):
        for file in fnmatch.filter(files, '*.{}'.format(extension)):
            absolute_path = os.path.abspath(path)       # create absolute path
            yield os.path.join(absolute_path, file)     # use it in yielded values


my_music_files = find_music('music', 'emp3')

for f in my_music_files:
    print(f)

# Create a generator that will return the complete filename of all emp3 files
# The genereator should start at a specified directory, the START, which will be provided as an argument to the generator function
# The filenames should include the full path from the specified START directory. So it'll return a relative path.
