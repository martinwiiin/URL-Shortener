import requests


def shorten_link(full_link, link_name):
    API_key = 'e1db81b772eaa26f63a9e0c699630592da705'
    BASE_url = 'https://cutt.ly/api/api.php'

    payload = {'key': API_key, 'short': full_link, 'name':link_name}
    request = requests.get(BASE_url, params=payload)
    data = request.json()

    print(' ')

    try: 
        title = data['url']['title']
        short_link = data['url']['shortLink']

        print('Title:', title)
        print('Link:', short_link)
    except:
        status = data['url']['status']
        print('Error Status:', status)

link = input('Enter a Link: >> ')
name = input('Give your link a name: >> ')

shorten_link(link, name)
    

