from pygments import highlight
import requests
from bs4 import BeautifulSoup

def weather(city):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    res = requests.get(
        f'https://www.google.com/search?q=마다가스카르+날씨',
        headers=headers)
    print("Searching...\n")
    soup = BeautifulSoup(res.text, 'html.parser')
    location = soup.select('#wob_loc')[0].getText().strip()
    time = soup.select('#wob_dts')[0].getText().strip()
    info = soup.select('#wob_dc')[0].getText().strip()
    weather = soup.select('#wob_tm')[0].getText().strip()
    high = soup.select('div.gNCp2e')[0].getText().strip()
    low = soup.select('div.QrNVmd.ZXCv8e')[0].getText().strip()

    print(location)
    print(time)
    print(info)
    print(weather + "°C")
    print("low : ", low)
    print("low len: ", len(low))
    
    if len(high) < 5:
        print(high[:1] + "°C")
    else:
        print(high[:2] + "°C")

    if len(low) < 5:
        print(low[:1] + "°C")
    else:
        print(low[:2] + "°C")
    # print(low[:2] + "°C")

if __name__ == "__main__":
    city = "seoul"
    weather(city)