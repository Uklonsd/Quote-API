from flask import Flask, jsonify, send_from_directory
import random
import os

app = Flask(__name__)

@app.route("/")
def index():
  return send_from_directory(os.path.join(app.root_path, "static"), "index.html")

QUOTES = {
  "Альберт Ейнштейн": {
    "quote": "Уява важливіша за знання.",
    "image": "/static/photo/Albert_Einstein_Head.jpg"
  },
  "Стів Джобс": {
    "quote": "Будь голодним. Будь безрозсудним.",
    "image": "/static/photo/_dzhobs_gettyimages_98328574_4e82378a0c40bb75f1e0778c95270bea_1200x675.jpg"
  },
  "Оскар Вайлд": {
    "quote": "Будь собою; інші ролі вже зайняті.",
    "image": "/static/photo/Oscar_Wilde_portrait.jpg"
  },
  "Махатма Ганді": {
    "quote": "Будь зміною, яку хочеш бачити у світі.",
    "image": "/static/photo/Makhatma-Handi.jpg"
  },
  "Вінстон Черчилль": {
    "quote": "Успіх — це рух від невдачі до невдачі без втрати ентузіазму.",
    "image": "/static/photo/Черчиль.jpg"
  },
  "Томас Едісон": {
    "quote": "Я не зазнав поразки — я знайшов 10 000 способів, які не працюють.",
    "image": "/static/photo/Thomas_Edison2.jpg"
  },
  "Конфуцій": {
    "quote": "Шлях у тисячу миль починається з одного кроку.",
    "image": "/static/photo/Konfuzius-1770.jpg"
  },
  "Лев Толстой": {
    "quote": "Щастя не в тому, щоб володіти всім, а в тому, щоб радіти всьому.",
    "image": "/static/photo/Фотопортрет_Л._Толстого_(Шерер,_Набгольц_и_Ко)_(cropped).jpg"
  },
  "Сенека": {
    "quote": "Не той багатий, хто має багато, а той, хто мало потребує.",
    "image": "/static/photo/Seneca.jpg"
  },
  "Брюс Лі": {
    "quote": "Будь водою, друже мій.",
    "image": "/static/photo/Bruce_Lee_1973.jpg"
  },
  "Вольтер": {
    "quote": "Сумнівайтесь у всьому, навіть у тому, що я кажу.",
    "image": "/static/photo/Atelier_de_Nicolas_de_Largillière,_portrait_de_Voltaire,_détail_(musée_Carnavalet)_-001.jpg"
  },
  "Фрідріх Ніцше": {
    "quote": "Те, що нас не вбиває, робить нас сильнішими.",
    "image": "/static/photo/Nietzsche187a.jpg"
  },
  "Маркус Аврелій": {
    "quote": "Життя кожної людини — це те, що вона думає про нього.",
    "image": "/static/photo/Marcus_Aurelius_Louvre_MR561_n02.jpg"
  },
  "Наполеон Хілл": {
    "quote": "Думай і багатій.",
    "image": "/static/photo/1_4_15.jpg"
  },
  "Арістотель": {
    "quote": "Ми — це те, що ми робимо постійно.",
    "image": "/static/photo/Aristotle_Altemps_Inv8575.jpg"
  },
  "Далай-лама": {
    "quote": "Мета життя — бути щасливим.",
    "image": "/static/photo/Dalailama1_20121014_4639.jpg"
  },
  "Нельсон Мандела": {
    "quote": "Все здається неможливим, доки не буде зроблено.",
    "image": "/static/photo/Nelson_Mandela_1994.jpg"
  },
  "Бенджамін Франклін": {
    "quote": "Час — це гроші.",
    "image": "/static/photo/franklin2.jpg"
  },
  "Ілон Маск": {
    "quote": "Постійно ставте під сумнів себе.",
    "image": "/static/photo/The_White_House_-_54409525537_(cropped).jpg"
  },
  "Білл Гейтс": {
    "quote": "Ваші найнещасніші клієнти — найкраще джерело навчання.",
    "image": "/static/photo/thumbs_b_c_bdcdadcdfa280c641e6ced185e6de2b5.jpg"
  },
  "Ісаак Ньютон": {
    "quote": "Якщо я бачив далі, то тому що стояв на плечах гігантів.",
    "image": "/static/photo/GodfreyKneller-IsaacNewton-1689.jpg"
  },
  "Сократ": {
    "quote": "Я знаю лише те, що нічого не знаю.",
    "image": "/static/photo/Socrates_Louvre.jpg"
  },
  "Генрі Форд": {
    "quote": "Чи ти думаєш, що зможеш, чи ні — ти маєш рацію.",
    "image": "/static/photo/Henry_ford_1919.jpg"
  },
  "Пабло Пікассо": {
    "quote": "Натхнення існує, але воно повинно застати вас за роботою.",
    "image": "/static/photo/Pablo_picasso_1.jpg"
  },
  "Йоганн Гете": {
    "quote": "Зроби перший крок — і побачиш шлях.",
    "image": "/static/photo/istockphoto-96691028-612x612.jpg"
  },
  "Жан-Жак Руссо": {
    "quote": "Свобода — це послух закону, який ти сам собі встановив.",
    "image": "/static/photo/1200px-Jean-Jacques_Rousseau_(painted_portrait).jpg"
  },
  "Бернард Шоу": {
    "quote": "Розумна людина пристосовується до світу.",
    "image": "/static/photo/George_Bernard_Shaw_1909.jpg"
  },
  "Лао-цзи": {
    "quote": "Той, хто знає інших — мудрий. Той, хто знає себе — просвітлений.",
    "image": "/static/photo/Lao_Tzu_-_Project_Gutenberg_eText_15250.jpg"
  },
  "Джон Леннон": {
    "quote": "Життя — це те, що з тобою відбувається, поки ти будуєш інші плани.",
    "image": "/static/photo/John_Lennon,_1974_(restored_cropped).jpg"
  },
  "Карл Юнг": {
    "quote": "Хто дивиться зовні — мріє, хто дивиться всередину — пробуджується.",
    "image": "/static/photo/lossy-page1-640px-ETH-BIB-Jung,_Carl_Gustav_(1875-1961)-Portrait-Portr_14163_(cropped).tif.jpg"
  }
}


@app.route("/quote")
def quote():
  author, data = random.choice(list(QUOTES.items()))
  return jsonify({
    "author": author,
    "quote": data["quote"],
    "image": data.get("image", None)
  })

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5000)
