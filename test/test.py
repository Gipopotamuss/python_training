import random
from model.contact import Contact

def test(app, db, check_ui):
    return app.contact.select_contact_by_id(134)
