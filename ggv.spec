Summary:     GNOME Ghostscript Viewer
Name:        ggv
Version:     0.26
Release:     3
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
# Needed for snapshot releases.
if [ ! -f configure ]; then
  CFLAGS="$RPM_OPT_FLAGS" ./autogen.sh --prefix=/usr
else
  CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr
fi

make

%install
rm -rf $RPM_BUILD_ROOT
make prefix=$RPM_BUILD_ROOT/usr install

strip $RPM_BUILD_ROOT/usr/bin/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%doc AUTHORS ChangeLog NEWS README
%attr(755, root, root) /usr/bin/ggv
/usr/share/apps/Graphics/ggv.desktop
%lang(fr) /usr/share/locale/fr/LC_MESSAGES/ggv.mo
%lang(ko) /usr/share/locale/ko/LC_MESSAGES/ggv.mo
%lang(pt) /usr/share/locale/pt/LC_MESSAGES/ggv.mo

%changelog
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
