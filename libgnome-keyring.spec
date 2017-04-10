#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libgnome-keyring
Version  : 3.12.0
Release  : 1
URL      : https://download.gnome.org/sources/libgnome-keyring/3.12/libgnome-keyring-3.12.0.tar.xz
Source0  : https://download.gnome.org/sources/libgnome-keyring/3.12/libgnome-keyring-3.12.0.tar.xz
Summary  : The GNOME keyring libraries
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.0
Requires: libgnome-keyring-data
Requires: libgnome-keyring-lib
Requires: libgnome-keyring-doc
Requires: libgnome-keyring-locales
BuildRequires : docbook-xml
BuildRequires : gettext
BuildRequires : gobject-introspection-dev
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : intltool
BuildRequires : libgcrypt-dev
BuildRequires : libgpg-error-dev
BuildRequires : libxslt-bin
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(dbus-1)
BuildRequires : pkgconfig(glib-2.0)

%description
gnome-keyring is a program that keep password and other secrets for
users. The library libgnome-keyring is used by applications to integrate
with the gnome keyring system.

%package data
Summary: data components for the libgnome-keyring package.
Group: Data

%description data
data components for the libgnome-keyring package.


%package dev
Summary: dev components for the libgnome-keyring package.
Group: Development
Requires: libgnome-keyring-lib
Requires: libgnome-keyring-data
Provides: libgnome-keyring-devel

%description dev
dev components for the libgnome-keyring package.


%package doc
Summary: doc components for the libgnome-keyring package.
Group: Documentation

%description doc
doc components for the libgnome-keyring package.


%package lib
Summary: lib components for the libgnome-keyring package.
Group: Libraries
Requires: libgnome-keyring-data

%description lib
lib components for the libgnome-keyring package.


%package locales
Summary: locales components for the libgnome-keyring package.
Group: Default

%description locales
locales components for the libgnome-keyring package.


%prep
%setup -q -n libgnome-keyring-3.12.0

%build
export LANG=C
export SOURCE_DATE_EPOCH=1491866747
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1491866747
rm -rf %{buildroot}
%make_install
%find_lang libgnome-keyring

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/GnomeKeyring-1.0.typelib
/usr/share/gir-1.0/*.gir

%files dev
%defattr(-,root,root,-)
/usr/include/gnome-keyring-1/gnome-keyring-memory.h
/usr/include/gnome-keyring-1/gnome-keyring-result.h
/usr/include/gnome-keyring-1/gnome-keyring.h
/usr/lib64/libgnome-keyring.so
/usr/lib64/pkgconfig/gnome-keyring-1.pc

%files doc
%defattr(-,root,root,-)
/usr/share/gtk-doc/html/gnome-keyring/annotation-glossary.html
/usr/share/gtk-doc/html/gnome-keyring/ch01.html
/usr/share/gtk-doc/html/gnome-keyring/gnome-keyring-Callbacks.html
/usr/share/gtk-doc/html/gnome-keyring/gnome-keyring-Daemon-Management-Functions.html
/usr/share/gtk-doc/html/gnome-keyring/gnome-keyring-Item-ACLs.html
/usr/share/gtk-doc/html/gnome-keyring/gnome-keyring-Item-Attributes.html
/usr/share/gtk-doc/html/gnome-keyring/gnome-keyring-Item-Information.html
/usr/share/gtk-doc/html/gnome-keyring/gnome-keyring-Keyring-Info.html
/usr/share/gtk-doc/html/gnome-keyring/gnome-keyring-Keyring-Items.html
/usr/share/gtk-doc/html/gnome-keyring/gnome-keyring-Keyrings.html
/usr/share/gtk-doc/html/gnome-keyring/gnome-keyring-Miscellaneous-Functions.html
/usr/share/gtk-doc/html/gnome-keyring/gnome-keyring-Network-Passwords.html
/usr/share/gtk-doc/html/gnome-keyring/gnome-keyring-Non-pageable-Memory.html
/usr/share/gtk-doc/html/gnome-keyring/gnome-keyring-Result-Codes.html
/usr/share/gtk-doc/html/gnome-keyring/gnome-keyring-Search-Functionality.html
/usr/share/gtk-doc/html/gnome-keyring/gnome-keyring-Simple-Password-Storage.html
/usr/share/gtk-doc/html/gnome-keyring/gnome-keyring.devhelp2
/usr/share/gtk-doc/html/gnome-keyring/home.png
/usr/share/gtk-doc/html/gnome-keyring/index.html
/usr/share/gtk-doc/html/gnome-keyring/index.sgml
/usr/share/gtk-doc/html/gnome-keyring/left.png
/usr/share/gtk-doc/html/gnome-keyring/right.png
/usr/share/gtk-doc/html/gnome-keyring/style.css
/usr/share/gtk-doc/html/gnome-keyring/up.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/libgnome-keyring.so.0
/usr/lib64/libgnome-keyring.so.0.2.0

%files locales -f libgnome-keyring.lang
%defattr(-,root,root,-)

