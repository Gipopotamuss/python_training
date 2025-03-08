# -*- coding: utf-8 -*-
import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from model.contact import Contact
from data.contacts import constant as testdata

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

