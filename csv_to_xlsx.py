#!/usr/bin/env python

"""csv_to_xlsx

Usage:
    csv_to_xlsx --format=xlsx <file>...

"""

import tablib
import docopt
import os
from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__, version='csv_to_xlsx 0.1')

    
    for arg in [arg for arg in arguments['<file>'] if os.path.isfile(arg)]:
        data = tablib.Dataset()
        with open(arg,'r') as f_:
            data.csv = f_.read(-1)
            if arguments['--format'] in ('xls', 'xlsx'):
                f_ext = arguments['--format']
            else:
                f_ext = 'xlsx'

            output = eval('data' + '.' + f_ext)
        
        
            with open(arg[:-3]+f_ext,'wb') as f_out:
                f_out.write(output)
