from model.contact import Contact
import random
from model.group import Group


def test_add_user_to_group(app, orm, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    groups = orm.get_group_list()
    group_id = random.choice(groups).id
    if len(orm.get_contacts_not_in_group(Group(id=group_id))) == 0:
        app.contact.create(Contact(firstname="firstname", lastname="lastname"))
    contacts = orm.get_contacts_not_in_group(Group(id=group_id))
    contact = random.choice(contacts)
    app.contact.add_contact_to_group(contact.id, group_id)
    new_contacts = orm.get_contacts_in_group(Group(id=group_id))
    assert contact in new_contacts