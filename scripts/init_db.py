from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base, Quote

engine = create_engine('sqlite:///quotes.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

quotes_data = [
    ("Альберт Ейнштейн", "Уява важливіша за знання.", "/static/photo/Albert_Einstein_Head.jpg"),
    ("Стів Джобс", "Будь голодним. Будь безрозсудним.", "/static/photo/_dzhobs_gettyimages_98328574_4e82378a0c40bb75f1e0778c95270bea_1200x675.jpg"),
    ("Оскар Вайлд", "Будь собою; інші ролі вже зайняті.", "/static/photo/Oscar_Wilde_portrait.jpg"),
    ("Махатма Ганді", "Будь зміною, яку хочеш бачити у світі.", "/static/photo/Makhatma-Handi.jpg"),
    ("Вінстон Черчилль", "Успіх — це рух від невдачі до невдачі без втрати ентузіазму.", "/static/photo/Черчиль.jpg"),
    ("Томас Едісон", "Я не зазнав поразки — я знайшов 10 000 способів, які не працюють.", "/static/photo/Thomas_Edison2.jpg"),
    ("Конфуцій", "Шлях у тисячу миль починається з одного кроку.", "/static/photo/Konfuzius-1770.jpg"),
    ("Лев Толстой", "Щастя не в тому, щоб володіти всім, а в тому, щоб радіти всьому.", "/static/photo/Фотопортрет_Л._Толстого_(Шерер,_Набгольц_и_Ко)_(cropped).jpg"),
    ("Сенека", "Не той багатий, хто має багато, а той, хто мало потребує.", "/static/photo/Seneca.jpg"),
    ("Брюс Лі", "Будь водою, друже мій.", "/static/photo/Bruce_Lee_1973.jpg"),
    ("Вольтер", "Сумнівайтесь у всьому, навіть у тому, що я кажу.", "/static/photo/Atelier_de_Nicolas_de_Largillière,_portrait_de_Voltaire,_détail_(musée_Carnavalet)_-001.jpg"),
    ("Фрідріх Ніцше", "Те, що нас не вбиває, робить нас сильнішими.", "/static/photo/Nietzsche187a.jpg"),
    ("Маркус Аврелій", "Життя кожної людини — це те, що вона думає про нього.", "/static/photo/Marcus_Aurelius_Louvre_MR561_n02.jpg"),
    ("Наполеон Хілл", "Думай і багатій.", "/static/photo/1_4_15.jpg"),
    ("Арістотель", "Ми — це те, що ми робимо постійно.", "/static/photo/Aristotle_Altemps_Inv8575.jpg"),
    ("Далай-лама", "Мета життя — бути щасливим.", "/static/photo/Dalailama1_20121014_4639.jpg"),
    ("Нельсон Мандела", "Все здається неможливим, доки не буде зроблено.", "/static/photo/Nelson_Mandela_1994.jpg"),
    ("Бенджамін Франклін", "Час — це гроші.", "/static/photo/franklin2.jpg"),
    ("Ілон Маск", "Постійно ставте під сумнів себе.", "/static/photo/The_White_House_-_54409525537_(cropped).jpg"),
    ("Білл Гейтс", "Ваші найнещасніші клієнти — найкраще джерело навчання.", "/static/photo/thumbs_b_c_bdcdadcdfa280c641e6ced185e6de2b5.jpg"),
    ("Ісаак Ньютон", "Якщо я бачив далі, то тому що стояв на плечах гігантів.", "/static/photo/GodfreyKneller-IsaacNewton-1689.jpg"),
    ("Сократ", "Я знаю лише те, що нічого не знаю.", "/static/photo/Socrates_Louvre.jpg"),
    ("Генрі Форд", "Чи ти думаєш, що зможеш, чи ні — ти маєш рацію.", "/static/photo/Henry_ford_1919.jpg"),
    ("Пабло Пікассо", "Натхнення існує, але воно повинно застати вас за роботою.", "/static/photo/Pablo_picasso_1.jpg"),
    ("Йоганн Гете", "Зроби перший крок — і побачиш шлях.", "/static/photo/istockphoto-96691028-612x612.jpg"),
    ("Жан-Жак Руссо", "Свобода — це послух закону, який ти сам собі встановив.", "/static/photo/1200px-Jean-Jacques_Rousseau_(painted_portrait).jpg"),
    ("Бернард Шоу", "Розумна людина пристосовується до світу.", "/static/photo/George_Bernard_Shaw_1909.jpg"),
    ("Лао-цзи", "Той, хто знає інших — мудрий. Той, хто знає себе — просвітлений.", "/static/photo/Lao_Tzu_-_Project_Gutenberg_eText_15250.jpg"),
    ("Джон Леннон", "Життя — це те, що з тобою відбувається, поки ти будуєш інші плани.", "/static/photo/John_Lennon,_1974_(restored_cropped).jpg"),
    ("Карл Юнг", "Хто дивиться зовні — мріє, хто дивиться всередину — пробуджується.", "/static/photo/lossy-page1-640px-ETH-BIB-Jung,_Carl_Gustav_(1875-1961)-Portrait-Portr_14163_(cropped).tif.jpg")
]


for author, quote, image in quotes_data:
    session.add(Quote(author=author, quote=quote, image=image))

session.commit()
