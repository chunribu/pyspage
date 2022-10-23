import argparse
import os
import pyspage

def parse_args():
    parser = argparse.ArgumentParser(description='[Pyspage]\nQuickly build open source web pages for academic purposes in a pythonic and elegant way.')
    parser.add_argument('file', type=str,
                        help='path to input file')
    parser.add_argument('-o', '--output', type=str, 
                        help='path to output file (default: the same as input, but .py -> .html)')
    parser.add_argument('-l', '--localize', action=argparse.BooleanOptionalAction,
                        help='save all used network resources to local')
    parser.add_argument('-s', '--server', action=argparse.BooleanOptionalAction,
                        help='start a server on localhost:8000')
    parser.add_argument('-b', '--browser', action=argparse.BooleanOptionalAction,
                        help='open your default browser automatically')
    args = parser.parse_args()
    return args

def main(args):
    fpath = args.file
    html = pyspage.main(fpath)
    if args.output:
        dirname, filename = os.path.split(fpath)
        outpath = os.path.join(dirname, filename.replace('.py', '.html'))
    else:
        outpath = args.output
    with open(outpath, 'w') as f:
        f.write(html)

def run():
    args = parse_args
    main(args)
