Summary:	GNOME Ghostscript Viewer
Summary(pl):	Przegl±darka ghostscript dla GNOME
Name:		ggv
Version:	2.8.5
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://ftp.gnome.org/pub/gnome/sources/ggv/2.8/%{name}-%{version}.tar.bz2
# Source0-md5:	e8b338c1427e170ffbb33c62d0aaf191
Patch0:		%{name}-desktop.patch
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.8.1
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	docbook-style-dsssl
BuildRequires:	gettext-devel
BuildRequires:	ghostscript
BuildRequires:	gnome-common >= 2.8.0
BuildRequires:	gtk+2-devel >= 2:2.4.4
BuildRequires:	intltool >= 0.30
BuildRequires:	libbonobo-devel >= 2.6.2
BuildRequires:	libgnomeui-devel >= 2.10.0-2
BuildRequires:	libtool
BuildRequires:	openjade
BuildRequires:	pkgconfig
BuildRequires:	popt-devel
BuildRequires:	rpm-build >= 4.1-8.2
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	scrollkeeper
Requires(post,preun):	GConf2
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	scrollkeeper
Requires:	ghostscript
Requires:	libbonobo >= 2.6.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME Ghostscript viewer - a GUI frontend to the Ghostscript
postscript interpretter. Use this program to preview postscript
documents on your screen.

%description -l pl
Przegl±darka ghostscriptu dla GNOME - graficzny frontend dla
interpretera postscriptu o nazwie ghostscript. Program ten slu¿y do
przegl±dania postscriptowych dokumentów na ekranie.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing acinclude.m4
%{__libtoolize}
%{__glib_gettextize}
%{__intltoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-platform-gnome-2 \
	--disable-schemas-install
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

rm -r $RPM_BUILD_ROOT%{_datadir}/locale/no

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install ggv.schemas
%scrollkeeper_update_post
%update_desktop_database_post

%preun
%gconf_schema_uninstall ggv.schemas

%postun
%scrollkeeper_update_postun
%update_desktop_database_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/ggv*
%{_datadir}/gnome-2.0/ui/ggv*
%{_datadir}/idl/*
%{_libdir}/bonobo/servers/*
%{_omf_dest_dir}/%{name}
%{_desktopdir}/ggv.desktop
%{_pixmapsdir}/*
%{_sysconfdir}/gconf/schemas/*
