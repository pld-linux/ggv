Summary:	GNOME Ghostscript Viewer
Summary(pl):	Przegl±darka Ghostscriptu dla GNOME
Name:		ggv
Version:	1.0
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Group(pl):	X11/Aplikacje/Grafika
Source0:	ftp://ftp.gnome.org/pub/GNOME/testing/%{name}-%{version}-test7.tar.gz
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	gnome-libs-devel
BuildRequires:	bonobo-devel >= 0.33
BuildRequires:	docbook-dsssl
BuildRequires:	jade
URL:		http://www.gnome.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_sysconfdir	/etc/X11/GNOME

%description
GNOME Ghostscript viewer - a GUI frontend to the Ghostscript
postscript interpretter. Use this program to preview postscript
documents on your screen.

%description -l pl
Przegl±darka Ghostscriptu dla GNOME - graficzny frontend dla
interpretera postscriptu o nazwie Ghostscript. U¿ywaj tego programu do
przegl±dania postscriptowych dokumentów na Twoim ekranie.

%prep
%setup -q -n %{name}-%{version}-test7

%build
gettextize --copy --force
%configure \
	--enable-bonobo

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Graphicsdir=%{_applnkdir}/Graphics

gzip -9nf AUTHORS ChangeLog NEWS README

%find_lang %{name} --with-gnome

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} > /dev/null 2>&1
%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} > /dev/null 2>&1                                                                                             
%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Graphics/ggv.desktop
%{_datadir}/pixmaps/*
%{_datadir}/oaf/*
/usr/share/info/*.gz
