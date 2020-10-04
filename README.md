***Написать на Django и django REST Framework "Меню ресторана"***


- У каждого пункта меню есть название, пищевая ценность, цена, картиночка и список аллергенов.

- Все блюда разбиты по категориям.

- На главной странице выводится список всех блюд из меню, сгруппированных по категориям, с галочками и кнопкой отправить которая переходит на страницу, где вычислена сумма заказа, выведен список блюд и ниже показан список аллергенов, которые содержатся в выбранных блюдах.

- У сайта есть API, позволяющий добавлять блюдо в меню (на главной), с указанием цены и пищевой ценности, загружать картинку и получать список блюд. В качестве защиты используется один токен, указанный в настройках.

- Написать тест на API метод добавления элемента в меню.

- На главной странице показывать ссылку на Paste в сервисе https://pastebin.com в котором содержится список всех блюд с указанием названия и цены.

- Создание Paste реализовать в асинхронной задаче Celery.

- Для создания Paste нельзя использовать готовые обертки на API, надо использовать библиотеку requests.

- Результат удобно оформить в виде репозитория на github

- Требований к верстке нет, никакой красоты наводить не надо.

- Настроить локальную разработку на основе Docker и docker-compose