Summary:	/etc/protocols and /etc/services provided by IANA
Name:		iana-etc
Version:	2.30
Release:	1
License:	OSL v.3.0
Group:		Applications
Source0:	http://sethwklein.net/%{name}-%{version}.tar.bz2
# Source0-md5:	3ba3afb1d1b261383d247f46cb135ee8
Patch0:		newer.patch
URL:		http://sethwklein.net/iana-etc.html
BuildRequires:	gawk
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The iana-etc package provides the Unix/Linux /etc/services and
/etc/protocols files.

%prep
%setup -q
%patch0 -p1

%build
%{__make} get
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install port-numbers.iana protocol-numbers.iana \
	$RPM_BUILD_ROOT%{_datadir}/%{name}

%check
%{__make} -j1 test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING CREDITS NEWS README
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/protocols
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/services
%{_datadir}/%{name}

