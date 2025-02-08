# -*- coding: utf-8 -*-
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import pytest
from model.group import Group
from fixture.application import Application


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.session.login(username="admin", password= "secret")
    app.create_group(Group(name="hgjhgjghjg", header="ghjghjghjghj", footer="ghjghjgjghj"))
    app.session.logout()

def test_add_empty_group(app):
    app.session.login(username="admin", password= "secret")
    app.create_group(Group(name="", header="", footer=""))
    app.session.logout()

def is_element_present(self, how, what):
    try: self.wd.find_element(by=how, value=what)
    except NoSuchElementException as e: return False
    return True

def is_alert_present(self):
    try: self.wd.switch_to_alert()
    except NoAlertPresentException as e: return False
    return True
