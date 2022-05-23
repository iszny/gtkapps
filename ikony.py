import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from gi.repository.GdkPixbuf import Pixbuf

icons = ["dialog-warning", "dialog-error", "minecraft", "evince", "flowblade"]

class IconViewWindow(Gtk.Window):
	def __init__(self):
		super().__init__()
		self.set_default_size(200,500)
		
		liststore = Gtk.ListStore(Pixbuf, str)
		iconview = Gtk.IconView.new()
		iconview.set_model(liststore)
		iconview.set_pixbuf_column(0)
		iconview.set_text_column(1)
		
		for icon in icons:
			pixbuf = Gtk.IconTheme.get_default().load_icon(icon, 64, 0)
			liststore.append([pixbuf, "ikona"])
			
			self.add(iconview)
			
win = IconViewWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
