Summary:     GNOME Ghostscript Viewer
Name:        ggv
Version:     0.26
Release:     4
Copyright:   GPL
Group:       X11/gnome
Source:      ftp://ftp.gnome.org/pub/GNOME/sources/%{name}-%{version}.tar.gz
BuildRoot:   /tmp/%{name}-%{version}-root
URL:         http://www.gnome.org

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
%attr(755, root, root) /usr/X11R6/bin/ggv
/usr/X11R6/share/apps/Graphics/ggv.desktop
%lang(fr) /usr/X11R6/share/locale/fr/LC_MESSAGES/ggv.mo
%lang(ko) /usr/X11R6/share/locale/ko/LC_MESSAGES/ggv.mo
%lang(pt) /usr/X11R6/share/locale/pt/LC_MESSAGES/ggv.mo

%changelog
* Fri Sep 18 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.26-4]
- changed prefix to /usr/X11R6.

* Sun Sep  6 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.26-3]
- added -q %setup parameter,
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- added using %%{name} and %%{version} in Source,
- added %lang macros for /usr/share/locale/*/LC_MESSAGES/ggv.mo files,
- changed Copyright: field to GPL,
- changed Group: to X11/gnome,
- removed COPYING from %doc (copyright statment is in Copyright: field),
- added full %attr description in %files,
- added striping binaries.

* Thu Aug 20 1998 Michael Fulbright <msf@redhat.com>
- Added a %clean section

* Thu Aug 20 1998 Michael Fulbright <msf@redhat.com>
- First spec file
