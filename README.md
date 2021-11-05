# xmlreader
# Во время написания команд нужно находится внутри loadfile 
Переместите папки с архивами , в папку put_xml_here что находится в папке media


(Если добавление файлов происходит не в первый раз достаточно одной команды docker-compose up -d  --build	)

Сделайте билд  docker-compose build
Проведите миграции docker-compose exec web python manage.py migrate --noinput

Находясь в корне проекта запустите контейнер используя команду docker-compose up -d  --build


Либо docker-compose up --build чтобы процесс не был фоновым

Откройте в браузере ссылку http://"ip сервера":8000/

Нажмите кнопку "Запустить", после чего ждите окончания загрузки


Чтобы подключится к базе к примеру через PgAdmin4 или DbGate
1. Введите команду чтобы узнать название контейнера docker network ls
2. Введите команду docker network inspect Название , к примеру docker network inspect loadfile_default
3. Найдите и скопируйте IPv4Address
4. Используйте данный айпи для подключения с портом 5432, текущий пароль 123456 логин postgres

1.DbGate 
	->Add Connection

	Database engine - Postgre SQL

	Server -  айпи из пункта 3 выше , Port 5432
	User - postgres Password 123456

	-> test
	-> save

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
