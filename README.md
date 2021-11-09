# xmlreader
# Во время написания команд нужно находится внутри loadfile 
Переместите папки с архивами , в папку put_xml_here что находится в папке media
Находясь в папке loadfile нажмие ПКМ, открыть в терминале
Пропишите команду sudo su 
введите пароль супер пользователя

(Если добавление файлов происходит не в первый раз достаточно одной команды docker-compose up -d  --build	)

Сделайте билд  docker-compose up -d  --build
Проведите миграции docker-compose exec web python manage.py migrate --noinput

Запустите контейнер используя команду docker-compose up -d  --build


Либо docker-compose up --build чтобы процесс не был фоновым

Откройте в браузере ссылку http://0.0.0.0:8000/

Нажмите кнопку "Запустить", после чего ждите окончания загрузки


Чтобы подключится к базе к примеру через PgAdmin4 или DbGate
1. Введите команду чтобы узнать название контейнера docker network ls
2. Введите команду docker network inspect Название , к примеру docker network inspect loadfile_default
3. Найдите и скопируйте IPv4Address под  loadfile_db_1
4. Используйте данный айпи для подключения с портом 5432, текущий пароль 123456 логин postgres
К примеру можно подключится через:
1.DbGate 
	В верхнем меню нажмите кнопку Add Connection

	В Database engine Выберите  Postgre SQL

	Введиде в  Server -  айпи из пункта 3 выше ,Введите в  Port - 5432
	Введите в User - postgres,Введите в  Password - 123456

	Нажмите кнопку  test для проверки, если появилась галочка, нажмите кнопку Save
	Если нет, проверьте корректность введенных данных


2. pgAdmin4
	 -> Servers -> Create -> Server
	 -> General
	 Name - Любое
	 -> Connection
	 Host name/address - айпи из пункта 3,
	 Port - 5432
	 Username - postgres
	 Password - 123456
	 -> Save
	 
Для того чтобы достать какой-либо файл из контейнера введите команду docker ps скопируйте оттуда CONTAINER ID для loadfile_web
используйте команду  docker cp айди_контейнера:/путь_к_файлу_внутри_конейнера /куда_сохранить файл
к примеру  docker cp b436c9dc8d6b:app/file_view_log.txt /home/


Если вам нужно отчистить базу введите docker exec -ti loadfile_web_1 /bin/sh
затем python manage.py flush
после чего оно предложит ввести yes 

если возникнет ошибка, что файл manage.py не найден, вернитесь в loadfile 


Чтобы достать дамп базы из контейнера введите:
Где вместо <id> введите айди контейнера postgres из   docker ps , а после >напишите путь по которому нужно создать бэкап 
 docker exec <id> pg_dump -U postgres -F t django_db_xml | gzip >(путь)/backup.tar.gz
 к примеру
 docker exec 2a5a5f9e2f5f pg_dump -U postgres -F t django_db_xml | gzip >/home/denis/backup/backup.tar.gz

Если нужно освободить порт введите fuser -k 8000/tcp    



