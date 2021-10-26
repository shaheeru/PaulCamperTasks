
class VisitPage():
    def __init__(self, drv):
        self.drv = drv
        drv.maximize_window()


    def VisitTheURL(self):
        self.drv.implicitly_wait(30)

    def VerifyRegisterTextLink(self):
        self.drv.find_element_by_id("register")
