# HeadLess
![изображение](https://github.com/VlCl0US/HeadLess/assets/146950743/1cfe07f0-e170-4d3f-aa1e-adbfa01886c3)

Security headers testing tool ~ Version 1.0

## Description:
A tool for working with server headers, running in python via the urllib module.

## Installation:
```bash
git clone https://github.com/VlCl0US/HeadLess  && cd HeadLess
python3 headless.py -u github.com -c
```
## Usage:
```bash
usage: headless.py [-h] [-u URL] [-i] [-c] [-f] [-a] [-d]

options:
  -h, --help                show this help message and exit
  -u URL, --url URL         Input host's url
  -i, --invisible           Invisible mode. No logo. For the best POC <3
  -c, --check               Simple security headers check
  -f, --full                Security headers check with full value
  -a, --all_headers         Show all headers
  -d, --disable_redirects   Disable redirects
```
## Soon:
* Server information disclousure headers detection feature
* Cross Origin Resource Sharing (CORS) misconfiguration detection feature
* Input multiple hosts from file feature
