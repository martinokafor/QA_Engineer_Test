
class WebElementReader:

    def __init__(self, web_element_file):
        self.web_element_file = web_element_file


    def web_element_reader(self):
        self.store_web_element = []
        with open("./web_element/"+ self.web_element_file, "r+") as self.web_element_file_content:
            for self.web_element in self.web_element_file_content:
                self.store_web_element.append(self.web_element.strip())
        return self.store_web_element

#webelement = WebElementReader("dashboard_web.txt")
#webelement = webelement.web_element_reader()
#print(webelement[0])