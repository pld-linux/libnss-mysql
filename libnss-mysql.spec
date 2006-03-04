Summary:	MySQL Name Service Switch Module
Summary(pl):	Modu³ NSS MySQL
Name:		libnss-mysql
Version:	1.5
Release:	1
License:	GPL
Group:		Base
Source0:	http://dl.sourceforge.net/libnss-mysql/%{name}-%{version}.tar.gz
# Source0-md5:	a34d41a38e426ba26ffde07d03beef8e
URL:		http://libnss-mysql.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	mysql-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libdir		/%{_lib}

%description
libnss-mysql is a NSS library for MySQL. It features full groups,
passwd and shadow support.

%description -l pl
libnss-mysql jest bibliotek± NSS dla MySQL. Pozwala ona na
przechowywanie informacji typowych dla plików groups, passwd oraz
shadow w bazie MySQL.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	MYSQL_LIB_DIR=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_libdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog DEBUGGING FAQ README NEWS THANKS TODO UPGRADING sample
%attr(755,root,root) %{_libdir}/*.so.*.*
%attr(644,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.cfg
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}-root.cfg
