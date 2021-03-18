import os
import sys

if __name__ == '__main__':
    base = os.path.curdir
    threshold_size = float(sys.argv[1]) * 1024 * 1024 * 1024
    print(threshold_size)
    # threshold_size = 2.5 * 1024 * 1024 * 1024
    # os.chdir('F:/1/s262')
    for root, dirs, files in os.walk(base):
        for f in files:
            s = os.path.join(root, f)
            file_size = os.path.getsize(s)
            if file_size >= threshold_size:
                print('%s\t\t%sG' % (s, round(file_size / (1024 * 1024 * 1024), 2)))
