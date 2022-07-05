from pygments import highlight
import requests
from bs4 import BeautifulSoup

def weather(city):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    res = requests.get(
        f'https://www.google.com/search?q=에베레스트+날씨',
        headers=headers)
    print("Searching...\n")
    soup = BeautifulSoup(res.text, 'html.parser')
    location = soup.select('#wob_loc')[0].getText().strip()
    time = soup.select('#wob_dts')[0].getText().strip()
    info = soup.select('#wob_dc')[0].getText().strip()
    weather = soup.select('#wob_tm')[0].getText().strip()
    high = soup.find_all('div', {'class':'gNCp2e'})[0].find('span', {'style':'display:inline'}).text
    low = soup.find_all('div', {'class':'QrNVmd ZXCv8e'})[0].find('span', {'style':'display:inline'}).text

    print(location)
    print(time)
    print(info)
    print(weather + "°C")
    print(high)
    print(low)

if __name__ == "__main__":
    city = "seoul"
    weather(city)