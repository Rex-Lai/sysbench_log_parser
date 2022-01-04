#! /usr/bin/python

import sys
import argparse

def parseFile(filename, shards, warmup_seconds, is_title):
    f = open(filename, 'r')
    if is_title:
        print('shards,seconds,threads,tps,qps,latency,errors')
    for line in f:
        lst = []
        if line[0] == '[':
            time = line.split(']')
            seconds = time[0].replace('[', '').replace(' ', '').replace('s','')
            if int(seconds) <= int(warmup_seconds):
                continue
            tmpLst = time[1].split(' ')
            lst.append(str(shards))
            lst.append(seconds)
            lst.append(tmpLst[2])
            lst.append(tmpLst[4])
            lst.append(tmpLst[6])
            lst.append(tmpLst[11])
            lst.append(tmpLst[13])
            print(','.join(lst))

def main(args):
        parseFile(args.filename, args.shards, args.warmup_seconds, args.title)

if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('--filename', help='input log file', required=True)
        parser.add_argument('--title', help='output title. (default=False)', default=False)
        parser.add_argument('--shards', help='shard number. (default=1)', default=1)
        parser.add_argument('--warmup_seconds', help='warmup seconds. (default:0)', default=0)
        args = parser.parse_args()
        if main(args):
            sys.exit()
    except Exception as err:
        print('EXCEPTION!!! ' + str(err))
    sys.exit(13)
