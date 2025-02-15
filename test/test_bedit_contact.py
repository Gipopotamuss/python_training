from model.contact import Contact

def test_edit_contact_firstname(app):
    app.contact.edit_first_contact(Contact(firstname="New firstname"))

def test_edit_contact_lastname(app):
    app.contact.edit_first_contact(Contact(lastname="New lastname"))