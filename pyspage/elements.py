

class Base:
    def __init__(self):
        self.innerHtml = '{innerHtml}'
        self.id_ = '{id_}'
        self.class_ = '{class_}'
    @property
    def html(self):
        return self.template.format(innerHtml=self.innerHtml, class_=self.class_, id_=self.id_)

class Box(Base):
    template = '''
    <div id="{id_}" class="{class_}">
        {innerHtml}
    </div>
    '''
    def __init__(self, class_ = 'container'):
        super().__init__()
        self.class_ = class_
        

class Button(Base):
    template = '''
    <button id="{id_}" class="{class_}">
        {innerHtml}
    </button>
    '''
    def __init__(self, innerHtml = 'Click Me', class_ = 'btn btn-primary'):
        super().__init__()
        self.innerHtml = innerHtml
        self.class_ = class_




class Page:
    template = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{page_title}</title>
  <link rel="stylesheet" href="{css_url}" />
  <script defer src="{js_url}"></script>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" crossorigin="anonymous">
</head>
<body>
  {layout}
  <py-script id="pyspage">
    {script}
  </py-script>
</body>
</html>
'''
    def __init__(self,
        page_title = 'pyspage',
        css_url = 'https://pyscript.net/latest/pyscript.css',
        js_url = 'https://pyscript.net/latest/pyscript.js',
        layout = '',
        script = '',
    ):
        self.page_title = page_title
        self.css_url = css_url
        self.js_url = js_url
        self.layout = layout
        self.script = script
    
    @property
    def html(self):
        return self.template.format(
            page_title = self.page_title,
            css_url = self.css_url,
            js_url = self.js_url,
            layout = self.layout,
            script = self.script,
        )