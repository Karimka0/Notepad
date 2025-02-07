# Текстовый редактор на Python
Добро пожаловать в текстовый редактор на Python! Этот проект создан для облегчения редактирования текстовых файлов с удобным интерфейсом и набором полезных функций.

## Описание проекта
Добро пожаловать в текстовый редактор на Python! Целью данного проекта является создание текстового редактора на языке Python с базовым набором функций для редактирования текстовых файлов. Редактор будет обладать интуитивно понятным пользовательским интерфейсом и поддерживать основные операции редактирования текста.

## Реализуемый функционал
- **Возможность редактирования файла:** Открывайте, сохраняйте и создавайте новые текстовые файлы.
- **Навигация по тексту:** Перемещайтесь по тексту с помощью стрелок, удаляйте строки и слова.
- **Поиск и замена:** Ищите и заменяйте текстовые фрагменты в файле.
- **Удаление строк и слов:** Удаляйте слова или целые строки.
- **Хоткеи:**
  - Ctrl+O: Открыть файл.
  - Ctrl+S: Сохранить файл.
  - Ctrl+X: Закрыть редактор.
  - Ctrl+F: Открыть окно поиска.
  - Ctrl+T: Поменять тему.
- **Настройки внешнего вида:** Меняйте тему оформления и шрифт текста по вашему вкусу.

## Архитектура
Проект организован по принципам объектно-ориентированного программирования. Он состоит из следующих основных компонентов:

- **NotepadApp (Приложение Notepad):** Основной класс приложения, наследник Tk.
    - `create_menu():` Метод для создания меню приложения.
    - `change_theme(theme):` Метод для изменения темы оформления.
    - `create_text_field():` Метод для создания текстового поля.
    - `show_info(font):` Метод для изменения шрифта текста.
    - `fast_change_theme(font):` Метод для изменения шрифта текста.
    - `notepad_exit(font):` Метод для изменения шрифта текста.
    - `open_file(font):` Метод для изменения шрифта текста.
    - `save_file(font):` Метод для изменения шрифта текста.
    - `search_word(font):` Метод для изменения шрифта текста.
    - `search(font):` Метод для изменения шрифта текста.
    - `highlight(font):` Метод для изменения шрифта текста.
    - `delete_highlight(font):` Метод для изменения шрифта текста.

## Запуск

1. Склонируйте репозиторий на свой компьютер:
    ```
    git clone https://github.com/Karimka0/Notepad
    ```
3. Чтобы просмотреть документацию, перейдите в ветку documentation и откройте файл README.md с помощью любого текстового редактора, например так
    ```
    git checkout documentation
    nano README.md
    ```
3. Чтобы запустить программу, перейдите в ветку dev и выполните в консоли команду
    ```
    git checkout dev
    python3 Notepad.py
    ```
    Либо просто запустите исполняемый файл Notepad


## Автор

Автор: Karim Mazitov, Б05-322
Контактная информация: https://t.me/KarimMazitov

