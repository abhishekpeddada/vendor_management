# project_vendor_management

Develop a Vendor Management System using Django and Django REST Framework that can handle vendor profiles, track purchase orders, and calculate vendor performance


## Prerequisites

- Python (version 3.10.12)
- Django (version 4.2.7)

## Installation

# 1. Clone the repository:
   bash:  
   git clone https://github.com/abhishekpeddada/vendor_management.git  
   cd vendor_management  

# 2.Create a virtual environment:
python -m venv venv  
source venv/bin/activate  # For Linux/Mac  
venv\Scripts\activate     # For Windows  

# 3.Install dependencies:
pip install -r requirements.txt  

# 4.Database setup:
python manage.py makemigrations  
python manage.py migrate  

## Usage
# 1.Create Django Admin

python manage.py createsuperuser

# 2.Start the server:
python manage.py runserver  
