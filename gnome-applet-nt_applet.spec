Summary:	applet for GNOME panel for WebDownloader for X
Summary(pl):	aplet panelu GNOME dla WebDownloadera pod X
Name:		gnome-applet-nt_applet
Version:	1.2.3
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://www.krasu.ru/soft/chuchelo/files/nt_applet-%{version}.tar.gz
Patch0:		%{name}-fix_desktop.patch
URL:		http://www.krasu.ru/soft/chuchelo/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnome-core-devel
BuildRequires:	gettext-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	nt_applet

%define		_prefix 	/usr/X11R6/
%define		_sysconfdir	/etc/X11/GNOME

%description
nt_applet is GNOME panel applet for manage WebDownloader for X.

%description -l pl
nt_applet jest apletem panelu GNOME zarz±dzaj±cym WebDownloaderem dla
X.

%prep
%setup -q -n nt_applet-%{version}
%patch0 -p1

%build
rm -f missing
gettextize --copy --force
aclocal -I macros
%{__autoconf}
%{__automake}
%configure
%{__make}

gzip -9nf AUTHORS NEWS README

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_pixmapsdir}/nt_applet/nt.png \
	$RPM_BUILD_ROOT%{_pixmapsdir}

ln -s nt-icon-anim.gif $RPM_BUILD_ROOT%{_pixmapsdir}/nt_applet/nt-animation.default

%find_lang nt_applet

%clean
rm -rf $RPM_BUILD_ROOT

%files -f nt_applet.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/nt_applet
%{_sysconfdir}/CORBA/servers/nt_applet.gnorba
%{_datadir}/applets/Network/nt_applet.desktop
%{_pixmapsdir}/*
