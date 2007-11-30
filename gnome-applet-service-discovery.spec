%define		_realname	service-discovery-applet
Summary:	An GNOME applet for service discovery via mdns
Summary(pl.UTF-8):	Aplet GNOME do wykrywanie usług poprzez mdns
Name:		gnome-applet-service-discovery
Version:	0.4.3
Release:	0.1
License:	GPL v2
Group:		X11/Applications
Source0:	http://0pointer.de/~sebest/%{_realname}-%{version}.tar.gz
# Source0-md5:	68e67e75d4e5223e75a656b61e76d6d4
URL:		http://avahi.org/
BuildRequires:	avahi-discover >= 0.5
BuildRequires:	gettext-autopoint
BuildRequires:	python-dbus
BuildRequires:	python-devel >= 1:2.4
BuildRequires:	python-gnome
BuildRequires:	rpmbuild(macros) >= 1.198
%pyrequires_eq	python-libs
Requires(post,preun):	GConf2
Requires:	avahi-discover >= 0.5
Requires:	python-gnome-desktop-applet
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a small GNOME applet making use of the zeroconf dns-sd
facility to listen for services announced via zeroconf protocol. The
applet allows to easily connect to that service and has a quite rich
services type filter.

%description -l pl.UTF-8
Ten mały aplet GNOME wykorzystuje technologię zeroconf dns-sd do
nasłuchiwania ogłaszanych usług w sieci przy pomocy protokołu
zeroconf. Aplet pozwala w łatwy sposób łączyć się z usługami i ma
całkiem bogaty zbiór filtrów na rodzaje usług.

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
%gconf_schema_uninstall service-discovery-applet.schemas

%files -f %{_realname}.lang
%defattr(644,root,root,755)
%doc AUTHORS README TODO
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/service-discovery-applet
%{_datadir}/service-discovery-applet/icons
%{_datadir}/service-discovery-applet/interfaces
%{_datadir}/service-discovery-applet/plugins
%dir %{_datadir}/service-discovery-applet/tools
%attr(755,root,root) %{_datadir}/service-discovery-applet/tools/exec_wrapper
%{_libdir}/bonobo/servers/GNOME_ServiceDiscoveryApplet.server
%dir %{py_sitescriptdir}/sdapplet
%{py_sitescriptdir}/sdapplet/*.py[co]
%{_sysconfdir}/gconf/schemas/service-discovery-applet.schemas
