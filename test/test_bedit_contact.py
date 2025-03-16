from model.contact import Contact
import random

def test_edit_contact_name(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = db.get_contact_list()
    contact_choice = random.choice(old_contacts)
    contact = Contact(firstname="New firstname")
    app.contact.edit_contact_by_id(contact_choice.id,contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts[old_contacts.index(contact_choice)] = contact
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),key=Contact.id_or_max)

#def test_edit_contact_lastname(app):
#    old_contacts = app.contact.get_contact_list()
#    if app.contact.count() == 0:
#        app.contact.create(Contact(firstname="test"))
#    app.contact.edit_first_contact(Contact(lastname="New lastname"))
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) == len(new_contacts)