import argparse
import Exercises2 as ex

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='exercise2')
    parser.add_argument('csv', help='csv file to read')
    parser.add_argument('-f', '--file', help='file name to output to')
    args = parser.parse_args()

    if args.file == None:
        print(ex.read_csv(args.csv))
    else:
        l = ex.read_csv(args.csv)
        ex.write_list2_to_file(args.file, l)