from distutils.core import setup

setup(
    name='pyfastq_reader',
    version='1.0',
    author='Andy Hauser',
    author_email='Andreas.Hauser@LMU.de',
    scripts=['pyfastq_reader.py'],
    url='https://github.com/ahcm/pyfastq_reader',
    license='LICENSE',
    description='FASTQ file reader',
    long_description='Pure python reader for the FASTQ format used in sequencing',
    install_requires=[ ],
)
