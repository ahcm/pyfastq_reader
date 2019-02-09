# pyfastq_reader
Pure Python FASTQ reader. Faster than you think.

# Installation

```bash
pip3 install --user pyfastq_reader
```

# Usage

See also https://github.com/ahcm/pyfastq_filter

Either provide a filename (fastq_reader):

```python
import pyfastq_filter
for filename in sys.argv[1:]:
  count = 0
  for head, seq, qual in pyfastq_reader.fastq_reader(filename):
    count += 1
  print(count)
```

Or a filehandle (fastq_reader_fh):

```python
import pyfastq_filter
for filename in sys.argv[1:]:
  count = 0
  for head, seq, qual in pyfastq_reader.fastq_reader_fh(open(filename, 'r')):
    count += 1
  print(count)
```
