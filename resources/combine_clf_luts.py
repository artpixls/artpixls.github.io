import argparse
import os, sys
import gzip
import xml.etree.ElementTree as ET


def getopts():
    p = argparse.ArgumentParser()
    p.add_argument('-o', '--output')
    p.add_argument('-c', '--compressed', action='store_true')
    p.add_argument('luts', nargs='+')
    return p.parse_args()


def main():
    opts = getopts()
    luts = list(opts.luts)
    root = ET.Element('ProcessList', compCLFversion='3', id='processlist')
    for l in opts.luts:
        t = ET.parse(l)
        r = t.getroot()
        assert r.tag == 'ProcessList'
        for c in r:
            root.append(c)
    def write(out):
        tree = ET.ElementTree(root)
        out.write(b'<?xml version="1.0" encoding="UTF-8"?>\n')
        tree.write(out, encoding='utf-8')
        out.write(b'\n')
    if opts.output:
        fopen = gzip.open if opts.compressed else open
        with fopen(opts.output, 'wb') as out:
            write(out)
    elif opts.compressed:
        with gzip.open(sys.stdout.buffer, 'wb') as out:
            write(out)
    else:
        write(sys.stdout.buffer)


if __name__ == '__main__':
    main()
