# $Revision: 1.1 $Date: 2003-11-25 13:40:21 $
Summary:	SQLite PAM Module
Summary(pl):	Modu³ PAM SQLite
Name:		pam-pam_sqlite
Version:	0.3
Release:	1
License:	GPL
Group:		Base
Source0:	http://www.edin.dk/pam_sqlite/distributions/%{name}-%{version}.tar.gz
# Source0-md5:	61ad442fe619bb1dbb00fd5ba28e54bd
Source1:	%{name}.conf
Patch0:		%{name}-pld.patch
URL:		http://www.edin.dk/pam_sqlite/
BuildRequires:	pam-devel
BuildRequires:	sqlite-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define _libdir /lib/security

%description
PAM SQLite is a PAM module that uses SQLite database.

%description -l pl
PAM SQLite jest modu³em PAM u¿ywaj±cym bazy SQLite.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1

%build
%configure2_13 \
	%{!?debug:--disable-debug}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_libdir},%{_sysconfdir}}

%{__make} install \
	ROOTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README NEWS
%attr(755,root,root) %{_libdir}/pam_sqlite.so
%attr(600,root,root) %{_sysconfdir}/%{name}.conf
