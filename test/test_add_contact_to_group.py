from model.contact import Contact
import random
from model.group import Group


def test_add_user_to_group(app, orm, db):
    if len(db.get_contact_list()) == 0:
        app.user.create(Contact(firstname="firstname", lastname="lastname"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    all_contacts = orm.get_contact_list()
    contact = random.choice(all_contacts)
    groups = orm.get_group_list()
    group_id = random.choice(groups).id
    app.contact.add_contact_to_group(contact.id, group_id)
    new_users = orm.get_contacts_in_group(Group(id=group_id))
    assert contact in new_users