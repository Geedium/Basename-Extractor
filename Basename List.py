import os
import sys
import uuid

from pathlib import Path

argc = len(sys.argv)

if(argc > 1):
    rand = uuid.uuid4().urn
    filename = rand[9:] + ".txt"
    fs = open(filename, "w+")
    data = list()

    for i in range(1, argc, 1):
        arg = sys.argv[i]
        basename = os.path.basename(arg)

        if os.path.isdir(arg):
            for root, dirs, files in os.walk(arg):
                for arg in files:
                    basename = os.path.basename(arg)
                    data.append(basename)

        if os.path.isfile(arg):
            data.append(basename)

    data.sort()

    for i in range(0, len(data), 1):
        basename = os.path.basename(data[i])
        stem = Path(basename).stem
        fs.write(stem)
        if i < len(data) - 1:
            fs.write('\n')

    fs.close()