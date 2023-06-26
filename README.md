## Шифратор текста

Скрипт на Python, реализующий шифр Виженера, Цезаря. Также поддерживает расшифровку шифра Виженера методом частотного анализа

### Работа со скриптом
`python3 encryptor.py [--input-file INPUT_FILE] [--output-file OUTPUT_FILE] {encode, decode, hack} ...`

`INPUT_FILE` - файл ввода

`OUTPUT_FILE` - файл вывода

`{encode, decode} [--cipher {caesar, vigenere}] [--key KEY]` - шифровка/расшифровка Цезарем/Виженером с указанным ключом `KEY`

`hack` - расшифровка шифра Виженера частотным анализом
