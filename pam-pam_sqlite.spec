# $Revision: 1.13 $Date: 2008-02-01 01:47:52 $
%define 	modulename pam_sqlite
Summary:	SQLite PAM Module
Summary(pl.UTF-8):	Moduł PAM SQLite
Name:		pam-%{modulename}
Version:	0.3
Release:	2
Epoch:		0
License:	GPL
Group:		Base
Source0:	http://www.edin.dk/pam_sqlite/distributions/%{modulename}-%{version}.tar.gz
# Source0-md5:	61ad442fe619bb1dbb00fd5ba28e54bd
Source1:	%{name}.conf
Patch0:		%{name}-pld.patch
Patch1:		%{name}-null.patch
URL:		http://www.edin.dk/pam_sqlite/
BuildRequires:	pam-devel
BuildRequires:	sqlite-devel
Obsoletes:	pam_sqlite
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libdir		/%{_lib}/security

%description
PAM SQLite is a PAM module that uses SQLite database.

%description -l pl.UTF-8
PAM SQLite jest modułem PAM używającym bazy SQLite.

%prep
%setup -q -n %{modulename}-%{version}
%patch0 -p1
%patch1 -p1

%build
%configure2_13 \
	%{!?debug:--disable-debug}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_sysconfdir}}

install -c pam_sqlite.so $RPM_BUILD_ROOT%{_libdir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README NEWS
%attr(755,root,root) %{_libdir}/pam_sqlite.so
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.conf
