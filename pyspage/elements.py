

class Base:
    @property
    def html(self):
        return self.template.format(innerHtml=self.innerHtml, class_=self.class_, id_='{id_}')

class Box(Base):
    template = '''<div id="{id_}" class="{class_}">{innerHtml}</div>'''

    def __init__(self, class_ = 'container'):
        self.class_ = class_
        

class Button(Base):
    template = '''<button class="{class_}">{innerHtml}</button>'''

    def __init__(self, innerHtml = 'Click Me', class_ = 'btn btn-primary'):
        self.innerHtml = innerHtml
        self.class_ = class_

