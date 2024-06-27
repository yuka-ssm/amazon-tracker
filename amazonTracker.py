import requests
from bs4 import BeautifulSoup


amazonURL = "https://www.amazon.co.jp/Python%E3%81%A7%E3%81%AF%E3%81%98%E3%82%81%E3%82%8B%E6%A9%9F%E6%A2%B0%E5%AD%A6%E7%BF%92-%E2%80%95scikit-learn%E3%81%A7%E5%AD%A6%E3%81%B6%E7%89%B9%E5%BE%B4%E9%87%8F%E3%82%A8%E3%83%B3%E3%82%B8%E3%83%8B%E3%82%A2%E3%83%AA%E3%83%B3%E3%82%B0%E3%81%A8%E6%A9%9F%E6%A2%B0%E5%AD%A6%E7%BF%92%E3%81%AE%E5%9F%BA%E7%A4%8E-Andreas-C-Muller/dp/4873117984/ref=sr_1_29?crid=1NSGPES2MGX82&dib=eyJ2IjoiMSJ9.Z1QSusfLZsM8aA4n4IkiY5o3mujh5IWrDTcg8ULrVtEqoOpSgJeR3Qmt3zHxm9KTnaqioeU3Fs6lRiKayK6zpWacjM3Y2dxkQTcCuEFyd6PL7FPOsy7gbEgfF4nY1z46VPSQAku8rRYcSDhaLEnBrKhHukguf_PAuYgUwqNKmjxJT_2FlyyO3wA-RcBH6T1I4DJD36PVGoRTlirKnVBxaLDEWnXvWZt0nLSJ7oCNiTUZF_gQ6Uu1wK-B4CBgfDQU4zqkuiBOMYXPDCHxhb4UruYl1jWkFx0aLbwHM8E4c04.20cNbCb3hGkNnaBOUT4NxbS1DBeBeonKbIAZVpKn-zM&dib_tag=se&keywords=python+%E3%82%AA%E3%83%A9%E3%82%A4%E3%83%AA%E3%83%BC&qid=1719495323&sprefix=Python+orairi%2Caps%2C185&sr=8-29"

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
    lineNotifyToken = "9hVtZgqzJ3UM9hHcnajQcrgjyD7nB53NIPrW7eI4I2S"
    lineNotifyAPI = "https://notify-api.line.me/api/notify"
    headers = {"Authorization": f"Bearer {lineNotifyToken}"}
    data = {"message": "今が買い時です！https://www.amazon.co.jp/Python%E3%81%A7%E3%81%AF%E3%81%98%E3%82%81%E3%82%8B%E6%A9%9F%E6%A2%B0%E5%AD%A6%E7%BF%92-%E2%80%95scikit-learn%E3%81%A7%E5%AD%A6%E3%81%B6%E7%89%B9%E5%BE%B4%E9%87%8F%E3%82%A8%E3%83%B3%E3%82%B8%E3%83%8B%E3%82%A2%E3%83%AA%E3%83%B3%E3%82%B0%E3%81%A8%E6%A9%9F%E6%A2%B0%E5%AD%A6%E7%BF%92%E3%81%AE%E5%9F%BA%E7%A4%8E-Andreas-C-Muller/dp/4873117984/ref=sr_1_29?crid=1NSGPES2MGX82&dib=eyJ2IjoiMSJ9.Z1QSusfLZsM8aA4n4IkiY5o3mujh5IWrDTcg8ULrVtEqoOpSgJeR3Qmt3zHxm9KTnaqioeU3Fs6lRiKayK6zpWacjM3Y2dxkQTcCuEFyd6PL7FPOsy7gbEgfF4nY1z46VPSQAku8rRYcSDhaLEnBrKhHukguf_PAuYgUwqNKmjxJT_2FlyyO3wA-RcBH6T1I4DJD36PVGoRTlirKnVBxaLDEWnXvWZt0nLSJ7oCNiTUZF_gQ6Uu1wK-B4CBgfDQU4zqkuiBOMYXPDCHxhb4UruYl1jWkFx0aLbwHM8E4c04.20cNbCb3hGkNnaBOUT4NxbS1DBeBeonKbIAZVpKn-zM&dib_tag=se&keywords=python+%E3%82%AA%E3%83%A9%E3%82%A4%E3%83%AA%E3%83%BC&qid=1719495323&sprefix=Python+orairi%2Caps%2C185&sr=8-29"}
    
    requests.post(lineNotifyAPI, headers=headers, data=data)
    
    print("LINEに通知が行きました")


amazonTrackingPrice()