Это первой мой основной проект в роли разработчика. Это было прекрасно.

# Функционал
Данное приложение разрабатывалось по заказу, основной идеей была платная печать документов, используя специальные аппараты с экранами на window 10 с принтером. Сами аппараты статичны, и разбросаны по городу.

Для получения документа на печать есть два способа, первый через флешку, второй через почту (парсинг вложенных писем). Показаны будут только файлы с расширениями `pdf`, `docx` и `docs`, остальные будут недоступны. Для получения документа с почты, нужно просто отправить файл на указанное почту, программа сама перехватит документ.

Предпоказ работает по принципу конвертации файла в `pdf` (если он уже таковым не является), после создается изображение с каждой старицей и вывод их на экран. Сам файл будет распечатан в том разрешении, в котором пришел.

Далее можно выбрать количество копий, это общее количество листов, то есть если документ на 10 листов, и клиент выбирает две копии, то на выходе получится 20 листов.

Окно оплаты работает на `yookassa`, ссылка на операцию храниться в qr-коде, который можно отсканировать и оплатить, после нужно нажать на кнопку проверки и при успешной транзакции окно меняется на печать и выход к главному экрану.

На этом все. Спасибо за внимание 💕
