# artemis-api
REST API for the Artemis School Management System written in the Django Rest Framework for Python

## License
MIT license

## Docs

Documentation with all the available endpoints of this API can be found at LOCALHOST:8000/redoc

## Running

1) Install required dependencies using ```pip3 install -r requirements.txt```


2) Run ```python3 manage.py migrate``` to create all database tables. Note that this backend was designed with the intention using a MySQL database as its database


3) Create a .env file in the root directory and populate it with the following fields. An openweathermaps api key can be obtained on the openweathermaps website

    ```
    MYSQL_DB=
    MYSQL_USERNAME=
    MYSQL_PASSWORD=
    openweathermapsapikey=
    ```

3) Run ```python3 manage.py runserver``` to start the server. DON'T USE THIS DEVELOPMENT SERVER IN PRODUCTION!
## Contributing

This code is released "as is". Feel free to fork it if you wish, but no pull requests will be reviewed or accepted

## Acknowledgements

Although the actual coding part of this project was done by myself, would like to pay tribute to one person

- [@MikeRomaa](https://github.com/MikeRomaa) for showing me the ropes around Django and the Django Rest Framework for the backend. He's a real expert at this framework with a lot of experience under his belt with it, and helped me to understand many concepts before I started using this framework

# Contact
If you have any further questions, feel free to message me on github, or alternatively join my discord server and contact me there

[![DISCORD](https://img.shields.io/discord/591914197219016707.svg?label=Discord&logo=Discord&colorB=7289da&style=for-the-badge)](https://discord.gg/9RcdNvB)
