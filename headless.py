import argparse
from urllib import request, error
from colorama import Fore

# read user's arguments
parser = argparse.ArgumentParser()
parser.add_argument("-u" , "--url" , type = str , help = "Input host's url")
parser.add_argument("-i" , "--invisible" , action = 'store_true' , help = "Invisible mode. No logo. For the best POC <3")
parser.add_argument("-c" , "--check" , action = 'store_true' , help = "Simple security headers check")
parser.add_argument("-f" , "--full" , action = 'store_true' , help = "Security headers check with full value")
parser.add_argument("-a" , "--all_headers" , action = 'store_true' , help = "Show all headers")
parser.add_argument("-d" , "--disable_redirects" , action = 'store_true' , help = "Disable redirects")
parser.add_argument("-x" , "--cors_check" , action = 'store_true' , help = "Cross origin resource sharing check with full value")

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

# security headers list
security_headers = ["X-Frame-Options" , "Strict-Transport-Security" , 
                    "Permissions-Policy" ,"Content-Security-Policy" , 
                    "X-Content-Type-Options" , "Referrer-Policy"]

# CORS headers list
cors_headers = ["Access-Control-Allow-Origin" , "Access-Control-Allow-Credentials" , 
                "Access-Control-Allow-Headers" , "Access-Control-Allow-Methods" , 
                "Access-Control-Expose-Headers" , "Access-Control-Max-Age" , 
                "Access-Control-Request-Headers" , "Access-Control-Request-Method" , 
                "Origin"]

class main:          
    # fix input URL
    def to_http():
        if args.url == None:
            print(Fore.RED + 'no URL found.' + Fore.RESET)
            exit()
        if not args.url.startswith('http://') and not args.url.startswith('https://'):
            args.url = 'http://' + args.url
        print('Connecting to ' + Fore.BLUE + args.url + Fore.RESET)
    
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
    
    # output CORS headers
    def cors_headers():
        print('''
Value of CORS headers -''')
        for cors_header in cors_headers:
            if request.headers[cors_header] == None:
                print(Fore.RED + cors_header + Fore.RESET + ': ' + 'EMPTY')
            else:
                print(Fore.GREEN + cors_header + Fore.RESET + ': ' + request.headers[cors_header])

# disable redirects
class NoRedirect(request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None

# get target
main.to_http()

# get response from target
if args.disable_redirects == True:
    print('Redirection disabled')
    opener = request.build_opener(NoRedirect)
    request.install_opener(opener)

    try:
        request = request.urlopen(args.url)
    except error.HTTPError as e:
        request = e
    except error.URLError as e:
        print(Fore.RED + 'connection error.' + Fore.RESET)
        exit()
    print('Response code: ' + str(request.getcode()))

else:
    try:
        request = request.urlopen(args.url)
    except error.HTTPError as e:
        request = e
    except error.URLError as e:
        print(Fore.RED + 'connection error.' + Fore.RESET)
        exit()
    print('Redirected to ' + Fore.BLUE + request.geturl() + Fore.RESET)
    print('Response code: ' + str(request.getcode()))

# show all headers
if args.all_headers == True:
    main.all_headers()

# show security headers
if args.check == True and args.full != True:       
    main.list_headers()                

# show full values of security headers
if args.full == True:
    main.security_headers_full()
    
if args.cors_check == True:
    main.cors_headers()
