from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter import colorchooser

# before open the file set variable for open the file
global open_status_name
open_status_name=FALSE

global selected
selected=FALSE

root=Tk()
root.title('text editor')
root.geometry('400x400')

# create a new file fiction
def new_file():
      # delete pervious file
      my_text.delete(1.0,END)
      # update the status bar
      root.title('New File Text Pad....!')
      status_bar.config(text='New File        ')
      
      # if file name doesn't exist then create new file
      global open_status_name
      open_status_name=FALSE

# create a open file
def open_file():
      # delete a previous file/text
      my_text.delete(1.0,END)
      # grab file name
      text_file=filedialog.askopenfilename(initialdir='pycache',title='Open File',filetypes=(('Text File','*.text'),('All Files', '*.*')))
      
      # check to see if there is file name
      if text_file:
            # make file name gobal so we can access it later
            global open_status_name
            open_status_name=text_file
      
      # update a status bar
      name=text_file
      status_bar.config(text=f'{name}        ')
      name=name.replace('storage',' ')
      root.title(f'{name}  -  Text Pad....!')
      
      # open file
      # r is for read file
      text_file=open(text_file,'r')
      stuff=text_file.read()
      # add file to text file
      my_text.insert(END,stuff)
      # close the opened file
      text_file.close()
      
# create save as file    
def save_as_file():
      text_file=filedialog.asksaveasfilename(defaultextension='.*', initialdir='storage',title='Save File',filetypes=(('Text File','*.text'),('All files','*.*')))
      if text_file:
            name=text_file
            
            # update status bar
            status_bar.config(text=f' saved :{name}        ')
            name=name.replace('storage','')
            root.title(f'{name}  -  Text Pad....!')
            
            # save the file
            # w for write a file
            text_file=open(text_file,'w')
            text_file.write(my_text.get(1.0,END))
            # close the file
            text_file.close()

# save file
def save_file():
             global open_status_name
             if open_status_name:
                   # save the file
                   text_file=open(open_status_name,'w')
                   text_file.write(my_text.get(1.0,END))
                   # close file
                   text_file.close()
                   # put status update or pop up code
                   status_bar.config(text=f'saved :{open_status_name}        ')
             else:
                     save_as_file()
                     
# cut text
def cut_text(e=''):
      global selected
      # check to see if keyboard shortcuts are used
      if e:
            selected=root.clipboard_get()
      else:
            if my_text.selection_get():
                  # grab selected text from text box
                  selected=my_text.selection_get()
                  # delete selected text from text box
                  my_text.delete('sel.first','sel.last')
                  # clear the clipboard and append
                  root.clipboard_clear()
                  root.clipboard_append(selected)
                  
      '''if my_text.selection_get():
            # grab selected text from text box
            selected=my_text.selection_get()
            # delete selected text from text box
            my_text.delete('sel.first','sel.last')'''
      
# copy text
def copy_text(e=''):
      global selected
      # check to see if the keyboard shortcuts are used
      if e:
            selected=root.clipboard_get()
      if my_text.selection_get():
             # grab selected text from text box
             selected=my_text.selection_get()
             # clear the clipboard then append
             root.clipboard_clear()
             root.clipboard_append(selected)
             
# past text
def paste_text(e=''):
      global selected
      # check to see if the keyboard shortcuts are used
      if e:
            selected=root.clipboard_get()
      else:
            if selected:
                  position=my_text.index(INSERT) 
                  my_text.insert(position, selected)     

# bold text
def bold_it():
      # create font
      bold_font=font.Font(my_text,my_text.cget('font'))    
      bold_font.configure(weight='bold')  
      # configure tag        
      my_text.tag_configure('bold',font=bold_font)                
      # define current tag
      current_tags=my_text.tag_names('sel.first')
      
      # if statement is to see  tag has set 
      if 'bold' in current_tags:
            my_text.tag_remove('bold','sel.first','sel.last')
      else:
            my_text.tag_add('bold','sel.first','sel.last')     

# italics text
def italics_it():
      # create font
      italics_font=font.Font(my_text,my_text.cget('font'))    
      italics_font.configure(slant='italic')  
      # configure tag        
      my_text.tag_configure('italic',font=italics_font)                
      # define current tag
      current_tags=my_text.tag_names('sel.first')
      
      # if statement is to see  tag has set 
      if 'italic' in current_tags:
            my_text.tag_remove('italic','sel.first','sel.last')
      else:
            my_text.tag_add('italic','sel.first','sel.last')

# change selected text color
def text_color():
      # pick a color
      my_color=colorchooser.askcolor()[1]
      if my_color:
            #status_bar.config(text=my_color)
            # create font
            color_font=font.Font(my_text,my_text.cget('font'))
            #color_font.configure(slant='colored')
            # configure tag
            my_text.tag_configure('colored',font=color_font, foreground=my_color) 
            # define current tag
            current_tags=my_text.tag_names('sel.first      ')
            # if statement is to see  tag has set
            if 'colored' in current_tags:
                  my_text.tag_remove('colored','sel.first','sel.last')
            else:
                  my_text.tag_add('colored','sel.first','sel.last')
                  
# change bg color
def bg_color():
      my_color=colorchooser.askcolor()[1]
      if my_color:
            my_text.config(bg=my_color)  

# change all text color
def all_text_color():
      my_color=colorchooser.askcolor()[1]
      if my_color:
            my_text.config(fg=my_color)  

# create toolbar frame
toolbar_frame=Frame(root)
toolbar_frame.pack(fill=X)

# create a main frame
my_frame=Frame(root)
my_frame.pack(pady=5)

# create a vertical scroll bar for text box
text_scroll=Scrollbar(my_frame)
text_scroll.pack(side=RIGHT,fill=Y)

# create a horizontal scroll bar for you  text box
hor_scroll=Scrollbar(my_frame,orient='horizontal')
hor_scroll.pack(side=BOTTOM,fill=X)

# create a text box
my_text=Text(my_frame,width=97, height=25,font=('Helvetica',16), selectbackground='yellow', selectforeground='black',undo=True, yscrollcommand=text_scroll.set, wrap=None, xscrollcommand=hor_scroll.set)
my_text.pack()

# configure our Scrollbar
text_scroll.config(command=my_text.yview)
hor_scroll.config(command=my_text.xview)

# create a menu
my_menu=Menu(root)
root.config(menu=my_menu)

# file menu
file_menu=Menu(my_menu, tearoff=FALSE)
my_menu.add_cascade(label='File',menu=file_menu)
file_menu.add_command(label='New', command=new_file)
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Save', command=save_file)
file_menu.add_command(label='Save As', command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label='Print', command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=root.quit)


# add edit menu
edit_menu=Menu(my_menu, tearoff=FALSE)
my_menu.add_cascade(label='Edit',menu=edit_menu)
edit_menu.add_command(label='Cut',command=lambda:cut_text(False), accelerator='(Ctrl+x)')
edit_menu.add_command(label='Copy',command=lambda:copy_text(False), accelerator='(Ctrl+c)')
edit_menu.add_command(label='Paste',command=lambda:paste_text(False), accelerator='(Ctrl+v)')
edit_menu.add_separator()
edit_menu.add_command(label='Undo', command=my_text.edit_undo, accelerator=('Ctrl+z'))
edit_menu.add_command(label='Redo', command=my_text.edit_redo, accelerator=('Ctrl+y'))

# add color menu
color_menu=Menu(my_menu, tearoff=FALSE)
my_menu.add_cascade(label='Colors',menu=color_menu)
color_menu.add_command(label='Selected Text',command=text_color)
color_menu.add_command(label='All Text',command=all_text_color)
color_menu.add_command(label='Background',command=bg_color)

# add a status bar at the bottom of app
status_bar=Label(root,text='ready        ', anchor=E)
status_bar.pack(fill=X,side=BOTTOM,ipady=15)

# edit bindings
root.bind('<Control-Key-x>',cut_text)
root.bind('<Control-Key-c>',copy_text)
root.bind('<Control-Key-v>', paste_text)

# create button

# bold button
bold_button=Button(toolbar_frame,text='Bold', command=bold_it)
bold_button.grid(row=0, column=0,sticky=W,padx=5)

# italic button
italics_button=Button(toolbar_frame,text='Italics', command=italics_it)
italics_button.grid(row=0, column=1,sticky=W,padx=5)

# undo or redo
undo_button=Button(toolbar_frame,text='Undo', command=my_text.edit_undo)
undo_button.grid(row=0, column=2,sticky=W,padx=5)

redo_button=Button(toolbar_frame,text='Redo', command=my_text.edit_redo)
redo_button.grid(row=0, column=3,sticky=W,padx=5)

# text color
color_text_button=Button(toolbar_frame,text='Text Color', command=text_color)
color_text_button.grid(row=0, column=4,padx=5)


root.mainloop()

# accelerator is used to accelerate the item toware the corner k
# line no 172 has been comment just to see the status bar testing