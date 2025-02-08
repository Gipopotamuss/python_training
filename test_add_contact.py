# -*- coding: utf-8 -*-
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import pytest
from contact import Contact
from application_contact import Application_contact

@pytest.fixture()
def app(request):
    fixture = Application_contact()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname= "dfgdfgdf",middlename= "dfgdfg", lastname= "dfgdfg", nickname="dfgdfgdfg", title="dfgdfgdfg", company="dfgdgdfg", address="dfgdfgdfgdfg",
                            home="dfgdgdf", mobile="dfgdgdfg", work="dfgdgdfg", fax="dfgdfgdfg", email_1="dfgdgdfg", email_2="dfgdfgdfg", email_3="dfgdgdfgd",
                            homepage="dfgdfgdfgdfg"))
    app.logout()


def is_element_present(self, how, what):
    try: self.wd.find_element(by=how, value=what)
    except NoSuchElementException as e: return False
    return True
    
def is_alert_present(self):
    try: self.wd.switch_to_alert()
    except NoAlertPresentException as e: return False
    return True

