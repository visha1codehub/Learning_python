a = open('txxxt.txt','w')
a.write('''Hello,
        This is Vishal.
        I am trying to learn python basics.
        In this I am learning about File Handeling.
        It is so easy topic.
        But I was so confused because I didn't learn this topic very well.
        But now I think I would learn and understand this very easily.''')
a.close()

with open ('txxxt.txt','r') as f:
    data = f.read()
print(data)
# # -- coding: utf-8 --

# ## Class responsible for creating the freight query area

# # This class is responsible for the graphical interface + all
# # a logical part.  


# ## Required libraries:
# # Local file:
# from auxWidgets import AuxWidgets

# # GUI:
# from auxWidgets import QWidget


# class  Gui_ConsFrete ( AuxWidgets ):
#     ## Constructor: defines the super class as well as the group
#     def _init(self, wid:QWidget) -> None:                                 
#         super(Gui_ConsFrete, self)._init_()

#         self.root = self.gBox("Consulta Frete", 990, 450, 360, 210, wid_)               # Cria o Group Box
#         self . root . setEnabled ( False )                                                      # v5.0: Leave inactive

#         self . gui_Ui ()                                                                    # Calls the GUI (Graphical Interface) build method
        

#     ## Destroyer: deallocates declared attributes
#     def _del_(self) -> None:
#         del  self . root                                                                    # Delete attributes
#         del self.btVeri, self.btCopi, self.resp,self.tOrigem, self.tDestino
    

#     ## Method: create and configure window
#     def gui_Ui(self) -> None:
#         self . tOrigin  =  self . lblBt ( "Source:" , 10 , 80 , self . root )                          # Create label and input text

#         self . tDestination  =  self . lblBt ( "Target:" , 195 , 260 , self . root )                      # Create label and text input

#         self . resp  =  self . txtView ( 10 , 60 , 340 , 100 , self . root )                            # Create text visualization area

#         self . btVeri  =  self . bts ( "Verify" , 140 , 173 , 100 , 23 , self . root )                # Create the "Verify" button

#         self . btCopi  =  self . bts ( "Copy" , 250 , 173 , 100 , 23 , self . root )                   # Create the "Copy" button