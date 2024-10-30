import os
import win32com.client


# Конвертация Word в PDF
def convert_doc_in_pdf(file_path, output_directory):
    # Создание экземпляра Word
    word = win32com.client.Dispatch("Word.Application")
    word.Visible = False

    # Название файла без расширения
    output_file_name = os.path.splitext(os.path.basename(file_path))[0] + '.pdf'

    # Полный путь к выходному файлу
    output_file_path = os.path.join(output_directory, output_file_name)

    try:
        # Открытие документа
        doc = word.Documents.Open(file_path)

        # Сохранение документа в формате PDF
        doc.SaveAs2(output_file_path, FileFormat=17)  # 17 соответствует формату PDF
        doc.Close()

    except Exception as e:
        raise Exception(f"Произошла ошибка: {e}")

    finally:
        # Завершение работы Word
        word.Quit()

    return output_file_path

