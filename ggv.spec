Summary:     GNOME Ghostscript Viewer
Summary(pl): Przegl±darka Ghostscriptu dla GNOME
Name:        ggv
Version:     0.26
Release:     5
Copyright:   GPL
Group:       X11/Libraries
Source:      ftp://ftp.gnome.org/pub/GNOME/sources/%{name}-%{version}.tar.gz
URL:         http://www.gnome.org
BuildRoot:	/tmp/%{name}-%{version}-root

%description
GNOME Ghostscript viewer - a GUI frontend to the Ghostscript postscript
interpretter. Use this program to preview postscript documents on your
screen.

%description -l pl
Przegl±darka Ghostscriptu dla GNOME - graficzny frontend dla interpretera
postscriptu o nazwie Ghostscript. U¿ywaj tego programu do przegl±dania
postscriptowych dokumentów na Twoim ekranie.

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" \
./configure %{_target_platform} \
	--prefix=/usr/X11R6

make

%install
rm -rf $RPM_BUILD_ROOT

make prefix=$RPM_BUILD_ROOT/usr/X11R6 install

strip $RPM_BUILD_ROOT/usr/X11R6/bin/*

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) /usr/X11R6/bin/ggv
/usr/X11R6/share/apps/Graphics/ggv.desktop
