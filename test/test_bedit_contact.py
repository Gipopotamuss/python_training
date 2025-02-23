from model.contact import Contact

def test_edit_contact_firstname(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="New firstname")
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    app.contact.edit_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

#def test_edit_contact_lastname(app):
#    old_contacts = app.contact.get_contact_list()
#    if app.contact.count() == 0:
#        app.contact.create(Contact(firstname="test"))
#    app.contact.edit_first_contact(Contact(lastname="New lastname"))
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) == len(new_contacts)