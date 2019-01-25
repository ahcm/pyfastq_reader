#!/usr/bin/env python3
# MIT License see LICENSE
# -- Andy Hauser <Andreas.Hauser@LMU.de>

from __future__ import print_function
import sys

def fastq_reader(filename):
  return fastq_reader_fh(open(filename, 'r'))

def fastq_reader_fh(infile):
  name = infile.readline().rstrip()
  while True:
    seq = ""
    for s in infile:
      if s[0] == '+':
        commentp = s.rstrip()
        break
      else:
        seq += s.rstrip()
    qual = ""
    for q in infile:
      if len(qual) > 0 and  q[0] == '@':
        yield name, seq, qual
        name = q.rstrip()
        break
      else:
        qual += q.rstrip()
    else:
      yield name, seq, qual
      return

def main():
  for filename in sys.argv[1:]:
    count = 0
    for head, seq, qual in fastq_reader(filename):
      count += 1
    print(count)

if __name__ == '__main__':
  main()

