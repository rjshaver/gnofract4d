
from gi.repository import Gtk

class Table(Gtk.Table):
    def __init__(self,rows=1,cols=1,homogeneous=False):
        self.__gobject_init__()
        GObject.GObject.__init__(self,rows,cols,homogeneous)
        self.nextrow=0
        self.set_col_spacing(0,10)

    def add(
        self,
        widget,col,
        xoptions=Gtk.AttachOptions.EXPAND|Gtk.AttachOptions.FILL,yoptions=Gtk.AttachOptions.EXPAND|Gtk.AttachOptions.FILL,
        xpadding=0, ypadding=0):
        self.attach(
            widget,col,col+1,self.nextrow,self.nextrow+1,
            xoptions,yoptions,xpadding,ypadding)

    def next():
        self.nextrow += 1
