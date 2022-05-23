import gi
gi.require_version("Gtk", "3.0")
gi.require_version('Notify', '0.7')
from gi.repository import Gtk, Notify


class MyWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Hello World")
        Gtk.Window.set_default_size(self, 400, 300)
        Notify.init("powiadomienie")

        self.box = Gtk.Box(spacing=10)
        self.add(self.box)

        self.button1 = Gtk.Button(label="Powitanie")
        self.button1.connect("clicked", self.on_button1_clicked)
        self.box.pack_start(self.button1, True, True, 0)

        self.button2 = Gtk.Button(label="Pożegnanie")
        self.button2.connect("clicked", self.on_button2_clicked)
        self.box.pack_start(self.button2, True, True, 0)

    def on_button1_clicked(self, widget):
        n = Notify.Notification.new("Powiadomienie z aplikacji", "Witaj!")
        n.show()

    def on_button2_clicked(self, widget):
        n = Notify.Notification.new("Powiadomienie z aplikacji", "Do widzenia!")
        n.show()


win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
