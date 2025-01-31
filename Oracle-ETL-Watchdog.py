import oracledb
import requests
import winsound
import tkinter as tk
from tkinter import messagebox

# Use environment variables for sensitive information
user_name = 'DB_USER'
user_password = 'DB_PASSWORD'
url = 'DB_DSN'
webhook_url = 'TEAMS_WEBHOOK_URL'

# Create the message payload
adaptive_card_payload = {
    "type": "message",
    "attachments": [
        {
            "contentType": "application/vnd.microsoft.card.adaptive",
            "content": {
                "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
                "type": "AdaptiveCard",
                "version": "1.4",
                "body": [
                    {
                        "type": "TextBlock",
                        "text": "Check ETL Time!",
                        "weight": "Bolder",
                        "size": "Large"
                    }
                ]
            }
        }
    ]
}

try:
    con = oracledb.connect(user=user_name, password=user_password, dsn=url)
    if not con.is_healthy():
        print("Database connection is not healthy. Exiting.")
        exit()

    cur = con.cursor()
    cur.execute("""
        SELECT
            TO_NUMBER(TO_CHAR(t.INSERT_DATE, 'HH24')) AS INSERT_HOUR,
            TO_NUMBER(TO_CHAR(SYSDATE, 'HH24')) AS SYS_HOUR
        FROM SCHEMA.TABLE t
    """)
    insert_hour, sys_hour = cur.fetchone()

    if insert_hour != sys_hour:
        result = "Check ETL Time!"
        winsound.Beep(900, 1000)
        messagebox.showinfo("Check ETL Time!", result)
        response = requests.post(webhook_url, json=adaptive_card_payload)
    else:
        result = "OK"
        messagebox.showinfo("Check ETL Time!", result)

finally:
    con.close()