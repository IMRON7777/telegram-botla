import requests
from bs4 import BeautifulSoup as BS

from knopkalar import viloyatlar_knopkasi

def start(update, context):
    user = update.message.from_user
    update.message.reply_html("Assalomyu Alaykom. <b>{}</b>.Hududni tanlang: ".format(user.first_name), reply_markup=viloyatlar_knopkasi)
    return 1

def toshkent(update, context):
    r = requests.get('https://sinoptik.ua/погода-ташкент')
    html =BS(r.content, 'html.parser')
    minimum = html.findAll
    maximum = html.findAll
def toshkent_viloyati(update, context):
    r = requests.get('https://sinoptik.ua/погода-ташкент')
    html =BS(r.content, 'html.parser')
    minimum = html.findAll
    maximum = html.findAll
def sirdaryo (update, context):
    r = requests.get('https://sinoptik.ua/погода-ташкент')
    html =BS(r.content, 'html.parser')
    minimum = html.findAll("div", {"class": "min"})
    maximum = html.findAll("div", {"class": "max"})
    t_min=minimum[0].text
    t_max=maximum[0].text
    update.message.reply_text(
        f"Siz Sirdaryoni tanladingizP: \n eng past: {t_min} gradus, \n eng yuqori {t_max}",reply_markup=viloyatlar_knopkasi
    )
def jizzax (update, context):
    r = requests.get('https://sinoptik.ua/погода-ташкент')
    html =BS(r.content, 'html.parser')
    maximum = html.findAll
    minimum = html.findAll
def samarqand (update, context):
    r = requests.get('https://sinoptik.ua/погода-ташкент')
    html =BS(r.content,'html.parser')
    maximum = html.findAll
    minimum = html.findAll
def fargona (update, context):
    r = requests.get('https://sinoptik.ua/погода-ташкент')
    html =BS(r.content, 'html.parser')
    maximum = html.findAll
    minimum = html.findAll
def namangan (update, context):
    r = requests.get('https://sinoptik.ua/погода-ташкент')
    html =BS(r.content, 'html.parser')
    maximum = html.findAll
    minimum = html.findAll
def andijon (update, context):
    r = requests.get('https://sinoptik.ua/погода-ташкент')
    html =BS(r.content, 'html.parser')
    maximum = html.findAll
    minimum = html.findAll
def qashqadaryo (update, context):
    r = requests.get('https://sinoptik.ua/погода-ташкент')
    html =BS(r.content, 'html.parser')
    maximum = html.findAll
    minimum = html.findAll
def surxondaryo (update, context):
    r = requests.get('https://sinoptik.ua/погода-ташкент')
    html =BS(r.content, 'html.parser')
    maximum = html.findAll
    minimum = html.findAll
def buxoro (update, context):
    r = requests.get('https://sinoptik.ua/погода-ташкент')
    html =BS(r.content, 'html.parser')
    maximum = html.findAll
    minimum = html.findAll
def xorazm (update, context):
    r = requests.get('https://sinoptik.ua/погода-ташкент')
    html =BS(r.content, 'html.parser')
    maximum = html.findAll
    minimum = html.findAll
def qoraqolpogiston (update, context):
    r = requests.get('https://sinoptik.ua/погода-ташкент')
    html =BS(r.content, 'html.parser')
    maximum = html.findAll
    minimum = html.findAll
def navoiy (update, context):
    r = requests.get('https://sinoptik.ua/погода-ташкент')
    html =BS(r.content, 'html.parser')
    maximum = html.findAll
    minimum = html.findAll