# NumberToText

Program that finds numerals (e.g. 200 406) and replaces them by their spelled out version (duzentos mil quatrocentos e
seis) in Portuguese.

This rep have two different aproaches:

- 1º Aproach - Regular Expressions and some calculations to convert:
  - Usage: `./NumberToText1.py [OPTIONS] [FILENAME]`\
      or: `./NumberToText1.py [OPTIONS]` //STDIN, CTRL+D to stop input
    
  - Default behaviour: Convert numbers to portuguese text
  - Options:
      - -r &ensp;&ensp;&ensp; Convert portuguese text to numbers
      - -h &ensp;&ensp;&ensp;	Help

  - Example: `./NumberToText2.py text.txt`
- 2º Aproach - Only Regular Expressions:
  - Usage: `./NumberToText2.py [OPTIONS] [FILENAME]`\
      or: `./NumberToText2.py [OPTIONS]` //STDIN, CTRL+D to stop input
    
  - Default behaviour: Convert numbers to portuguese text
  - Options:
      - -r &ensp;&ensp;&ensp; Convert portuguese text to numbers
      - -h &ensp;&ensp;&ensp;	Help

  - Example: `./NumberToText2.py text.txt`

## Dependencies

- [Python 3](https://www.python.org/)