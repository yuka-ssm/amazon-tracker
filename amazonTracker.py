import requests
from bs4 import BeautifulSoup


amazonURL = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

def amazonTrackingPrice():
    amazonPage = requests.get(amazonURL)
    soup = BeautifulSoup(amazonPage.content, "html.parser")

    title = soup.find(id="productTitle").get_text()
    price=soup.find("span", class_="a-price-whole").get_text()
    convertedPrice = price.replace(",", "")
    intPrice = int(convertedPrice)

    if(intPrice > 3000):
        sendLineNotify()



def sendLineNotify():
    lineNotifyToken = "aaaaaaaaaaaaaaaaaaaaaaa"
    lineNotifyAPI = "https://notify-api.line.me/api/notify"
    headers = {"Authorization": f"Bearer {lineNotifyToken}"}
    data = {"message": "今が買い時です！xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"}
    
    requests.post(lineNotifyAPI, headers=headers, data=data)
    
    print("LINEに通知が行きました")


amazonTrackingPrice()