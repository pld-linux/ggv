Summary:	GNOME Ghostscript Viewer
Summary(pl):	Przegl±darka Ghostscriptu dla GNOME
Name:		ggv
Version:	1.99.97
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/1.99/%{name}-%{version}.tar.bz2
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	docbook-style-dsssl
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2.2.0
BuildRequires:	libtool
BuildRequires:	GConf2-devel >= 1.2.1-10
BuildRequires:	openjade
BuildRequires:	scrollkeeper
BuildRequires:	bonobo-activation-devel >= 2.1.0-3
BuildRequires:	rpm-build >= 4.1-8.2
Requires(post):	GConf2
Requires(post):	scrollkeeper
Requires:	ghostscript
Requires:	bonobo-activation >= 2.1.0-3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME Ghostscript viewer - a GUI frontend to the Ghostscript
postscript interpretter. Use this program to preview postscript
documents on your screen.

%description -l pl
Przegl±darka Ghostscriptu dla GNOME - graficzny frontend dla
interpretera postscriptu o nazwie Ghostscript. U¿ywaj tego programu do
przegl±dania postscriptowych dokumentów na Twoim ekranie.

%prep
%setup -q

%build
%configure --enable-platform-gnome-2 \
	   --disable-install-schemas

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT 

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/bin/scrollkeeper-update
%gconf_schema_install

%postun -p /usr/bin/scrollkeeper-update

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/ggv*
%{_datadir}/applications/ggv.desktop
%{_datadir}/gnome-2.0/ui/ggv*
%{_datadir}/idl/*
%{_libdir}/bonobo/servers/*
%{_omf_dest_dir}/%{name}
%{_pixmapsdir}/*
%{_sysconfdir}/gconf/schemas/*
