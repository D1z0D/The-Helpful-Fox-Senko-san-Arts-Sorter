# The-Helpful-Fox-Senko-san-Arts-Sorter
### 🌍 Languages 
[![English](https://img.shields.io/badge/English-100%25-red)](README.md)
[![Russian](https://img.shields.io/badge/Русский-100%25-blue)](README_ru.md)

У тебя папка с 3000 артов с Сэнко, Широ и Сорой? Просто закинь их в скрипт, который автоматически расфасует их по полочкам!

Это обученная модель на основе "YOLO". На вход идут: папка с изображениями и путь до папки где будет производиться сортировка.

<img width="573" height="219" alt="2025-08-28-205419_hyprshot" src="https://github.com/user-attachments/assets/9406ffe7-7f4f-4c81-ac88-1ef67058fc16" />

По окончании детекции, по указанному пути вас будет ждать папка "Undetected" и "The Helpful Fox Senko-san" в которой вы увидите папки с вашими отсортированными артами!

<img width="488" height="174" alt="2025-08-28-205003_hyprshot" src="https://github.com/user-attachments/assets/e1d358d4-6e22-4fb4-8381-fa30ce403d10" />

## 📦 Установка

### Windows
```bash
# Скачайте и запустите install.bat
git clone https://github.com/D1z0D/The-Helpful-Fox-Senko-san-Arts-Sorter.git
cd The-Helpful-Fox-Senko-san-Arts-Sorter
install.bat
```

### GNU/Linux and Mac OS
```bash
# Скачайте и запустите install.sh
git clone https://github.com/D1z0D/The-Helpful-Fox-Senko-san-Arts-Sorter.git
cd The-Helpful-Fox-Senko-san-Arts-Sorter
./install.sh
```

## 🚀 Использование

1. Запустите приложение:

### Windows
```bash
# Запустите python-файл
python gui.py
```

### GNU/Linux and Mac OS
```bash
# Активируйте виртуальное окружение и запустите python-файл
source venv/bin/activate # или activate.fish если вы используете fish shell
python3 gui.py
```

2. Выберите папку с изображениями
3. Выберите директорию в которой будут отсортированные арты
4. Нажмите "Launch"
5. Ждите завершения обработки!

## 📝 Лицензия

Этот проект лицензирован под MIT License - подробности в файле [LICENSE](LICENSE).

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
