# Текстовый редактор на Python
Добро пожаловать в текстовый редактор на Python! Этот проект создан для облегчения редактирования текстовых файлов с удобным интерфейсом и набором полезных функций.

## Описание проекта
Добро пожаловать в текстовый редактор на Python! Целью данного проекта является создание текстового редактора на языке Python с базовым набором функций для редактирования текстовых файлов. Редактор будет обладать интуитивно понятным пользовательским интерфейсом и поддерживать основные операции редактирования текста.

## Реализуемый функционал
- **Возможность редактирования файла:** Открывайте, сохраняйте и создавайте новые текстовые файлы.
- **Навигация по тексту:** Перемещайтесь по тексту с помощью стрелок, удаляйте строки и слова.
- **Поиск и замена:** Ищите и заменяйте текстовые фрагменты в файле.
- **Хоткеи:** Используйте горячие клавиши для сохранения изменений и выхода из редактора.
- **Настройки внешнего вида:** Меняйте тему оформления и шрифт текста по вашему вкусу.

## Архитектура
Проект организован по принципам объектно-ориентированного программирования. Он состоит из следующих основных компонентов:
- **NotepadApp (Приложение Notepad):** Основной класс приложения, наследник Tk.
- **create_menu():** Метод для создания меню приложения.
- **change_theme(theme):** Метод для изменения темы оформления.
- **create_text_field():** Метод для создания текстового поля.
- **change_font(font):** Метод для изменения шрифта текста.

