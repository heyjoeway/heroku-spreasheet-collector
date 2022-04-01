import os
import json
from googleapiclient.discovery import build
from google.oauth2 import service_account

SPREADSHEET_ID = None
if "SPREADSHEET_ID" in os.environ:
    SPREADSHEET_ID = os.environ["SPREADSHEET_ID"]
else:
    with open("spreadsheet_id.txt") as f:
        SPREADSHEET_ID = f.readline()

credentialsRaw = None
if "GOOGLE_CREDENTIALS" in os.environ:
    credentialsRaw = json.loads(os.environ["GOOGLE_CREDENTIALS"])
else:
    with open("google_credentials.json") as f:
        credentialsRaw = json.load(f)

service = build(
    'sheets', 'v4',
    credentials=service_account.Credentials.from_service_account_info(credentialsRaw)
)

# =============================================================================

from flask import Flask, request
app = Flask(__name__)

@app.route("/submit", methods=["POST"])
def submit():
    request.get_json(force=True)

    if "coffee" in request.json:
        return "I'm a teapot", 418

    try:
        sheetRequest = service.spreadsheets().values().append(
            spreadsheetId=SPREADSHEET_ID,
            range=f"{request.json['sheet']}!A:A",
            valueInputOption="RAW",
            body={
                "values": [ request.json["values"] ]
            }
        )
        sheetRequest.execute()
        return { "status": "success" }, 200
    except:
        return { "status": "error" }, 400
        pass