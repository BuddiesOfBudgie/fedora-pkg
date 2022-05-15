%global glib2_version 2.25
%global gnome_stack 3.1.91
%global gtk3_version 2.99.3

Name:           budgie-screensaver
Version:        5.0.1
Release:        1%{?dist}
Summary:        A fork of gnome-screensaver intended for use with Budgie Desktop

License:        GPLv2
URL:            https://github.com/BuddiesOfBudgie/budgie-screensaver
Source0:        https://github.com/BuddiesOfBudgie/budgie-screensaver/releases/download/v5.0.1/budgie-screensaver-v5.0.1.tar.xz

BuildRequires:  pkgconfig(dbus-glib-1) >= 0.3.0
BuildRequires:  pkgconfig(gio-2.0) >= %{glib2_version}
BuildRequires:  pkgconfig(glib-2.0) >= %{glib2_version}
BuildRequires:  pkgconfig(gnome-desktop-3.0) >= %{gnome_stack}
BuildRequires:  pkgconfig(gsettings-desktop-schemas) >= %{gnome_stack}
BuildRequires:  pkgconfig(gthread-2.0) >= %{glib2_version}
BuildRequires:  pkgconfig(gtk+-3.0) >= %{gtk3_version}
BuildRequires:  pkgconfig(libsystemd) >= 209
BuildRequires:  pkgconfig(pam)
BuildRequires:  pkgconfig(x11) >= 1.0
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  meson

%description
A fork of gnome-screensaver intended for use with Budgie Desktop.

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name}

%files -f %{name}.lang
%doc README.md
%license LICENSE
%{_bindir}/budgie-screensaver-command
%{_bindir}/budgie-screensaver
%{_datadir}/applications/budgie-screensaver.desktop
%{_libexecdir}/budgie-screensaver-dialog
%{_mandir}/man1/budgie-screensaver-command.1*
%{_mandir}/man1/budgie-screensaver.1*
%{_sysconfdir}/pam.d/budgie-screensaver

%changelog
* Sun May 15 2022 Joshua Strobl <me@joshuastrobl.com> - 5.0.1-1
- Initial packaging of budgie-screensaver
