import sys
import colorama
import re
import random
from termcolor import colored, cprint

__version__ = "1.0.1"

c = '''\nVersion: 1.0
    
Available tags:

<r> - shows the text of red color, <g> - shows the text of green color, <b> - shows the text of blue color,
<y> - shows the text of yellow color, <c> - shows the text of cyan color.\n'''

def parse(t, f, t1, t2):
    r = re.compile(t1+"(.*?)"+t2, re.MULTILINE|re.IGNORECASE)
    rfa = r.findall(t)
    r2 =  re.sub(r, "%s", t)
    #r3 = random_id()
    f2 = tuple([f.format(x) for x in rfa])
    res = r2 % f2
    return res

def print_color(g):
    a = parse(g, colorama.Fore.RED+"{}"+'\033[39m', t1="<r>", t2="</r>")
    b = parse(a, colorama.Fore.GREEN+"{}"+'\033[39m', t1="<g>", t2="</g>")
    c = parse(b, colorama.Fore.BLUE+"{}"+'\033[39m', t1="<b>", t2="</b>")
    d = parse(c, colorama.Fore.YELLOW+"{}"+'\033[39m', t1="<y>", t2="</y>")
    f = parse(d, colorama.Fore.CYAN+"{}"+'\033[39m', t1="<c>", t2="</c>")
    return f

def main():
    print(c)
    try:
        while True:
            #g = input(colorama.Fore.GREEN+"Input: "+"\033[39m")
            text = colored('Input: ', 'green', attrs=['bold'])
            g = input(text)
            h = print_color(g)
            print("\n"+colored('Output:\n', 'red', attrs=['bold'])+"\n"+h+"\n")

    except (KeyboardInterrupt, EOFError):
           
        cprint("\n\nOperation cancelled by user\n", "red")
