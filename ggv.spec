Summary:	GNOME Ghostscript Viewer
Summary(pl):	Przeglądarka ghostscript dla GNOME
Name:		ggv
Version:	2.8.0
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.8/%{name}-%{version}.tar.bz2
# Source0-md5:	1a8e9e43ef793ef3221c5afb15d14a81
Patch0:		%{name}-mime-pdf.patch
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.7.91
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	docbook-style-dsssl
BuildRequires:	gettext-devel
BuildRequires:	ghostscript
BuildRequires:	gnome-common
BuildRequires:	gtk+2-devel >= 2:2.4.4
BuildRequires:	intltool >= 0.30
BuildRequires:	libgnomeui-devel >= 2.7.91
BuildRequires:	libbonobo-devel >= 2.6.2
BuildRequires:	libtool
BuildRequires:	openjade
BuildRequires:	popt-devel
BuildRequires:	rpm-build >= 4.1-8.2
BuildRequires:	scrollkeeper
Requires(post):	GConf2
Requires(post,postun):	scrollkeeper
Requires:	ghostscript
Requires:	libbonobo >= 2.6.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME Ghostscript viewer - a GUI frontend to the Ghostscript
postscript interpretter. Use this program to preview postscript
documents on your screen.

%description -l pl
Przeglądarka ghostscriptu dla GNOME - graficzny frontend dla
interpretera postscriptu o nazwie ghostscript. Program ten sluży do
przeglądania postscriptowych dokumentów na ekranie.

%prep
%setup -q
%patch0 -p1

sed -i -e 's/^Categories=GNOME;Application;/Categories=GTK;GNOME;/' \
        ggv.desktop.in

%build
rm -f missing acinclude.m4
%{__libtoolize}
glib-gettextize --copy --force
intltoolize --copy --force
%{__aclocal} -I %{_aclocaldir}/gnome2-macros
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
umask 022
/usr/bin/scrollkeeper-update
%gconf_schema_install
[ ! -x /usr/bin/update-desktop-database ] || /usr/bin/update-desktop-database >/dev/null 2>&1 ||:

%postun
umask 022
/usr/bin/scrollkeeper-update
[ ! -x /usr/bin/update-desktop-database ] || /usr/bin/update-desktop-database >/dev/null 2>&1

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
