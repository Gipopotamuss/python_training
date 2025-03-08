from model.contact import Contact
import random
import string

constant = [
    Contact(firstname="firstname1", middlename="middlename1", lastname="lastname1",
            nickname="nickname1", title="title1", company="company1", address="address1",
            home="home1", mobile="mobile1", work="work1", fax="fax1", email_1="email_11",
            email_2="email_21", email_3="email_31",homepage="homepage1"),
    Contact(firstname="firstname2", middlename="middlename2", lastname="lastname2",
            nickname="nickname2", title="title2", company="company2", address="address2",
            home="home2", mobile="mobile2", work="work2", fax="fax2", email_1="email_12",
            email_2="email_22", email_3="email_32",homepage="homepage2")
]

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