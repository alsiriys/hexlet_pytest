def reverse(string):
    return string[::-1]

def test_reverse_with_long_text():
    # 1. Читаем исходный длинный текст
    with open("test_data/input.txt", "r", encoding="utf-8") as file:
        source_text = file.read()

    # 2. Читаем заранее подготовленный эталонный перевернутый текст
    with open("test_data/expected_output.txt", "r", encoding="utf-8") as file:
        expected_text = file.read()

    # 3. Переворачиваем текст с помощью нашей функции
    actual_text = reverse(source_text)

    # 4. Проверяем совпадение с помощью утверждения (assert)
    assert actual_text == expected_text, "Ошибка! Результат функции не совпадает с ожидаемым."
    
    print("Тест успешно пройден! Функция reverse() корректно обработала длинный текст.")

# Запуск теста
if __name__ == "__main__":
    test_reverse_with_long_text()