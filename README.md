### **Описание проекта:**

Скрипт для загрузки файлов на google диск


### **Установка:**

Версия python >= 3.8

Создаем сервисный аккаунт в консоли [Google Cloud](console.cloud.google.com) и для email сервисного аккаунта открываем доступ на редактирование необходимых папок на гугл диске куда будем загружать файлы. [Пример как получить ключ для сервисного аккаунта в формате JSON](https://www.youtube.com/watch?v=Lxxge05UP8M&feature=emb_logo)

Копируем JSON файл в папку /settings

### **Команда upload_backup:**

Создает бэкап папки на google диске. Проверяет их количество на google диске и удаляет лишние 

 `python upload_backup.py -f {file_path} -i {id_root_directory} -m {max_count_backup} -n {name_backup_folder}`

где:
 - `-f {file_path}`, где file_path - это полный путь до файла, который находится на локальном компьютере
 - `-i {id_root_directory}`, где id_root_directory - это id папки на гугл диске, куда нужно скопировать файл
 - `-m {max_count_backup}`, где max_count_backup - это количество копий которые должны хранится на гугл диске
 - `-n {name_backup_folder}`, где name_backup_folder - это название корневой папки, которая будет создана на гугл диске и в которую будет помещен бэкап

Обязательные ключи:
 - `-f {file_path}`
 - `-i {id_root_directory}`

Не обязательные ключи:
 - `-m {max_count_backup}`, значение по умолчанию '1'
 - `-n {name_backup_folder}` значение по умолчанию 'backup_server__%d_%m_%Y__%H_%M_%S', где %d_%m_%Y__%H_%M_%S дата и время. Пример: backup_server__01_01_1970__01_01_01