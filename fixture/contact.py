from model.contact import Contact
import re

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_homepage(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_xpath("//input[@value='Send e-Mail']")) > 0):
            wd.find_element_by_link_text("home").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def init(self, contact):
        wd = self.app.wd
        # fill contact form
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email_1)
        self.change_field_value("email2", contact.email_2)
        self.change_field_value("email3", contact.email_3)
        self.change_field_value("homepage", contact.homepage)
        # birthday
        wd.find_element_by_xpath("//option[@value='25']").click()
        wd.find_element_by_name("bmonth").click()
        wd.find_element_by_xpath("//option[@value='November']").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys("dfg")
        # anniversary
        wd.find_element_by_name("aday").click()
        wd.find_element_by_xpath("//div[@id='content']/form/select[3]/option[27]").click()
        wd.find_element_by_name("amonth").click()
        wd.find_element_by_xpath("//div[@id='content']/form/select[4]/option[12]").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys("dfgd")

    def create(self, contact):
        wd = self.app.wd
        self.open_homepage()
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        self.init(contact)
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[20]").click()
        self.return_to_homepage()
        self.contact_cache = None

    def select_edit_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()

    def select_edit_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_xpath('//a[contains(@href, "edit.php?id=%s")]' % id).click()


    def edit_first_contact(self):
        self.edit_contact_by_index(0)

    def edit_contact_by_index(self,index, new_contact_data):
        wd = self.app.wd
        self.open_homepage()
        # edit contact
        self.select_edit_contact_by_index(index)
        self.init(new_contact_data)
        # submit edit
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def select_contact_by_index(self,index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_contact_by_id(self,id):
        wd = self.app.wd
        wd.find_element_by_id(id).click()

    def delete_contact_by_index(self,index):
        wd = self.app.wd
        self.open_homepage()
        # select first contact
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        self.contact_cache = None

    def return_to_homepage(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def count(self):
        wd = self.app.wd
        self.open_homepage()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_homepage()
            self.contact_cache = []
            index = 0
            for element in wd.find_elements_by_css_selector("td.center"):
                if element.find_elements_by_name("selected[]") and element.find_elements_by_name("selected[]")[
                    0].is_displayed():
                    firstname = wd.find_element_by_xpath(f"//table[@id='maintable']/tbody/tr[{index + 2}]/td[3]").text
                    lastname = wd.find_element_by_xpath(f"//table[@id='maintable']/tbody/tr[{index + 2}]/td[2]").text
                    id = element.find_element_by_name("selected[]").get_attribute("value")
                    all_phones = wd.find_element_by_xpath(
                        f"//table[@id='maintable']/tbody/tr[{index + 2}]/td[6]").text
                    all_emails = wd.find_element_by_xpath(
                        f"//table[@id='maintable']/tbody/tr[{index + 2}]/td[5]").text
                    address = wd.find_element_by_xpath(
                        f"//table[@id='maintable']/tbody/tr[{index + 2}]/td[4]").text
                    self.contact_cache.append(Contact(firstname=firstname, lastname=lastname,
                                                      id=id, all_phones_from_home_page=all_phones,
                                                      all_emails_from_home_page=all_emails, address=address))
                    index += 1
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self,index):
        wd = self.app.wd
        self.open_homepage()
        self.select_edit_contact_by_index(index)

    def open_contact_to_view_by_index(self,index):
        wd = self.app.wd
        self.open_homepage()
        wd.find_elements_by_xpath("//img[@alt='Details']")[index].click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        home = wd.find_element_by_name("home").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        work = wd.find_element_by_name("work").get_attribute("value")
        email_1 = wd.find_element_by_name("email").get_attribute("value")
        email_2 = wd.find_element_by_name("email2").get_attribute("value")
        email_3 = wd.find_element_by_name("email3").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id,
                       home=home, mobile=mobile, work=work,
                       email_1=email_1, email_2=email_2, email_3=email_3, address=address)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_to_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home = re.search("H: (.*)", text).group(1)
        mobile = re.search("M: (.*)", text).group(1)
        work = re.search("W: (.*)", text).group(1)
        return Contact(home=home, mobile=mobile, work=work)

    def delete_contact_by_id(self,id):
        wd = self.app.wd
        self.open_homepage()
        # select first contact
        self.select_contact_by_id(id)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        self.contact_cache = None

    def edit_contact_by_id(self, id, new_contact_data):
        wd = self.app.wd
        self.open_homepage()
        # edit contact
        self.select_edit_contact_by_id(id)
        self.init(new_contact_data)
        # submit edit
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.contact_cache = None

    def add_contact_to_group(self, id, group_id):
         wd = self.app.wd
         self.open_homepage()
         wd.find_element_by_xpath('//input[@id="%s"]' % id).click()
         wd.find_element_by_xpath('//select[@name = "to_group"]').click()
         wd.find_elements_by_css_selector('select[name="to_group"] > option[value="%s"]' % group_id)[0].click()
         wd.find_element_by_xpath('//input[@name="add"]').click()
         self.contact_cache = None

    def del_contact_from_group(self, id, group_id):
         wd = self.app.wd
         self.open_homepage()
         wd.find_element_by_xpath('//select[@name="group"]').click()
         wd.find_element_by_xpath('//option[@value="%s"]' % group_id).click()
         wd.find_element_by_xpath('//input[@id="%s"]' % id).click()
         wd.find_element_by_xpath('//input[@name="remove"]').click()
         self.contact_cache = None