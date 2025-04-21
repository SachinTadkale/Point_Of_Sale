# Point of Sale System

A modern Point of Sale (POS) system built with Django, featuring inventory management, sales tracking, and user authentication.

## Features

- **User Authentication**: Secure login and registration system
- **Product Management**: Add, edit, and delete products with image support
- **Inventory Tracking**: Real-time stock management
- **Sales Processing**: Create and manage sales transactions
- **Responsive Design**: Works on desktop and mobile devices

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Virtual environment (recommended)

## Installation

1. Clone the repository:
```bash
git clone <your-repository-url>
cd Point_Of_Sale
```

2. Create and activate a virtual environment:
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up the database:
```bash
python manage.py makemigrations authentication
python manage.py makemigrations products
python manage.py makemigrations sales
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

## Running the Application

1. Start the development server:
```bash
python manage.py runserver
```

2. Access the application:
- Open your web browser and navigate to `http://127.0.0.1:8000`
- Admin interface is available at `http://127.0.0.1:8000/admin`

## Project Structure

```
Point_Of_Sale/
├── authentication/     # User authentication app
├── products/          # Product management app
├── sales/            # Sales processing app
├── static/           # Static files (CSS, JS, images)
├── templates/        # HTML templates
└── manage.py         # Django management script
```

## Usage

1. **Login/Register**:
   - Use the registration page to create a new account
   - Login with your credentials

2. **Managing Products**:
   - Add new products with images and details
   - Update product information and stock levels
   - Remove products from inventory

3. **Processing Sales**:
   - Create new sales transactions
   - Add products to cart
   - Complete transactions

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details 