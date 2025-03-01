# -*- coding: utf-8 -*-
import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from model.contact import Contact
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits +  " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(firstname="", middlename="", lastname="", nickname="",
                    title="", company="", address="", home="", mobile="",
                    work="", fax="", email_1="", email_2="", email_3="",homepage="")] + [
    Contact(firstname=random_string("firstname", 10),
            middlename=random_string("middlename", 10),
            lastname=random_string("lastname", 10),
            nickname=random_string("nickname", 10),
            title=random_string("title", 10),
            company=random_string("company", 10),
            address=random_string("address", 10),
            home=random_string("home", 10),
            mobile=random_string("mobile", 10),
            work=random_string("work", 10),
            fax=random_string("fax", 10),
            email_1=random_string("email_1", 10),
            email_2=random_string("email_2", 10),
            email_3=random_string("email_3", 10),
            homepage=random_string("homepage", 10))
    for i in range(2)
]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def is_element_present(self, how, what):
    try: self.wd.find_element(by=how, value=what)
    except NoSuchElementException as e: return False
    return True
    
def is_alert_present(self):
    try: self.wd.switch_to_alert()
    except NoAlertPresentException as e: return False
    return True

