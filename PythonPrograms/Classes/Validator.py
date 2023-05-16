import datetime


def validate_input(text):
    if text not in ('y', 'n', 'stop'):
        raise SystemExit("Ihre Eingabe war ungültig. Programm wird abgebrochen")


def validate_sql_input(text):
    if text not in ('1', '2', '3', '4'):
        raise SystemExit("Ihre Eingabe war ungültig. Programm wird abgebrochen")


def validate_date(date_text):
    try:
        datetime.date.fromisoformat(date_text)
    except ValueError:
        raise SystemExit("Es wurde ein ungültiges Datum angegeben")


def validate_start_and_end_date(start_date, end_date):
    if start_date > end_date:
        raise SystemExit("Das End-Datum muss jünger sein als das Start-Datum")
