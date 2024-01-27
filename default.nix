{ pkgs ? import <nixpkgs> {}}:

pkgs.mkShell {

    buildInputs = [
        pkgs.python311Packages.pygobject3
            pkgs.gtk4
            pkgs.gtk3
            pkgs.glade
            pkgs.gobject-introspection

    ];

    env = {
        MPLBACKEND="GTK3Cairo";
    };


}
