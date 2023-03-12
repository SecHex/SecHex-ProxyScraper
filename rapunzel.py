import requests
from bs4 import BeautifulSoup
from termcolor import colored
import json



def get_socks4_proxies():
    urls = [
        'https://www.socks-proxy.net/',
    ]
    proxies = []
    for url in urls:
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')

            if url == 'https://www.socks-proxy.net/':
                table = soup.find('table')
                rows = table.find_all('tr')
                for row in rows[1:]:
                    cols = row.find_all('td')
                    if len(cols) > 0:
                        ip = cols[0].text.strip()
                        port = cols[1].text.strip()
                        country = cols[2].text.strip()
                        uptime = cols[6].text.strip()

                        # Extract location from country column
                        location = ''
                        if country:
                            location = country.split(',')[0]

                        proxy = {
                            'ip': ip,
                            'port': port,
                            'uptime': uptime,
                            'location': location
                        }
                        proxies.append(proxy)

        except:
            print(f"Error scraping {url}")
    return proxies





def get_http_proxies():
    urls = [
        'https://www.sslproxies.org/',
    ]
    proxies = []
    for url in urls:
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')

            if url == 'https://www.sslproxies.org/':
                table = soup.find('table')
                rows = table.find_all('tr')
                for row in rows[1:]:
                    cols = row.find_all('td')
                    if len(cols) > 0:
                        ip = cols[0].text.strip()
                        port = cols[1].text.strip()
                        country = cols[2].text.strip()
                        uptime = cols[6].text.strip()

                        # Extract location from country column
                        location = ''
                        if country:
                            location = country.split(',')[0]

                        proxy = {
                            'ip': ip,
                            'port': port,
                            'uptime': uptime,
                            'location': location
                        }
                        proxies.append(proxy)

        except:
            print(f"Error scraping {url}")
    return proxies




def get_ssl_proxies():
    urls = [
        'https://sslproxies.org/',
    ]
    proxies = []
    for url in urls:
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')

            if url == 'https://sslproxies.org/':
                table = soup.find('table')
                rows = table.find_all('tr')
                for row in rows[1:]:
                    cols = row.find_all('td')
                    if len(cols) > 0:
                        ip = cols[0].text.strip()
                        port = cols[1].text.strip()
                        country = cols[2].text.strip()
                        uptime = cols[6].text.strip()

                        # Extract location from country column
                        location = ''
                        if country:
                            location = country.split(',')[0]

                        proxy = {
                            'ip': ip,
                            'port': port,
                            'uptime': uptime,
                            'location': location
                        }
                        proxies.append(proxy)

        except:
            print(f"Error scraping {url}")
    return proxies

def get_us_proxies():
    urls = [
        'https://www.us-proxy.org/',
    ]
    proxies = []
    for url in urls:
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')

            if url == 'https://sslproxies.org/':
                table = soup.find('table')
                rows = table.find_all('tr')
                for row in rows[1:]:
                    cols = row.find_all('td')
                    if len(cols) > 0:
                        ip = cols[0].text.strip()
                        port = cols[1].text.strip()
                        country = cols[2].text.strip()
                        uptime = cols[6].text.strip()

                        # Extract location from country column
                        location = ''
                        if country:
                            location = country.split(',')[0]

                        proxy = {
                            'ip': ip,
                            'port': port,
                            'uptime': uptime,
                            'location': location
                        }
                        proxies.append(proxy)

        except:
            print(f"Error scraping {url}")
    return proxies



def get_all_proxies():
    socks4_proxies = get_socks4_proxies()
    http_proxies = get_http_proxies()
    ssl_proxies = get_ssl_proxies()
    us_proxies = get_us_proxies()



    all_proxies = socks4_proxies + http_proxies + ssl_proxies + us_proxies

    return all_proxies

def save_to_file(proxies):
    filename = input('Enter filename to save to: ')
    if not filename.endswith('.txt'):
        filename += '.txt'
    with open(filename, 'w') as f:
        f.write('\n'.join(proxies))
    print(f'Successfully saved {len(proxies)} proxies to {filename}')

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



    print('Select Proxy Type:')
    print('1. Socks4 Proxies')
    print('2. HTTP Proxies')
    print('3. SSL Proxies')
    print('4. US Proxies')
    print('5. All Proxies')

    option = int(input())

    if option == 1:
        proxies = get_socks4_proxies()
        proxy_type = 'SOCKS4'
    elif option == 2:
        proxies = get_http_proxies()
        proxy_type = 'HTTP'
    elif option == 3:
        proxies = get_ssl_proxies()
        proxy_type = 'SSL'
    elif option == 4:
        proxies = get_us_proxies()
        proxy_type = 'US'
    elif option == 5:
        proxies = get_all_proxies()
        proxy_type = 'ALL'
    else:
        print('Invalid option')
        return

    print(f'Found {len(proxies)} {proxy_type} proxies:')
    for proxy in proxies:
        print(colored(f'{proxy_type}: ', 'red') + json.dumps(proxy))





if __name__ == '__main__':
    main()
