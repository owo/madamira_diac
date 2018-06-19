# -*- coding: utf-8 -*-

# MIT License
#
# Copyright (c) 2018 New York University Abu Dhabi
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

"""This module contains a function for generating MADAMIRA XML configs.
"""


from xml.sax.saxutils import escape

from jinja2 import Template
import six


_MADAMIRA_CONFIG_TEMPLATE = Template('''<?xml version="1.0" encoding="UTF-8"?>
<madamira_input xmlns="urn:edu.columbia.ccls.madamira.configuration:0.1">
    <madamira_configuration>
        <preprocessing sentence_ids="false"
            separate_punct="{{ separate_punct }}"
            input_encoding="UTF8"/>
        <overall_vars output_encoding="UTF8" dialect="MSA"
            output_analyses="TOP" morph_backoff="NONE"/>
        <requested_output>
            <req_variable name="PREPROCESSED" value="{{ preprocess }}" />
            <req_variable name="DIAC" value="true" />
        </requested_output>
    </madamira_configuration>

    <in_doc id="ExampleDocument">
    {% for sentence in sentences %}
        <in_seg id="SENT_{{ sentence[0] }}">
            {{ sentence[1] }}
        </in_seg>
    {% endfor %}
    </in_doc>
</madamira_input>
''')


def _force_unicode(s):
    if isinstance(s, six.text_type):
        return s
    else:
        return s.decode('utf-8')


def _sentence_gen(sentences):
    for sentence in enumerate(sentences):
        yield (sentence[0], escape(_force_unicode(sentence[1])))


def generate_config(sentences, separate_punct=False):
    """Generate a MADAMIRA XML config given a list of sentences.

    Arguments:
        sentences {list} -- the list of sentences to be diacritized.

    Keyword Arguments:
        separate_punct {bool} -- separate punctuation (default: {False}).

    Returns:
        string -- the generated config.
    """

    return _MADAMIRA_CONFIG_TEMPLATE.render(
        sentences=_sentence_gen(sentences),
        preprocess=str(separate_punct).lower(),
        separate_punct=str(separate_punct).lower())
