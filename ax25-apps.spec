Name:           ax25-apps
Version:        0.0.8rc4
Release:        1
Summary:        AX.25 ham radio applications

Group:          Applications/Communications
#ax25ipd is BSD licensed, rest is GPLv2+
License:        GPLv2+ and BSD
URL:            http://www.linux-ax25.org/
Source0:        http://www.linux-ax25.org/pub/%{name}/%{name}-0.0.8-rc4.tar.gz
BuildRoot:      %{_tmppath}/%{name}-0.0.8-rc4-%{release}-root-%(%{__id_u} -n)

%description
This package provides specific user applications for hamradio that use AX.25 
Net/ROM or ROSE network protocols:

 * axcall: a general purpose AX.25, NET/ROM and ROSE connection program.
 * axlisten: a network monitor of all AX.25 traffic heard by the system.
 * ax25ipd: an RFC1226 compliant daemon which provides encapsulation of
   AX.25 traffic over IP.
 * ax25mond: retransmits data received from sockets into an AX.25 monitor
   socket.

%prep
%setup -q -n %{name}-0.0.8-rc4

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING README
%doc ax25ipd/COPYING.ax25ipd ax25ipd/HISTORY.ax25ipd ax25ipd/README.ax25ipd
%doc ax25rtd/TODO.ax25rtd ax25rtd/README.ax25rtd
%{_bindir}/*
%{_sbindir}/*
%{_mandir}/man?/*
%{_docdir}/*

%changelog
* Sat Jun 27 2009 Ralf Baechle <ralf@linux-mips.org>
- Initial version
