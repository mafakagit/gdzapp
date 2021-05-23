import requests
from bs4 import BeautifulSoup
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.label import Label

Window.clearcolor = (.21, .83, .82, 1)

HOST = "https://gdz.ru/class-8/english/reshebnik-spotlight-8-angliyskiy-v-fokuse-vaulina-yu-e/"
#page = input("Введите страницу ")


def get_images(url):
    responce = requests.get(url)
    html = responce.text
    soup = BeautifulSoup(html, 'html.parser')
    all_image = soup.find_all("div", class_="task-img-container")
    links = []
    for image in all_image:
        image_link = image.find("img").get("src")
        image_link = "https:" + image_link
        links.append(image_link)
    return links


class Mypop(Popup):
    def opened(self):
       global page
       url = HOST+page+"-s/"
       self.images = get_images(url)
       self.page2 = 0
       self.sync.source = self.images[0]
    def rightcl(self):
        self.page2 += 1
        if self.page2 < len(self.images):
            self.sync.source = self.images[self.page2]

    def leftcl(self):
        if self.page2 > 0:
            self.page2 -= 1
            self.sync.source = self.images[self.page2]

class Container(Widget):
    def clicked(self):
        global page
        page = self.txt1.text
        url = HOST+page+"-s/"
        
        self.images = get_images(url)
        self.page2 = 0
        

    


class GdzApp(App):
    def build(self):
        return Container()
        return Mypop()


if __name__ == "__main__":
    GdzApp().run()
