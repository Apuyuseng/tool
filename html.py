import uuid


class html(object):
    def __init__(self):
        self.cont = ""
        self.list = {}
        self.fkid = ''
        self.fknexid = ''

    def att(self, **kwargs):
        value = '<' + kwargs["tag"] + " "
        xclass = kwargs.get("xclass", None)
        if xclass is not None:
            value += 'class="%s" ' % xclass

        style = kwargs.get("style", None)
        if style is not None:
            value += 'style="%s"' % style

        value += ">"

        formatKey = str(uuid.uuid1()).replace("-", '')
        text = kwargs.get("text", "{%s}" % formatKey)
        value += text + "</%s>" % kwargs["tag"]
        if text == "{%s}" % formatKey:
            self.fkid = formatKey
            self.list[formatKey] = value

        formatKeyx = str(uuid.uuid1()).replace("-", '')
        nextx = kwargs.get('next', False)
        self.fknexid = ""
        if nextx:
            self.fknexid = formatKeyx
            value += "{%s}" % formatKeyx

        join = kwargs.get("join", None)
        if join is None:
            self.cont += value
        else:
            paras = {join: value}
            print(paras)
            self.cont = self.cont.format(**paras)
        return self
