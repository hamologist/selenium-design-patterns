from selenium_design_patterns.page_property import PageProperty


class TextInputProperty(PageProperty):

    @PageProperty.text.setter
    def text(self, text: str):
        self.clear()
        self.element.send_keys(text)

    def clear(self):
        self.element.clear()
