Summary:	GNOME Ghostscript Viewer
Summary(pl):	Przegl±darka Ghostscriptu dla GNOME
Name:		ggv
Version:	2.5.2
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.5/%{name}-%{version}.tar.bz2
# Source0-md5:	e3697de171a078395cd832ba52d46de0
Patch0:		%{name}-mime-pdf.patch
Patch1:		%{name}-libtool.patch
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.5.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	docbook-style-dsssl
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2.3.1
BuildRequires:	intltool
BuildRequires:	libbonobo-devel >= 2.5.0
BuildRequires:	libtool >= 0.29
BuildRequires:	openjade
BuildRequires:	rpm-build >= 4.1-8.2
BuildRequires:	scrollkeeper
BuildRequires:	gnome-common
BuildRequires:	ghostscript
Requires(post):	GConf2
Requires(post):	scrollkeeper
Requires:	ghostscript
Requires:	libbonobo >= 2.5.0
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
%patch0 -p1
%patch1 -p1

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
	--disable--schemas-install

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
unset GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL

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
%{_datadir}/gnome-2.0/ui/ggv*
%{_datadir}/idl/*
%{_libdir}/bonobo/servers/*
%{_omf_dest_dir}/%{name}
%{_desktopdir}/ggv.desktop
%{_pixmapsdir}/*
%{_sysconfdir}/gconf/schemas/*
