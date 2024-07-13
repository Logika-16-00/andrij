class Title():
    def __init__(self,name_text,x_num,y_num,opacity_text= True):
        self.name = name_text
        self.x = x_num
        self.y = y_num
        self.opacity = opacity_text

    def hide(self):
        self.opacity_text = False
    def show(self):
        self.opacity_text = True
    def print_info(self):
        print("Кнопка", self.name,"\n Розташування", self.x,self.y, "\nВидиміть", self.opacity_text)

btn1 = Title("dtrfy",43,75,False)
btn1.show()
btn1.print_info()
        