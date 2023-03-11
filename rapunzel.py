import requests
from bs4 import BeautifulSoup


def get_socks4_proxies():
    url = 'https://www.socks-proxy.net/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table')

    rows = table.find_all('tr')

    proxies = []
    for row in rows[1:]:
        cols = row.find_all('td')
        if len(cols) > 0:
            ip = cols[0].text.strip()
            port = cols[1].text.strip()
            proxy = f'{ip}:{port}'
            proxies.append(proxy)

    return proxies


def get_http_proxies():
    url = 'https://www.sslproxies.org/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table')

    rows = table.find_all('tr')

    proxies = []
    for row in rows[1:]:
        cols = row.find_all('td')
        if len(cols) > 0:
            ip = cols[0].text.strip()
            port = cols[1].text.strip()
            proxy = f'{ip}:{port}'
            proxies.append(proxy)

    return proxies


def get_ssl_proxies():
    url = 'https://sslproxies.org/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table')

    rows = table.find_all('tr')

    proxies = []
    for row in rows[1:]:
        cols = row.find_all('td')
        if len(cols) > 0:
            ip = cols[0].text.strip()
            port = cols[1].text.strip()
            proxy = f'{ip}:{port}'
            proxies.append(proxy)

    return proxies

def get_us_proxies():
    url = 'https://www.us-proxy.org/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table')

    rows = table.find_all('tr')

    proxies = []
    for row in rows[1:]:
        cols = row.find_all('td')
        if len(cols) > 0:
            ip = cols[0].text.strip()
            port = cols[1].text.strip()
            proxy = f'{ip}:{port}'
            proxies.append(proxy)

    return proxies



def get_all_proxies():
    socks4_proxies = get_socks4_proxies()
    http_proxies = get_http_proxies()
    ssl_proxies = get_ssl_proxies()
    us_proxies = get_us_proxies()



    all_proxies = socks4_proxies + http_proxies + ssl_proxies + us_proxies

    return all_proxies


def main():
    print("                      :::!~!!!!!:.")
    print("                  .xUHWH!! !!?M88WHX:.")
    print("                .X*#M@$!!  !X!M$$$$$$WWx:.")
    print("               :!!!!!!?H! :!$!$$$$$$$$$$8X:")
    print("              !!~  ~:~!! :~!$!#$$$$$$$$$$8X:")
    print("             :!~::!H!<   ~.U$X!?R$$$$$$$$MM!")
    print("             ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!")
    print("               !:~~~ .:!M$TS$$$$WX??#MRRMMM!")
    print("               ~?WuxiW*`   `$$#$$$$8!!!!??!!!")
    print("             :X- M$$$$       `!T#$T~!8$WUXU~")
    print("            :%`  ~#$$$m:        ~!~ ?$$$$$$")
    print("          :!`.-   ~T$$$$8xx.  .xWW- ~!!##*!")
    print(".....   -~~:<` !    ~?T#$$@@W@*?$$      /`")
    print("#!~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`")
    print(":::~:!!`:X~ .: ?H.!u !$$$B$$$!W:U!T$$M~")
    print(".~~   :X@!.-~   ?@WTWo(!*$$$W$TH$! `")
    print("Wi.~!X$?!-~    : ?$$$B$Wu(!**$RM!")
    print("$R@i.~~ !     :   ~$$$$$B$$en:``")
    print("?MXT@Wx.~    :     ~!##*$$$$M~")
    print("--~~Rapunzel's Proxy-Tool~~ ->	https://github.com/Rapunzel-ware")


    print('                  ')  
    print('Select Proxy Type:')
    print('1. Socks4 Proxies')
    print('2. HTTP Proxies')
    print('3. SSL Proxies')
    print('4. US Proxies')
    print('5. All Proxies')

    option = int(input())

    if option == 1:
        proxies = get_socks4_proxies()
    elif option == 2:
        proxies = get_http_proxies()
    elif option == 3:
        proxies = get_ssl_proxies()
    elif option == 4:
        proxies = get_us_proxies()
    elif option == 5:
        proxies = get_all_proxies()
    else:
        print('Invalid option')
        return

    print(f'Found {len(proxies)} proxies:')
    for proxy in proxies:
        print(proxy)


if __name__ == '__main__':
    main()
