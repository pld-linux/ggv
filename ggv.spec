Summary:     GNOME Ghostscript Viewer
Name:        ggv
Version:     0.26
Release:     4
Copyright:   GPL
Group:       X11/Libraries
Source:      ftp://ftp.gnome.org/pub/GNOME/sources/%{name}-%{version}.tar.gz
URL:         http://www.gnome.org
BuildRoot:   /tmp/%{name}-%{version}-root

%description
GNOME Ghostscript viewer - a GUI frontend to the Ghostscript postscript
interpretter. Use this program to preview postscript documents on your
screen.

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr/X11R6

make

%install
rm -rf $RPM_BUILD_ROOT

make prefix=$RPM_BUILD_ROOT/usr/X11R6 install

strip $RPM_BUILD_ROOT/usr/X11R6/bin/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)

%doc AUTHORS ChangeLog NEWS README
%atttr(755, root, root) /usr/X11R6/bin/ggv
/usr/X11R6/share/apps/Graphics/ggv.desktop

%lang(fr) /usr/X11R6/share/locale/fr/LC_MESSAGES/ggv.mo
%lang(ko) /usr/X11R6/share/locale/ko/LC_MESSAGES/ggv.mo
%lang(pt) /usr/X11R6/share/locale/pt/LC_MESSAGES/ggv.mo

%changelog
* Fri Oct  2 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.26-4]
- added -q %setup parameter,
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- added using %%{name} and %%{version} in Source,
- removed COPYING from %doc,
- added striping binaries,
- added %lang macros for /usr/X11R6/share/locale/*/LC_MESSAGES/ggv.mo
  files,
- added full %attr description in %files.

* Thu Aug 20 1998 Michael Fulbright <msf@redhat.com>
- Rebuilt against gnome-libs 0.30

* Thu Aug 20 1998 Michael Fulbright <msf@redhat.com>
- Added a %clean section

* Thu Aug 20 1998 Michael Fulbright <msf@redhat.com>
- First spec file
