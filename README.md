# PredCo

# PredCo - Predictive Maintenance Web Application

PredCo is a web application for monitoring IOT based dashboards, built with Django. The purpose of this application is to help companies to minimize downtime and maintenance costs by predicting equipment failures before they occur.

## Features

- User authentication and authorization
- Dashboard for sensor overview
- Real-time monitoring of equipment status and data
- Visualization of sensor data in graphs and charts
- Email alerts for equipment failures and maintenance reminders

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:
   
   `git clone https://github.com/Ashsenior/PredCo.git`
   `cd PredCo`
   

2. Install Python packages:
   
   `pip install -r requirements.txt`
   

3. Apply database migrations:
   
   `python manage.py migrate`
   
### Admin Account Creation

1. `python manage.py createsuperuser`


### Usage

1. Start the Django development server:
   
   `python manage.py runserver`
   

2. Open the web application in a browser:
   
   http://localhost:8000/

    #### Admin Panel

    Admin panel can be accessed through http://localhost:8000/admin
   

## Contributing

Contributions to PredCo are welcome and encouraged! To contribute, please follow these steps:

1. Fork the repository
2. Create a new branch: `git checkout -b new-feature`
3. Make your changes and commit them: `git commit -m 'Add new feature'`
4. Push to the branch: `git push origin new-feature`
5. Submit a pull request

## License

PredCo is licensed under the MIT license. See the LICENSE file for more details.
