import os
import sys

sys.path.append(os.path.abspath('..'))
import moduleA


if __name__ == '__main__':
    module = moduleA.ModuleClass().hello_world()
