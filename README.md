# MEDFI Emergency Response Backend

The MEDFI Emergency Response Backend is the server-side component of the MEDFI Emergency Response Platform. It manages emergency incidents, user authentication, location services, and other core functionalities.

## Getting Started

### Prerequisites

Make sure you have the following installed:

- [Python](https://www.python.org/downloads/)
- [Django](https://www.djangoproject.com/)

# Demo
### Upcoming patient list
<img width="1710" alt="Screenshot 2025-01-09 at 7 09 20 PM" src="https://github.com/user-attachments/assets/81924880-cf23-47f1-9892-e566c95ac4eb" />


### Location Routing to locations
https://github.com/user-attachments/assets/3353206f-a931-451d-aad4-185e0f8b58f6


### Setting Up the Backend

1. Clone the repository:

    ```bash
    https://github.com/shashaaankkkkk/Medfi-Backend.git
    cd Medfi-Backend
    ```

2. Set up the virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Linux/Mac
    venv\Scripts\activate     # On Windows
    ```

3. Install Django and other dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run database migrations:

    ```bash
    python manage.py migrate
    ```

## Project Structure

- `medfi_backend/`: Django backend code.

## Running the Application

1. Navigate to the `medfi_backend` directory:

    ```bash
    cd medfi_backend
    ```

2. Activate the virtual environment:

    ```bash
    source venv/bin/activate  # On Linux/Mac
    venv\Scripts\activate     # On Windows
    ```

3. Run the development server:

    ```bash
    python manage.py runserver
    ```

4. Access the Django admin interface at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Contributing

If you would like to contribute to the backend, please follow the [contributing guidelines](CONTRIBUTING.md).

## License

This backend is licensed under the [MIT License](LICENSE).
