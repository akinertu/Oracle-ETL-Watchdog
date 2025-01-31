# Oracle-ETL-Watchdog

Oracle-ETL-Watchdog is a Python-based tool designed to ensure the timely execution of ETL processes. It connects to an Oracle database to check the most recent data insertion time against the system clock. If the data has not been updated within the current hour, the tool triggers alerts. It utilizes a combination of local notifications(popup message and beep sound) and Microsoft Teams messages to promptly inform stakeholders of potential delays or disruptions in the ETL workflow. This project is ideal for data engineers and administrators looking to maintain high data quality and operational consistency in real-time data environments.

## Features

- **Real-Time Monitoring:** Checks the latest data insertion time against the system clock hourly.
- **Alert System:** Generates alerts if the ETL process does not update the data within the current hour.
- **Notification Mechanisms:** Uses local popups and Microsoft Teams messages to notify the relevant stakeholders of any delays.
- **Oracle Database Integration:** Seamlessly connects to Oracle databases to fetch insertion times.

## Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.x
- oracledb Python package
- requests Python package

## Setup
To run ETL-Monitor-Alert, you need to set up the following environment variables:

- DB_USER: Your database username
- DB_PASSWORD: Your database password
- DB_DSN: Your Oracle database DSN (Data Source Name)
- TEAMS_WEBHOOK_URL: The Microsoft Teams webhook URL for sending alerts

## Contact
Ertuğrul Akın - ertugrulakin88@gmail.com
Project Link: [https://github.com/yourusername/ETL-Monitor-Alert](https://github.com/akinertu/Oracle-ETL-Watchdog)
