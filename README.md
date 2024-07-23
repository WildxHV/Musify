# Spotify-Clone MUSIFY

A Django-based web App

## Installation

1. **Clone the Repo**
    ```sh
    git clone https://github.con/WildxHV/
    cd MUSIFY
    ```

2. **Create Virtual virtual env and activate it**
    ``` sh
    python -m venv venv
    source venv/bin/activate # on WIndows use `venv\Scripts\activate`
    ```

3. **Install dependencies**
    ```sh
    pip install -r requirements.txt
    ```

4. **Run database migrations**
   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```
5. **Create Super User**
    ```sh
    python manage.py createsuperuser
    ```
6. **Start server**
   ```sh
   python manage.py runserver
   ```
7. **Access the app**
   go to `http://127.0.0.1:8000/`


## Usage

- **Register** `http://127.0.0.1:8000/register/`
- **Login** `http://127.0.0.1:8000/login/`
- **Playlists** `http://127.0.0.1:8000/playlists/`
- **Profile** `http://127.0.0.1:8000/profile/`
- **Search** `http://127.0.0.1:8000/search/`