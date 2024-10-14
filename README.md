# Gallery

Gallery is a Django web application that allows users to upload, view, and delete photos. It features user authentication to ensure that only registered users can manage their own images.

## Features

- User authentication (registration, login, logout)
- Upload photos
- View uploaded photos
- Delete photos
- Drag and Drop facility 
- User-friendly interface

## Technologies Used

- Django
- Python
- SQLite (or any other database of your choice)
- HTML/CSS
- Bootstrap (optional for styling)


## Installation

To run this application locally, follow these steps:

1. **Clone the repository:**

    ```bash
    git clone https://github.com/im-yash21/Gallery-web.git
    cd galleryapp
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use: env\Scripts\activate
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply database migrations:**

    ```bash
    python manage.py migrate
    ```

5. **Create a superuser (optional, for admin access):**

    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

7. **Open your browser and navigate to:**

    ```
    http://127.0.0.1:8000/

## Configuration

The application uses default Django settings. For production use, consider configuring additional settings such as `ALLOWED_HOSTS`, `DEBUG`, and database settings in `settings.py`.

## Contributing

Contributions are welcome! If you would like to contribute, please fork the repository and submit a pull request with your changes.

## Contact

For any questions or feedback, please contact [yashjangid0021@gmail.com](mailto:yashjangid0021@gmail.com).

---

Thank you for checking out this project. Happy task managing!