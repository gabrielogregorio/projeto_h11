from tkinter import Frame
from tkinter import Label
from tkinter import Label
from tkinter import NSEW
from tkinter import Tk
from time import sleep


class Splash():
    def __init__(self, design):
        self.frame_splash = None
        self.fr_splash = None
        self.l1_splash = None
        self.l2_splash = None
        self.tela_splash = Tk()
        self.tela_splash.withdraw()
        self.tela_splash.overrideredirect(1)
        self.tela_splash.rowconfigure(1, weight=1)
        self.tela_splash.grid_columnconfigure(1, weight=1)
        self.design = design

    def splash_inicio(self):
        self.frame_splash = Frame(self.tela_splash)

        self.frame_splash.configure(background=self.design.dic["cor_intro"]["background"])
        self.frame_splash.rowconfigure(1, weight=1)
        self.frame_splash.grid_columnconfigure(0, weight=1)

        self.fr_splash = Frame(self.frame_splash)
        self.l1_splash = Label(self.frame_splash, self.design.dic["cor_intro"])
        self.l2_splash = Label(self.frame_splash, self.design.dic["cor_intro"])

        self.fr_splash.configure(background=self.design.dic["cor_intro"]["background"])
        self.l1_splash.configure(text=" COMBRATEC ", font=("Lucida Sans", 90), bd=80)
        self.l2_splash.configure(text="Safira IDE beta 0.3", font=("Lucida Sans", 12))

        self.frame_splash.grid(row=1, column=1, sticky=NSEW)
        self.fr_splash.grid(row=0, column=1, sticky=NSEW)
        self.l1_splash.grid(row=1, column=1, sticky=NSEW)
        self.l2_splash.grid(row=2, column=1, sticky=NSEW)
        self.frame_splash.update()

        self.tela_splash.update()
        self.tela_splash.withdraw()

        j_width = self.tela_splash.winfo_reqwidth()
        j_height = self.tela_splash.winfo_reqheight()

        t_width = self.tela_splash.winfo_screenwidth()
        t_heigth = self.tela_splash.winfo_screenheight()

        self.tela_splash.geometry("+{}+{}".format(int(t_width/2)-int(j_width/2), int(t_heigth/2)-int(j_height/2)))
        self.tela_splash.deiconify()
        self.tela_splash.update()

    def splash_fim(self):
        self.fr_splash.destroy()
        self.l1_splash.destroy()
        self.l2_splash.destroy()

        self.frame_splash.destroy()
        self.tela_splash.destroy()

if __name__ == '__main__':
    from design import Design

    design = Design()
    design.update_design_dic()

    splash = Splash(design)
    splash.splash_inicio()
    sleep(5)
    splash.splash_fim()