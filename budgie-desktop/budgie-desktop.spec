%global glib2_version 2.64
%global gnome_stack 42.0
%global gtk3_version 3.24
%global polkit_version 0.105
%global vala_version 0.52.5

Name:           budgie-desktop
Version:        10.6.2
Release:        1%{?dist}
Summary:     A feature-rich, modern desktop designed to keep out the way of the user

License:        GPLv2 and LGPLv2
URL:               https://github.com/BuddiesOfBudgie/budgie-desktop
Source0:       %{url}/releases/download/v%{version}/%{name}-v%{version}.tar.xz
Source1:       %{url}/releases/download/v%{version}/%{name}-v%{version}.tar.xz.asc
Source2:       https://joshuastrobl.com/pubkey.gpg

BuildRequires:  pkgconfig(accountsservice) >= 0.6.55
BuildRequires:  pkgconfig(alsa) >= 1.2.6
BuildRequires:  pkgconfig(glib-2.0) >= %{glib2_version}
BuildRequires:  pkgconfig(gio-unix-2.0) >= %{glib2_version}
BuildRequires:  pkgconfig(gdk-x11-3.0) >= %{gtk3_version}
BuildRequires:  pkgconfig(gnome-bluetooth-1.0) >= 3.34.0
BuildRequires:  pkgconfig(gnome-desktop-3.0) >= %{gnome_stack}
BuildRequires:  pkgconfig(gnome-settings-daemon) >= %{gnome_stack}
BuildRequires:  pkgconfig(gtk+-3.0) >= %{gtk3_version}
BuildRequires:  pkgconfig(ibus-1.0) >= 1.5.10
BuildRequires:  pkgconfig(libnotify) >= 0.7
BuildRequires:  pkgconfig(libpeas-1.0) >= 1.26.0
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libwnck-3.0) >= 3.36.0
BuildRequires:  pkgconfig(polkit-agent-1) >= %{polkit_version}
BuildRequires:  pkgconfig(polkit-gobject-1) >= %{polkit_version}
BuildRequires:  pkgconfig(upower-glib) >= 0.99.13
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(vapigen) >= %{vala_version}
BuildRequires:  budgie-desktop-view
BuildRequires:  budgie-screensaver
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gnome-menus-devel >= 3.36
BuildRequires:  gnupg2
BuildRequires:  gsettings-desktop-schemas >= %{gnome_stack}
BuildRequires:  gtk-doc >= 1.33.0
BuildRequires:  intltool
BuildRequires:  meson
BuildRequires:  mutter-devel >= %{gnome_stack}
BuildRequires:  sassc
BuildRequires:  vala
Requires:       budgie-desktop-view
Requires:       budgie-screensaver
Requires:       gnome-bluetooth3.34-libs
Requires:       gnome-session
Requires:       gnome-settings-daemon
Requires:       gsettings-desktop-schemas 
Requires:       network-manager-applet
Requires:       xdotool
Suggests:       budgie-control-center
Suggests:       materia-gtk-theme
Suggests:       papirus-icon-theme

Requires: glib2%{?_isa} >= %{glib2_version}
Requires: gtk3%{?_isa} >= %{gtk3_version}

%description
A feature-rich, modern desktop designed to keep out the way of the user.

%package devel
Summary: Development package for budgie-desktop
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files, libraries, and other files for developing Budgie Desktop.

%package docs
Summary: Documentation for budgie-desktop
Requires: gtk-doc
Requires: %{name}%{?_isa} = %{version}-%{release}

%description docs
Documentation for budgie-desktop

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files -f %{name}.lang
%doc README.md
%license LICENSE
%dir %{_datadir}/backgrounds/budgie
%dir %{_datadir}/budgie
%dir %{_datadir}/gir-1.0
%dir %{_datadir}/icons
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/scalable
%dir %{_datadir}/icons/hicolor/scalable/actions
%dir %{_datadir}/icons/hicolor/scalable/apps
%dir %{_datadir}/icons/hicolor/scalable/status
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins/
%dir %{_libdir}/%{name}/plugins/*
%{_bindir}/budgie-*
%{_datadir}/applications/budgie-*
%{_datadir}/backgrounds/budgie/default.jpg
%{_datadir}/budgie/budgie-version.xml
%{_datadir}/gir-1.0/Budgie-1.0.gir
%{_datadir}/glib-2.0/schemas/20_solus-project.budgie.wm.gschema.override
%{_datadir}/glib-2.0/schemas/com.solus-project.*.gschema.xml
%{_datadir}/gnome-session/sessions/%{name}.session
%{_datadir}/icons/hicolor/scalable/actions/*.svg
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%{_datadir}/icons/hicolor/scalable/status/*.svg
%{_datadir}/xsessions/%{name}.desktop
%{_libdir}/%{name}/libgvc.so
%{_libdir}/%{name}/plugins/*/*.plugin
%{_libdir}/%{name}/plugins/*/*.so*
%{_libdir}/libbudgie-plugin.so.0
%{_libdir}/libbudgie-plugin.so.0.0.0
%{_libdir}/libbudgie-private.so.0
%{_libdir}/libbudgie-private.so.0.0.0
%{_libdir}/libbudgietheme.so.0
%{_libdir}/libbudgietheme.so.0.0.0
%{_libdir}/libraven.so.0
%{_libdir}/libraven.so.0.0.0
%{_mandir}/man1/budgie-*.1*
%{_sysconfdir}/xdg/autostart/*.desktop

%files devel
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%dir %{_includedir}/%{name}
%{_datadir}/vala/vapi/budgie-1.0.deps
%{_datadir}/vala/vapi/budgie-1.0.vapi
%{_includedir}/%{name}/*.h
%{_libdir}/girepository-1.0/Budgie-1.0.typelib
%{_libdir}/libbudgie-plugin.so
%{_libdir}/libbudgie-private.so
%{_libdir}/libbudgietheme.so
%{_libdir}/libraven.so
%{_libdir}/pkgconfig/budgie-1.0.pc
%{_libdir}/pkgconfig/budgie-theme-1.0.pc

%files docs
%dir %{_datadir}/gtk-doc/html/
%dir %{_datadir}/gtk-doc/html/%{name}
%{_datadir}/gtk-doc/html/%{name}/*

%changelog
* Thu Jul 14 2022 Joshua Strobl <me@joshuastrobl.com> - 10.6.2-1
- Initial inclusion of Budgie Desktop
