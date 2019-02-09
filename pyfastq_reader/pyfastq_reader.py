#!/usr/bin/env python3
# MIT License see LICENSE
# -- Andy Hauser <Andreas.Hauser@LMU.de>

from __future__ import print_function
import sys
import fastq_reader from pyfastq_reader

def main():
  for filename in sys.argv[1:]:
    count = 0
    for head, seq, qual in fastq_reader(filename):
      count += 1
    print(filename, count, sep="\t")

if __name__ == '__main__':
  main()

