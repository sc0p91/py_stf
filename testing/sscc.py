#!/usr/bin/python3.6

import sys, getopt

def main(argv):
    input = ''
    searchterm = []

    if len(sys.argv) == 1:
        about()
    else:
        opts, args = getopt.getopt(argv,"ahs:",["search="])

    for opt, arg in opts:
        if opt in ('-h','--help'):
            about()
        elif opt in ('-s','--search'):
            if not arg:
                about()
            else:
                input = sys.argv[2:]
                for i in input:
                    searchterm.append(str(i))
                print 'searching for: ', searchterm
        else:
            about()


def about():
    print './sscc.py -s <searchterm(s)> or -a for everything'
    sys.exit()

if __name__ == "__main__":
    main(sys.argv[1:])
