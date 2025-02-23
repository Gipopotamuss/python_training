# -*- coding: utf-8 -*-
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(Contact(firstname="dfgdfgdf", middlename="dfgdfg", lastname="dfgdfg", nickname="dfgdfgdfg", title="dfgdfgdfg", company="dfgdgdfg", address="dfgdfgdfgdfg",
                               home="dfgdgdf", mobile="dfgdgdfg", work="dfgdgdfg", fax="dfgdfgdfg", email_1="dfgdgdfg", email_2="dfgdfgdfg", email_3="dfgdgdfgd",
                               homepage="dfgdfgdfgdfg"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)


def is_element_present(self, how, what):
    try: self.wd.find_element(by=how, value=what)
    except NoSuchElementException as e: return False
    return True
    
def is_alert_present(self):
    try: self.wd.switch_to_alert()
    except NoAlertPresentException as e: return False
    return True

