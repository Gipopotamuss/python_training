# -*- coding: utf-8 -*-
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from model.group import Group


def test_add_group(app):
    app.session.login(username="admin", password= "secret")
    app.group.create(Group(name="hgjhgjghjg", header="ghjghjghjghj", footer="ghjghjgjghj"))
    app.session.logout()

def test_add_empty_group(app):
    app.session.login(username="admin", password= "secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()

def is_element_present(self, how, what):
    try: self.wd.find_element(by=how, value=what)
    except NoSuchElementException as e: return False
    return True

def is_alert_present(self):
    try: self.wd.switch_to_alert()
    except NoAlertPresentException as e: return False
    return True
