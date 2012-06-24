%define		_realname   service-discovery-applet
Summary:	An GNOME applet for service discovery via mdns
Summary(pl):	Applet GNOME do wykrywanie us�ug poprzez mdns
Name:		gnome-applet-service-discovery
Version:	0.4
Release:	0.1
License:	GPL v2
Group:		X11/Applications
Source0:	http://0pointer.de/~sebest/%{_realname}-%{version}.tar.gz
# Source0-md5:	85083dd169ab00c3ab29911c3775a9d2
URL:		http://avahi.org/
BuildRequires:	avahi-devel >= 0.5
BuildRequires:	python-gnome
Requires:	avahi >= 0.5
Requires:	GConf2
Requires:	libbonobo
Requires:	python-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a small GNOME applet making use of the zeroconf dns-sd facility to
listen for services announced via zeroconf protocol. The applet allows to
easily connect to that service and  has a quite rich services type filter.

%description -l pl
Ten ma�y applet GNOME wykorzystuje technologi� zeroconf dns-sd to nas�uchiwania
og�aszanych us�ug w sieci przy pomocy protoko�u zeroconf. Applet pozwala
po��czy� si� z us�ugami w �atwy spos�b oraz posada ca�kiem bogaty zbi�r filtr�w
na typy us�ug.

%prep
%setup -q -n %{_realname}-%{version}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{_realname}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install service-discovery-applet.schemas

%preun
%gconf_schema_uninstall service-discovery-applet.schema

%files -f %{_realname}.lang
%defattr(644,root,root,755)
#%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/service-discovery-applet
%{_libdir}/bonobo/servers/GNOME_ServiceDiscoveryApplet.server
%dir %{py_sitescriptdir}/sdapplet
%{py_sitescriptdir}/sdapplet/*.pyc
%{py_sitescriptdir}/sdapplet/*.pyo
%{_sysconfdir}/gconf/schemas/service-discovery-applet.schemas
