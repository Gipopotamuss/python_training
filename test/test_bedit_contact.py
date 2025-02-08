from model.contact import Contact

def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(firstname="aaaaaaa", middlename="sssssss", lastname="dddddd", nickname="ffffff", title="t", company="eeeee", address="g",
                               home="f", mobile="dhhhhhhh", work="iiiiiii", fax="kkkkkkk", email_1="llllll", email_2="nnnnnnn", email_3="yyyyyy",
                               homepage="jjjjjjj"))
    app.session.logout()