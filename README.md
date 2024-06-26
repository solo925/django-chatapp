
# Django WhatsApp-like Chat Application

chatapp/
├── chat/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── consumers.py
│   ├── models.py
│   ├── routing.py
│   ├── urls.py
│   ├── views.py
├── chatapp/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── manage.py
├── requirements.txt


This is a simple chat application built using Django, Django Channels, and Bootstrap. It supports real-time messaging, user authentication, file sharing, and group chats.

## Features

- **User Authentication:** Register, login, and logout using Django's built-in authentication system.
- **Real-time Messaging:** Real-time chat using WebSockets and Django Channels.
- **File Sharing:** Share files in chat.
- **Group Chats:** Create and join group chat rooms.
- **UI Improvements:** User-friendly interface with Bootstrap.

## Requirements

- Python 3.7+
- Django 3.1+
- Channels 3.0+
- Redis

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/chatapp.git
    cd chatapp
    ```

2. **Create a virtual environment:**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Set up Redis:**

    Follow the instructions on the [Redis website](https://redis.io/download) to install and start Redis.

5. **Apply migrations:**

    ```sh
    python manage.py migrate
    ```

6. **Create a superuser:**

    ```sh
    python manage.py createsuperuser
    ```

7. **Run the development server:**

    ```sh
    python manage.py runserver
    ```

8. **Start the Channels development server:**

    ```sh
    daphne -p 8001 chatapp.asgi:application
    ```

## Usage

1. Open your web browser and go to `http://127.0.0.1:8000`.
2. Register a new user or log in with your existing credentials.
3. Create or join a chat room and start chatting in real-time!

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.



## Acknowledgements

- [Django](https://www.djangoproject.com/)
- [Django Channels](https://channels.readthedocs.io/)
- [Bootstrap](https://getbootstrap.com/)
- [Redis](https://redis.io/)
```
