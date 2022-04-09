import argparse

argparser = argparse.ArgumentParser()
argparser.add_argument("input_file", help="file path to input-file", type=str)
argparser.add_argument("-p", "-pc", "--print", "--print-to-console", help="print way to console", action="store_true", default=False)
argparser.add_argument("-pf", "--print-to-file", help="print way to given file", default=None)
args = argparser.parse_args()
print(args)

if args.print_to_file != None