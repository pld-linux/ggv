Summary:	GNOME Ghostscript Viewer
Summary(pl):	Przegl±darka Ghostscriptu dla GNOME
Name:		ggv
Version:	1.1.94
Release:	3
License:	GPL
Group:		X11/Applications/Graphics
Source0:	ftp://ftp.gnome.org/pub/GNOME/unstable/sources/ggv/%{name}-%{version}.tar.gz
URL:		http://www.gnome.org/
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	bonobo-devel >= 0.33
BuildRequires:	docbook-style-dsssl
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	gnome-libs-devel
BuildRequires:	oaf-devel >= 0.6.2
BuildRequires:	GConf-devel >= 0.12
BuildRequires:	openjade
BuildRequires:	libtool
BuildRequires:	scrollkeeper
Prereq:		scrollkeeper
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
%setup -q -n %{name}-%{version}

%build
#rm missing acinclude.m4
#libtoolize --copy --force
#gettextize --copy --force
#aclocal -I macros
#autoconf
#automake -a -c
CPPFLAGS="`gnome-config --cflags bonobo`"; export CPPFLAGS
LDFLAGS="-L%{_libdir} -lbonobox"; export LDFLAGS
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

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} > /dev/null 2>&1
/usr/bin/scrollkeeper-update

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} > /dev/null 2>&1
/usr/bin/scrollkeeper-update

%clean
rm -rf $RPM_BUILD_ROOT

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
