Summary:	GNOME Ghostscript Viewer
Summary(pl):	Przegl±darka Ghostscriptu dla GNOME
Name:		ggv
Version:	1.1.95
Release:	2
License:	GPL
Group:		X11/Applications/Graphics
Source0:	ftp://ftp.gnome.org//pub/GNOME/sources/ggv/%{version}/%{name}-%{version}.tar.gz
Patch0:		%{name}-omf.patch
Patch1:		%{name}-ac25x.patch
Patch2:		%{name}-am16.patch
Patch3:		%{name}-buffer.patch
URL:		http://www.gnome.org/
BuildRequires:	GConf-devel >= 0.12
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bonobo-devel >= 0.33
BuildRequires:	docbook-style-dsssl
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	libtool
BuildRequires:	libxml-devel
BuildRequires:	oaf-devel >= 0.6.2
BuildRequires:	openjade
BuildRequires:	scrollkeeper
Requires:	ghostscript
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_sysconfdir	/etc/X11/GNOME
%define		_omf_dest_dir	%(scrollkeeper-config --omfdir)

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
%patch2 -p1
%patch3 -p1

%build
rm -f missing acinclude.m4
%{__libtoolize}
%{__gettextize}
%{__aclocal} -I macros
%{__autoconf}
%{__automake}
#CPPFLAGS="`gnome-config --cflags bonobo`"; export CPPFLAGS
#LDFLAGS="-L%{_libdir} -lbonobox"; export LDFLAGS
%configure \
	--enable-bonobo

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Graphicsdir=%{_applnkdir}/Graphics/Viewers \
	omf_dest_dir=%{_omf_dest_dir}/%{name}

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /usr/bin/scrollkeeper-update
%postun -p /usr/bin/scrollkeeper-update

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Graphics/Viewers/ggv.desktop
%{_datadir}/gnome/ui/ggv*
%{_pixmapsdir}/*
%{_datadir}/oaf/*
%{_datadir}/idl/*
%{_omf_dest_dir}/%{name}
%{_sysconfdir}/gconf/schemas/ggv.schemas
