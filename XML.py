import lxml.etree as ET

tree = ET.parse(r'.XML/XML.xml')


def getData(uid):
    root = tree.getroot()
    for user in root.findall('user'):
        if user.find('uid').text == uid:
            return user

def saveUser(User):
    elementUsers = ET.SubElement("root", User)
