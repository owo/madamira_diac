# madamira_diac

## About

madamira_diac is a commandline utility to for diacritizing Arabic text using
MADAMIRA setup in server mode.

## Installation

First you need to acquire a copy of MADAMIRA from
[here](http://innovation.columbia.edu/technologies/cu14012_arabic-language-disambiguation-for-natural-language-processing-applications).

Start MADAMIRA in server mode by running the following in a console window:

```
cd /path/to/MADAMIRA

java -Xmx2500m -Xms2500m -XX:NewRatio=3 \
     -jar MADAMIRA-release-xxxxxxxx-x.x.jar -s
```

In a new terminal window, clone a copy of this repo.

```
git clone https://github.com/owo/madamira_diac.git madamira_diac
```

Then install madamira_diac and all of its dependencies:

```
cd madamira_diac

pip install .
```

## Usage

Below is the usage manual which can be seen by running `madamira_diac -h`.

```
Usage:
    madamira_diac [-u URL | --url=URL]
                  [-a | --all]
                  [-s | --separate-punct]
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
  -s --separate-punct         Seperate punctuation.
  -u URL --url=URL            The MADAMIRA server URL. Defaults to
                              http://localhost:8223.
  -v --version                Show version.
```

## Examples

### Interactive terminal session

To test out madamira_diac in an interactive terminal session, just type:

```
madamira_diac
```

MADAMIRA will not return a diacritization for words that are attached to
punctuation. One way around this is to ask it to separate punctuation before
diacritization by running:

```
madamira_diac -s
```

### Diacritizing an entire file

To diacritize an entire file using a single request to MADAMIRA, use the `-a`
flag as follows:

```
madamira_diac -a -i input.txt -o output.txt
```

By default, madamira_diac sends one request to MADAMIRA per line.
This is useful to get real-time feedback in an interactive session but will be
slow when processing large files. Note that using `-a` in an interactive session
will not return any results until the session is closed using `Ctrl-d`.

## License

madamira_diac is licensed under the MIT License. See [here](LICENSE)
for more information.
