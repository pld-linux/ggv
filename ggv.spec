Summary:	GNOME Ghostscript Viewer
Summary(pl):	Przeglądarka Ghostscriptu dla GNOME
Name:		ggv
Version:	0.95
Release:	2
License:	GPL
Group:		X11/Applications/Graphics
Group(pl):	X11/Aplikacje/Grafika
Source0:	ftp://ftp.gnome.org/pub/GNOME/stable/sources/ggv/%{name}-%{version}.tar.gz
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	gnome-libs-devel
BuildRequires:	bonobo-devel >= 0.33
URL:		http://www.gnome.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_sysconfdir	/etc/X11/GNOME

%description
GNOME Ghostscript viewer - a GUI frontend to the Ghostscript
postscript interpretter. Use this program to preview postscript
documents on your screen.

%description -l pl
Przeglądarka Ghostscriptu dla GNOME - graficzny frontend dla
interpretera postscriptu o nazwie Ghostscript. Używaj tego programu do
przeglądania postscriptowych dokumentów na Twoim ekranie.

%prep
%setup -q

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

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/CORBA/servers/*
%{_applnkdir}/Graphics/ggv.desktop
%{_datadir}/pixmaps/*
