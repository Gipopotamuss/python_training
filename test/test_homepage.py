import re
from random import randrange
from model.contact import Contact

#def test_info_on_home_page(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(firstname="test", lastname="test1", address="address", home="homephone",
#                                   mobile="mobile", work="workphone", email_1="email1@mail.ru",
#                                   email_2="email2@mail.ru", email_3="email3@mail.ru"))
#    contacts = app.contact.get_contact_list()
#    index = randrange(len(contacts))
#    contact_from_home_page = app.contact.get_contact_list()[index]
#    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
#    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
#    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)
#    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
#    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
#    assert contact_from_home_page.address == contact_from_edit_page.address


def test_contact_on_homepage(app, db):
    contacts_from_homepage = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contacts_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    index = 0
    for element in contacts_from_homepage:
        assert element.all_phones_from_home_page == merge_phones_like_on_home_page(contacts_from_db[index])
        assert element.all_emails_from_home_page == merge_emails_like_on_home_page(contacts_from_db[index])
        assert element.firstname == contacts_from_db[index].firstname
        assert element.lastname == contacts_from_db[index].lastname
        assert element.address == contacts_from_db[index].address
        index += 1

def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home, contact.mobile, contact.work]))))

def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                                filter(lambda x: x is not None,
                                       [contact.email_1, contact.email_2, contact.email_3])))