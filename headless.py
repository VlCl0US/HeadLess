import urllib.request
import argparse
from urllib import request
from colorama import Fore

# read user's arguments
parser = argparse.ArgumentParser()
parser.add_argument("-u" , "--url" , type = str , help = "Input host's url")
parser.add_argument("-i" , "--invisible" , action = 'store_true' , help = "Invisible mode. No logo. For the best POC <3")
parser.add_argument("-c" , "--check" , action = 'store_true' , help = "Simple security headers check")
parser.add_argument("-f" , "--full" , action = 'store_true' , help = "Security headers check with full value")
parser.add_argument("-a" , "--all_headers" , action = 'store_true' , help = "Show all headers")
parser.add_argument("-d" , "--disable_redirects" , action = 'store_true' , help = "Disable redirects")

args = parser.parse_args()

# invisible mode
if args.invisible == False:
    print('''
    )                                   
 ( /(              (    (               
 )\())   (     )   )\ ) )\   (          
((_)\   ))\ ( /(  (()/(((_) ))\ (   (   
 _((_) /((_))(_))  ((_))_  /((_))\  )\  
| || |(_)) ((_)_   _| || |(_)) ((_)((_) 
| __ |/ -_)/ _` |/ _` || |/ -_)(_-<(_-< 
|_||_|\___|\__,_|\__,_||_|\___|/__//__/ v1.0                                        
Security headers testing tool
          ''')

url = args.url
if not url.startswith('http://') and not url.startswith('https://'):
    url = 'http://' + url
print('Connecting to ' + Fore.BLUE + url + Fore.RESET)

# get response from target
class NoRedirect(request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None

if args.disable_redirects == True:
    print('Redirection disabled')
    opener = request.build_opener(NoRedirect)
    request.install_opener(opener)

    try:
        request = request.urlopen(url)
    except urllib.error.HTTPError as e:
        request = e
    print('Response code: ' + str(request.getcode()))

else:
    try:
        request = request.urlopen(url)
    except urllib.error.HTTPError as e:
        request = e
    if request.geturl() != url:
        print('Redirected to ' + Fore.BLUE + request.geturl() + Fore.RESET)
    print('Response code: ' + str(request.getcode()))

# security headers list
security_headers = ["X-Frame-Options" , "Strict-Transport-Security" , 
                    "Permissions-Policy" ,"Content-Security-Policy" , 
                    "X-Content-Type-Options" , "Referrer-Policy"]

class main:    
    # output security headers and values
    def list_headers():
        print('''          
Status of security headers -''')
        for header in security_headers:
            if request.headers[header] == None:
                print(Fore.RED + header + Fore.RESET + ': ' + 'EMPTY')
            else:
                print(Fore.GREEN + header + Fore.RESET + ': ' + 'ok')
                
    # output all headers            
    def all_headers():
        print('''
All headers -''')
        print(request.headers)
    
    # output full values of security headers
    def security_headers_full():
        print('''
Value of security headers -''')
        for header in security_headers:
            if request.headers[header] == None:
                print(Fore.RED + header + Fore.RESET + ': ' + 'EMPTY')
            else:
                print(Fore.GREEN + header + Fore.RESET + ': ' + request.headers[header])
    

# show all headers
if args.all_headers == True:
    main.all_headers()

# show security headers
if args.check == True and args.full != True:       
    main.list_headers()                

# show full values of security headers
if args.full == True:
    main.security_headers_full()
