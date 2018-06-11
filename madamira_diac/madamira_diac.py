#!/usr/bin/env python
# -*- coding: utf-8 -*-

# MIT License
#
# Copyright (c) 2018 Ossama W. Obeid
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""madamira_diac: A commandline utility for diacritizing Arabic text with
                  MADAMIRA in server mode.

Usage:
    madamira_diac [-u URL | --url=URL]
                  [-a | --all] [-s | --separate-punct] [-p | --preprocess]
                  [-i INPUT | --input=INPUT]
                  [-o OUTPUT | --output=OUTPUT]
    madamira_diac (-v | --version)
    madamira_diac (-h | --help)

Options:
  -a --all                    Send all lines to MADAMIRA at once.
  -h --help                   Show this screen.
  -i INPUT --input=INPUT      Input file. If not specified, input will be read
                              from standard input.
  -o OUTPUT --output=OUTPUT   Output file. If not specified, output will be
                              written to standard output.
  -p --preprocess             Preprocess text.
  -s --separate-punct         Seperate punctuation.
  -u URL --url=URL            The MADAMIRA server URL. Defaults to
                              http://localhost:8223.
  -v --version                Show version.
"""

from __future__ import absolute_import
import sys

from docopt import docopt
from requests.exceptions import RequestException

import madamira_diac
from madamira_diac.diac import diac_file, diac_stream


__version__ = madamira_diac.__version__

_DEFAULT_URL = 'http://localhost:8223'


def main():
    """Program entry point.
    """

    fin = sys.stdin
    fout = sys.stdout
    using_stdin = True
    using_stdout = True

    # Parse commandline arguments
    arguments = docopt(__doc__, version=__version__)

    input_path = arguments.get('--input', None)
    output_path = arguments.get('--output', None)
    server_url = arguments.get('--url', None)
    preprocess = arguments.get('--preprocess', False)
    separate_punct = arguments.get('--separate-punct', False)
    send_all = arguments.get('--all', False)

    if server_url is None:
        server_url = _DEFAULT_URL

    # Setup input and output files
    if input_path is not None:
        try:
            fin = open(input_path, 'r')
            using_stdin = False
        except Exception:
            sys.stderr.write('Error: Couldn\'t open input file {}.\n'.format(
                repr(input_path)))
            sys.exit(1)
    if output_path is not None:
        try:
            fout = open(output_path, 'w')
            using_stdout = False
        except Exception:
            sys.stderr.write('Error: Couldn\'t open output file {}.\n'.format(
                repr(output_path)))
            if not using_stdin:
                fin.close()
            sys.exit(1)

    # Diacritize input
    try:
        if send_all:
            diac_file(fin, fout, server_url, preprocess, separate_punct)
        else:
            diac_stream(fin, fout, server_url, preprocess, separate_punct)
        sys.exit(0)
    except RequestException as e:
        sys.stderr.write('An error occurred while connecting to MADAMIRA:\n')
        sys.stderr.write(str(e))
        sys.stderr.write('\n')
        sys.stderr.flush()
        sys.exit(1)
    except KeyboardInterrupt as e:
        sys.stderr.write('Exiting...\n')
        sys.exit(1)
    except Exception as e:
        sys.stderr.write('An error occurred while diacritizing text:\n')
        sys.stderr.write(str(e))
        sys.stderr.write('\n')
        sys.stderr.flush()
        sys.exit(1)
    finally:
        fout.flush()

        if not using_stdin:
            fin.close()
        if not using_stdout:
            fout.close()


if __name__ == '__main__':
    main()
