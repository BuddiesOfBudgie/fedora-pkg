%define cheese_version 3.28.0
%define glib2_version 2.64
%define gnome_online_accounts_version 3.44.0
%define gnome_stack 42.0
%define gtk3_version 3.24
%define polkit_version 0.105
%define upower_version 0.99.8
%define vala_version 0.52.5

Name:           budgie-control-center
Version:        1.0.2
Release:        1%{?dist}
Summary:        A fork of GNOME Control Center for the Budgie 10 Series

License:        GPLv2+ and CC-BY-SA
URL:            https://github.com/BuddiesOfBudgie/budgie-control-center
Source0:        https://github.com/BuddiesOfBudgie/budgie-control-center/releases/download/v1.0.2/budgie-control-center-1.0.2.tar.xz

BuildRequires:  pkgconfig(accountsservice)
BuildRequires:  pkgconfig(cheese) >= %{cheese_version}
BuildRequires:  pkgconfig(colord-gtk)
BuildRequires:  pkgconfig(gcr-3)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gnome-bluetooth-1.0) >= 3.34.0
BuildRequires:  pkgconfig(gnome-desktop-3.0) >= %{gnome_stack}
BuildRequires:  pkgconfig(gnome-settings-daemon) >= %{gnome_stack}
BuildRequires:  pkgconfig(gio-2.0) >= %{glib2_version}
BuildRequires:  pkgconfig(goa-1.0)
BuildRequires:  pkgconfig(goa-backend-1.0)
BuildRequires:  pkgconfig(grilo-0.3)
BuildRequires:  pkgconfig(gsettings-desktop-schemas) >= %{gnome_stack}
BuildRequires:  pkgconfig(gsound)
BuildRequires:  pkgconfig(gtk+-3.0) >= %{gtk3_version}
BuildRequires:  pkgconfig(ibus-1.0)
BuildRequires:  pkgconfig(libcanberra-gtk3)
BuildRequires:  pkgconfig(libgtop-2.0)
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(libnm) >= 1.24
BuildRequires:  pkgconfig(libnma)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libpulse-mainloop-glib)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libwacom)
BuildRequires:  pkgconfig(malcontent-0)
BuildRequires:  pkgconfig(mm-glib)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(pwquality)
BuildRequires:  pkgconfig(smbclient)
BuildRequires:  pkgconfig(udisks2)
BuildRequires:  pkgconfig(upower-glib) >= 0.99.13
BuildRequires:  pkgconfig(x11)
BuildRequires:  chrpath
BuildRequires:  cups-devel
BuildRequires:  desktop-file-utils
BuildRequires:  docbook-style-xsl libxslt
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires: libappstream-glib
BuildRequires:  meson

Requires: cheese-libs%{?_isa} >= %{cheese_version}
Requires: glib2%{?_isa} >= %{glib2_version}
Requires: gnome-bluetooth%{?_isa}
Requires: gnome-desktop3%{?_isa} >= %{gnome_stack}
Requires: gnome-online-accounts%{?_isa} >= %{gnome_online_accounts_version}
Requires: gnome-settings-daemon%{?_isa} >= %{gnome_stack}
Requires: gsettings-desktop-schemas%{?_isa} >= %{gnome_stack}
Requires: gtk3%{?_isa} >= %{gtk3_version}
Requires: upower%{?_isa} >= %{upower_version}

# For user accounts
Requires: accountsservice
Requires: alsa-lib

# For the thunderbolt panel
Recommends: bolt

# For the color panel
Requires: colord

# For the printers panel
Requires: cups-pk-helper
Requires: dbus

# For the info/details panel
Requires: glx-utils
Recommends: switcheroo-control

# For the user languages
Requires: iso-codes

# For the network panel
Recommends: NetworkManager-wifi
Recommends: nm-connection-editor

# For parental controls support
Requires: malcontent
Requires: malcontent-control

# For Show Details in the color panel
Recommends: gnome-color-manager

# For the sharing panel
Recommends: gnome-remote-desktop

# For the power panel
Recommends: power-profiles-daemon

%description
A fork of GNOME Control Center for the Budgie 10 Series.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
%meson \
    -Ddark_mode_distributor_logo=%{_datadir}/pixmaps/system-logo-white.png \
    -Ddocumentation=true \
    -Dmalcontent=true
%meson_build


%install
%meson_install
mkdir -p %{buildroot}%{_datadir}/budgie/wm-properties
rm -rf %{buildroot}%{_datadir}/budgie/autostart
rm -rf %{buildroot}%{_datadir}/budgie/cursor-fonts
chrpath --delete %{buildroot}%{_bindir}/budgie-control-center
%find_lang %{name} --all-name --with-gnome

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/budgie-control-center.appdata.xml

%files -f %{name}.lang
%license LICENSE
%doc README.md
%{_bindir}/budgie-control-center
%{_datadir}/applications/*.desktop
%{_datadir}/bash-completion/completions/budgie-control-center
%{_datadir}/dbus-1/services/org.buddiesofbudgie.ControlCenter.service
%{_datadir}/glib-2.0/schemas/org.buddiesofbudgie.ControlCenter.gschema.xml
%{_datadir}/budgie-control-center/keybindings/*.xml
%{_datadir}/budgie-control-center/pixmaps
%{_datadir}/budgie/wm-properties
%{_datadir}/icons/*
%{_datadir}/man/man1/budgie-control-center.1*
%{_datadir}/metainfo/budgie-control-center.appdata.xml
%{_datadir}/pixmaps/budgie-faces
%{_datadir}/pixmaps/budgie-logo.png
%{_datadir}/pkgconfig/budgie-keybindings.pc
%{_datadir}/polkit-1/actions/org.buddiesofbudgie.controlcenter.*.policy
%{_datadir}/polkit-1/rules.d/budgie-control-center.rules
%{_datadir}/sounds/budgie/default/*/*.ogg
%{_libexecdir}/budgie-cc-remote-login-helper
%{_libexecdir}/budgie-control-center-print-renderer

%changelog
* Sun May 15 2022 Joshua Strobl <me@joshuastrobl.com> - 1.0.1-1
- Initial packaging of Budgie Control Center
