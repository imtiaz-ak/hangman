from tkinter import *
from backend import main
from functools import partial

functions = main()

functions.get_random_word()
functions.create_display_string()

def filling_alphabet(alphabet):
	functions.check_input(alphabet)
	textFrame['text'] = ''.join(functions.display_string)

	

#The Graphical User Interface

root = Tk()



textFrame = Label(root, text=''.join(functions.display_string))
textFrame.pack(side=TOP)
buttonTopFrame = Frame(root)
buttonTopFrame.pack(side=TOP)
buttonSecondFrame = Frame(root)
buttonSecondFrame.pack(side=TOP)
buttonThirdFrame = Frame(root)
buttonThirdFrame.pack(side=TOP)

button_a = Button(buttonTopFrame, text='A', command=partial(filling_alphabet, 'A '))
button_b = Button(buttonTopFrame, text='B', command=partial(filling_alphabet, 'B '))
button_c = Button(buttonTopFrame, text='C', command=partial(filling_alphabet, 'C '))
button_d = Button(buttonTopFrame, text='D', command=partial(filling_alphabet, 'D '))
button_e = Button(buttonTopFrame, text='E', command=partial(filling_alphabet, 'E '))
button_f = Button(buttonTopFrame, text='F', command=partial(filling_alphabet, 'F '))
button_g = Button(buttonTopFrame, text='G', command=partial(filling_alphabet, 'G '))
button_h = Button(buttonTopFrame, text='H', command=partial(filling_alphabet, 'H '))
button_i = Button(buttonTopFrame, text='I', command=partial(filling_alphabet, 'I '))
button_j = Button(buttonSecondFrame, text='J', command=partial(filling_alphabet, 'J '))
button_k = Button(buttonSecondFrame, text='K', command=partial(filling_alphabet, 'K '))
button_l = Button(buttonSecondFrame, text='L', command=partial(filling_alphabet, 'L '))
button_m = Button(buttonSecondFrame, text='M', command=partial(filling_alphabet, 'M '))
button_n = Button(buttonSecondFrame, text='N', command=partial(filling_alphabet, 'N '))
button_o = Button(buttonSecondFrame, text='O', command=partial(filling_alphabet, 'O '))
button_p = Button(buttonSecondFrame, text='P', command=partial(filling_alphabet, 'P '))
button_q = Button(buttonSecondFrame, text='Q', command=partial(filling_alphabet, 'Q '))
button_r = Button(buttonSecondFrame, text='R', command=partial(filling_alphabet, 'R '))
button_s = Button(buttonThirdFrame, text='S', command=partial(filling_alphabet, 'S '))
button_t = Button(buttonThirdFrame, text='T', command=partial(filling_alphabet, 'T '))
button_u = Button(buttonThirdFrame, text='U', command=partial(filling_alphabet, 'U '))
button_v = Button(buttonThirdFrame, text='V', command=partial(filling_alphabet, 'V '))
button_w = Button(buttonThirdFrame, text='W', command=partial(filling_alphabet, 'W '))
button_x = Button(buttonThirdFrame, text='X', command=partial(filling_alphabet, 'X '))
button_y = Button(buttonThirdFrame, text='Y', command=partial(filling_alphabet, 'Y '))
button_z = Button(buttonThirdFrame, text='Z', command=partial(filling_alphabet, 'Z '))



button_a.pack(side=LEFT)
button_b.pack(side=LEFT)
button_c.pack(side=LEFT)
button_d.pack(side=LEFT)
button_e.pack(side=LEFT)
button_f.pack(side=LEFT)
button_g.pack(side=LEFT)
button_h.pack(side=LEFT)
button_i.pack(side=LEFT)
button_j.pack(side=LEFT)
button_k.pack(side=LEFT)
button_l.pack(side=LEFT)
button_m.pack(side=LEFT)
button_n.pack(side=LEFT)
button_o.pack(side=LEFT)
button_p.pack(side=LEFT)
button_q.pack(side=LEFT)
button_r.pack(side=LEFT)
button_s.pack(side=LEFT)
button_t.pack(side=LEFT)
button_u.pack(side=LEFT)
button_v.pack(side=LEFT)
button_w.pack(side=LEFT)
button_x.pack(side=LEFT)
button_y.pack(side=LEFT)
button_z.pack(side=LEFT)

filling_alphabet(' ')

root.mainloop() #Runs the game