## Lab_4: Робота з Docker

2. Для перевірки чи докер встановлений і працює правильно на віртуальній машині запустив перевірку версії, виведення допомоги та тестовий імедж:
    ```bash
    docker -v
    docker -h
    docker run docker/whalesay cowsay Docker is fun
    ```
    - перенаправив вивід цих команд у файл `my_work.log` та закомітив його до репозиторію.
4. Створимо імедж із Django сайтом зробленим у попередній роботі.
    - Оскільки проект на Python то і базовий імедж також потрібно вибрати відповідний.
    ```bash
    docker pull python:3.9-slim-buster
    docker images
    docker inspect python:3.9-slim-buster
    ```
    - Створив файл з іменем `Dockerfile` скопіював туди вміс такого ж файлу з  репозиторію викладача
    - Ознайомився із коментарями та  зрозумів структуру написання Dockerfile;
    - Замінив посилання на власний Git репозиторій із  веб-сайтом та закомітив даний Dockerfile*
5. Створив власний репозиторій на Docker Hub. 
6. Виконав білд (build) Docker імеджа та завантажив його до репозиторію.
    ```bash
    docker build -t vitaliykuz/lab4_bobas:django .
    docker images
    dokcer push vitaliykuz/lab4_bobas:django
    ```
   [Docker link](https://hub.docker.com/repository/docker/vitaliykuz/lab4_bobas) and [image link](https://hub.docker.com/layers/178493933/vitaliykuz/lab4_bobas/django/images/sha256-a983a6a3dd0dbc2d318e36498d6f8d11746a7c55881f66d36660db9cd238d409?context=repo)
7. Для запуску веб-сайту  виконав команду 
    ```bash
    docker run -it --name=django --rm -p 8000:8000 vitaliykuz/lab4_bobas:django
    ``` 
    - перейшов на адресу `http://127.0.0.1:8000` та переконався що Ваш веб-сайт працює;
8. Створит ще один контейнер із програмою моніторингу нашого веб-сайту 
    - створив ще один Dockerfile в якому помістив програму моніторингу 
   
      - виконав білд даного імеджа та дав йому тег `monitoring`;
   ```shell
   docker build -t vladgrz/lab_4 -f Dockerfile.monitoring .
   docker tag vitaliykuz/lab4_bobas vitaliykuz/lab4_bobas:monitoring
   docker push vitaliykuz/lab4_bobas:monitoring
   ```
    - запустив два контейнери одночасно  та переконався що програма моніторингу успішно доступається до сторінок  веб-сайту 
   ```shell
   docker run -it --name=django --rm -p 8000:8000 vitaliykuz/lab4_bobas:django
   ```
   ```shell
      docker run -it --name=monitoring --rm --net=host -v $(pwd)/server.log:/app/server.log vitaliykuz/lab4_bobas:monitoring

   ```
    - закомітив Dockerfile та результати роботи програми моніторингу запущеної з Docker контейнера 