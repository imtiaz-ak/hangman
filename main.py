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



textFrame = Label(root, text=''.join(functions.display_string), font=("Courier", 34))
textFrame.pack(side=TOP)
buttonTopFrame = Frame(root)
buttonTopFrame.pack(side=TOP)
buttonSecondFrame = Frame(root)
buttonSecondFrame.pack(side=TOP)
buttonThirdFrame = Frame(root)
buttonThirdFrame.pack(side=TOP)


button_a = Button(buttonTopFrame, text='A', command=partial(filling_alphabet, 'A '), height=1, width=4, bg='black', fg='white',font="Helvetica 18 bold")
button_b = Button(buttonTopFrame, text='B', command=partial(filling_alphabet, 'B '), height=1, width=4, bg='black', fg='white',font="Helvetica 18 bold")
button_c = Button(buttonTopFrame, text='C', command=partial(filling_alphabet, 'C '), height=1, width=4, bg='black', fg='white',font="Helvetica 18 bold")
button_d = Button(buttonTopFrame, text='D', command=partial(filling_alphabet, 'D '), height=1, width=4, bg='black', fg='white',font="Helvetica 18 bold")
button_e = Button(buttonTopFrame, text='E', command=partial(filling_alphabet, 'E '), height=1, width=4, bg='black', fg='white',font="Helvetica 18 bold")
button_f = Button(buttonTopFrame, text='F', command=partial(filling_alphabet, 'F '), height=1, width=4, bg='black', fg='white',font="Helvetica 18 bold")
button_g = Button(buttonTopFrame, text='G', command=partial(filling_alphabet, 'G '), height=1, width=4, bg='black', fg='white',font="Helvetica 18 bold")
button_h = Button(buttonTopFrame, text='H', command=partial(filling_alphabet, 'H '), height=1, width=4, bg='black', fg='white',font="Helvetica 18 bold")
button_i = Button(buttonTopFrame, text='I', command=partial(filling_alphabet, 'I '), height=1, width=4, bg='black', fg='white',font="Helvetica 18 bold")
button_j = Button(buttonSecondFrame, text='J', command=partial(filling_alphabet, 'J '), height=1, width=4, bg='black', fg='white',font="Helvetica 18 bold")
button_k = Button(buttonSecondFrame, text='K', command=partial(filling_alphabet, 'K '), height=1, width=4, bg='black', fg='white',font="Helvetica 18 bold")
button_l = Button(buttonSecondFrame, text='L', command=partial(filling_alphabet, 'L '), height=1, width=4, bg='black', fg='white',font="Helvetica 18 bold")
button_m = Button(buttonSecondFrame, text='M', command=partial(filling_alphabet, 'M '), height=1, width=4, bg='black', fg='white',font="Helvetica 18 bold")
button_n = Button(buttonSecondFrame, text='N', command=partial(filling_alphabet, 'N '), height=1, width=4, bg='black', fg='white',font="Helvetica 18 bold")
button_o = Button(buttonSecondFrame, text='O', command=partial(filling_alphabet, 'O '), height=1, width=4, bg='black', fg='white',font="Helvetica 18 bold")
button_p = Button(buttonSecondFrame, text='P', command=partial(filling_alphabet, 'P '), height=1, width=4, bg='black', fg='white',font="Helvetica 18 bold")
button_q = Button(buttonSecondFrame, text='Q', command=partial(filling_alphabet, 'Q '), height=1, width=4, bg='black', fg='white',font="Helvetica 18 bold")
button_r = Button(buttonSecondFrame, text='R', command=partial(filling_alphabet, 'R '), height=1, width=4, bg='black', fg='white',font="Helvetica 18 bold")
button_s = Button(buttonThirdFrame, text='S', command=partial(filling_alphabet, 'S '), height=1, width=4, bg='black', fg='white',font="Helvetica 18 bold")
button_t = Button(buttonThirdFrame, text='T', command=partial(filling_alphabet, 'T '), height=1, width=4, bg='black', fg='white',font="Helvetica 18 bold")
button_u = Button(buttonThirdFrame, text='U', command=partial(filling_alphabet, 'U '), height=1, width=4, bg='black', fg='white',font="Helvetica 18 bold")
button_v = Button(buttonThirdFrame, text='V', command=partial(filling_alphabet, 'V '), height=1, width=4, bg='black', fg='white',font="Helvetica 18 bold")
button_w = Button(buttonThirdFrame, text='W', command=partial(filling_alphabet, 'W '), height=1, width=4, bg='black', fg='white',font="Helvetica 18 bold")
button_x = Button(buttonThirdFrame, text='X', command=partial(filling_alphabet, 'X '), height=1, width=4, bg='black', fg='white',font="Helvetica 18 bold")
button_y = Button(buttonThirdFrame, text='Y', command=partial(filling_alphabet, 'Y '), height=1, width=4, bg='black', fg='white',font="Helvetica 18 bold")
button_z = Button(buttonThirdFrame, text='Z', command=partial(filling_alphabet, 'Z '), height=1, width=4, bg='black', fg='white',font="Helvetica 18 bold")



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