import requests
import bs4
import re

session = requests.session()


def get_zhilian(share_url):
    index_url = 'https://www.lanzous.com'
    headers = {
        'Upgrade-Insecure-Requests': '1',
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "max-age=0",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3672.400 QQBrowser/10.4.3448.400"
    }
    share_html_text = session.get(url=share_url, headers=headers).text
    share_html_bs4 = bs4.BeautifulSoup(share_html_text, "lxml")
    src_url = share_html_bs4.find('iframe', attrs={'class': 'ifr2'})['src']
    downloads_url = index_url + src_url
    headers_d = {
        "x-requested-with": "XMLHttpRequest",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "origin": "https://www.lanzous.com",
        "referer": downloads_url,
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "max-age=0",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3672.400 QQBrowser/10.4.3448.400"
    }
    downloads_page = session.get(url=downloads_url, headers=headers).text
    try:
        sign = re.search('sign.{89}', downloads_page).group()[7:89]
    except:
        sign = re.search('var ajaxup = \'.{0,100}\';', downloads_page).group()[13:-2]

    ajaxm_url = 'https://www.lanzous.com/ajaxm.php'

    data = {
        'action': 'downprocess',
        'sign': sign,
        'ves': 1
    }
    file_data = session.post(url=ajaxm_url, data=data, headers=headers_d).json()
    zhilian = str(file_data['dom']) + '/file/' + str(file_data['url']) + '='
    return zhilian


if __name__ == '__main__':
    i = 0
    while True:
        i = i + 1
        print(i)
        print(get_zhilian('https://www.lanzous.com/i6aa3hg'))
