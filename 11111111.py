import win32com.client

# Открываем Word
word = win32com.client.Dispatch("Word.Application")
word.Visible = True  # Делаем Word видимым

# Создаем новый документ
doc = word.Documents.Add()

# Добавляем текст в документ
doc.Content.Text = "Пример текста для печати."

# Вызываем меню печати
doc.PrintOut()

# Закрываем документ (по желанию, можно сохранить)
# doc.Close(SaveChanges=True)  # Сохранить изменения, если нужно
word.Quit()  # Закрываем Word
