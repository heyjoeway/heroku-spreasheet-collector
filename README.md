# heroku-spreadsheet-collector

Need a quick and dirty solution to create an append-only "database" using a spreadsheet? Here it is!

# Usage

Create a new Heroku app and deploy this repo. In the app's settings, add the following config vars:

- `SPREADSHEET_ID`: The ID of the Google Sheets document to append responses to.
- `GOOGLE_CREDENTIALS`: The contents of a JSON file for Google service account credentials.

After configuring, `POST` requests can be sent to `https://your-app.herokuapp.com/submit` with the following form (JSON ONLY):
```json
{
    "values": ["foo", "bar", "lorem", "ipsum", ... ],
    "sheet": "Sheet1"
}
```

Responses will either be:
- `{ "status": "success" }`
- `{ "status": "error" }`

The API has no further functionality. This simplicity is meant to make the code easier to deploy and debug.

# License

MIT