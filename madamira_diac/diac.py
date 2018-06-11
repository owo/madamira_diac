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

"""This module contains functions that diacritize text by sending requests to
a MADAMIRA server.
"""

from __future__ import absolute_import, print_function

from collections import deque
from io import BytesIO

from lxml import etree
import requests

from madamira_diac.config import generate_config


def _diac_gen(xml):
    xml_stream = BytesIO(xml)
    sentence = deque()

    for event, element in etree.iterparse(
            xml_stream, events=('start', 'end'), load_dtd=False):
        if element.tag[-17:] == 'morph_feature_set' and event == 'end':
            curr_diac = element.get('diac', '')
        elif element.tag[-14:] == 'svm_prediction' and event == 'end':
            sentence.append(curr_diac)
        elif element.tag[-7:] == 'out_seg':
            if event == 'start':
                sentence = deque()
            else:
                yield ' '.join(sentence)


def diac_file(fin, fout, server_url, preprocess=False, separate_punct=False):
    """Reads in an entire file and gets its diacritized form using one request
    to MADAMIRA, writing the diacritized text to an output file.

    Arguments:
        fin {file} -- input file.
        fout {file} -- output file.
        server_url {string} -- MADAMIRA server url.

    Keyword Arguments:
        preprocess {bool} -- preprocess text (default: {False})
        separate_punct {bool} -- separate punctuation (default: {False})
    """

    config = generate_config(fin, preprocess, separate_punct)

    response = requests.post(server_url, data=config.encode('utf-8'))
    diac_sentences = _diac_gen(response.content)

    for sentence in diac_sentences:
        fout.write(sentence.encode('utf-8'))
        fout.write('\n')

    fout.flush()


def diac_stream(fin, fout, server_url, preprocess=False, separate_punct=False):
    """Reads a file line by line, sending a request per line to MADAMIRA, and
    writing the results to an output file.

    Arguments:
        fin {file} -- input file.
        fout {file} -- output file.
        server_url {string} -- MADAMIRA server url.

    Keyword Arguments:
        preprocess {bool} -- preprocess text (default: {False})
        separate_punct {bool} -- separate punctuation (default: {False})
    """

    line = fin.readline()

    while line:
        config = generate_config([line], preprocess, separate_punct)
        response = requests.post(server_url, data=config.encode('utf-8'))
        diac_sentences = _diac_gen(response.content)

        for sentence in diac_sentences:
            fout.write(sentence.encode('utf-8'))
            fout.write('\n')

        fout.flush()
        line = fin.readline()
