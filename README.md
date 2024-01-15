## `EN` - Simple Stable Diffusion UI built on hugging's face diffusers.
### Requirements:
- python 3.9
### Installation:
Copy files to folder and run `pip install -r requirements.txt` (venv recommended)

### Usage:
- Put your checkpoints to 'models' folder.
- You can change default checkpoint's folder, size, steps and guidance scale in config.json
- launch `python simple_sd_ui.py`
- Open browser and go to 127.0.0.1:7860
- Select checkpoint from dropdown list, type positive and negative prompts and press "Generate"

### Docker's usage:
- Be sure you have Nvidia Container Toolkit for using GPU
- For WSL users additional info:
[https://docs.nvidia.com/cuda/wsl-user-guide/](https://docs.nvidia.com/cuda/wsl-user-guide/)
- For Windows Docker Desktop launch from PowerShell:\
``docker run -it -p 7860:7860 --env NVIDIA_DISABLE_REQUIRE=1 --gpus all simple_sd_ui``
---
## `RU` - Удобный и простой интерфейс Stable Diffusion для генерации изображений.
### Требования:
- python 3.9
### Установка:
Скопируйте файлы в папку и запустите `pip install -r requirements.txt` (рекомендуется создание виртуального окружения venv)

### Использование:
- Скопируйте модели в папку 'models'.
- Вы можете изменить папку с моделями, размер по умолчанию и количество шагов сэмплера в файле config.json
- Запустите `python simple_sd_ui.py`
- Откройте браузер и перейдите по адресу 127.0.0.1:7860
- Выберите модель из списка, введите положительный и отрицательный промпт, при необходимости измените размер и нажмите "Generate"

### Использование в Docker:
- Убедитесь, что у вас установлен Nvidia Container Toolkit для использования GPU
- Дополнительная информация для пользователей WSL:
[https://docs.nvidia.com/cuda/wsl-user-guide/](https://docs.nvidia.com/cuda/wsl-user-guide/)
- Для запуска контейнера в Windows Docker Desktop используйте следующую команду в PowerShell:\
``docker run -it -p 7860:7860 --env NVIDIA_DISABLE_REQUIRE=1 --gpus all simple_sd_ui``

---
![image](https://github.com/wasidy/simple_sd_ui/assets/122546017/8f99a939-e36a-4a40-a32e-d4ecece5f3a8)
