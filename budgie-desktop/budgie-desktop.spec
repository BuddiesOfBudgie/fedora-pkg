%define glib2_version 2.64
%define gnome_stack 42.0
%define gtk3_version 3.24
%define polkit_version 0.105
%define vala_version 0.52.5

Name:           budgie-desktop
Version:        10.6.1
Release:        1%{?dist}
Summary:        A feature-rich, modern desktop designed to keep out the way of the user

License:        GPLv2 and LGPLv2
URL:            https://github.com/BuddiesOfBudgie/budgie-desktop
Source0:        https://github.com/BuddiesOfBudgie/budgie-desktop/releases/download/v10.6.1/budgie-desktop-v10.6.1.tar.xz

# Drop unnecessary Comment in daemon desktop that produces warning.
# https://github.com/BuddiesOfBudgie/budgie-desktop/commit/3e2fd0dd6f8235716847d4b6c1f717719ab8632a
Patch0: 0001-Drop-unnecessary-Comment-in-daemon.patch

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
BuildRequires:  gettext
BuildRequires:  gnome-menus-devel >= 3.36
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
Requires:       lightdm
Requires:       slick-greeter
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
Requires: %{name}%{?_isa} = %{version}-%{release}

%description docs
Documentation for budgie-desktop

%prep
%autosetup -p1

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
%{_bindir}/budgie*
%{_datadir}/applications/budgie*
%{_datadir}/backgrounds/budgie/default.jpg
%{_datadir}/budgie/budgie-version.xml
%{_datadir}/gir-1.0/Budgie-1.0.gir
%{_datadir}/glib-2.0/schemas/*.gschema*
%{_datadir}/gnome-session/sessions/budgie-desktop.session
%{_datadir}/icons/*
%{_datadir}/xsessions/budgie-desktop.desktop
%{_libdir}/budgie-desktop/libgvc.so
%{_libdir}/budgie-desktop/plugins/*
%{_libdir}/lib*.so*
%{_mandir}/man1/budgie*.1*
%{_sysconfdir}/xdg/autostart/*.desktop

%files devel
%{_datadir}/vala
%{_includedir}/*
%{_libdir}/girepository-1.0/Budgie-1.0.typelib
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*

%files docs
%{_datadir}/gtk-doc

%changelog
* Sun May 15 2022 Joshua Strobl <me@joshuastrobl.com> - 10.6.1-1
- Initial inclusion of Budgie Desktop
