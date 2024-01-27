import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GdkPixbuf
import subprocess

def capture_window(window):
    # Create an offscreen window and render the contents of the provided window onto it
    offscreen_window = Gtk.OffscreenWindow()
    width, height = window.get_size()
    offscreen_window.set_default_size(width, height)
    offscreen_window.add(window)
    offscreen_window.show_all()

    # Get the GdkPixbuf from the offscreen window
    pixbuf = offscreen_window.get_pixbuf()

    return pixbuf

def render_in_mpv(pixbuf):
    # Convert the Pixbuf to a format compatible with mpv
    # Save the Pixbuf to a temporary file
    tmp_file = "/tmp/gtk_window.png"
    pixbuf.savev(tmp_file, "png", [], [])
    
    # Use subprocess to call mpv and display the temporary file
    subprocess.run(["mpv", tmp_file])

def main():
    # Create a GTK window
    window = Gtk.Window()
    window.connect("destroy", Gtk.main_quit)
    window.show_all()

    # Capture the window contents
    pixbuf = capture_window(window)

    # Render in mpv
    render_in_mpv(pixbuf)

    Gtk.main()

if __name__ == "__main__":
    main()
