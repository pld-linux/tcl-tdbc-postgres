Summary:	TDBC driver to access PostgreSQL databases
Summary(pl.UTF-8):	Sterownik TDBC służący do dostępu do baz danych PostgreSQL
Name:		tcl-tdbc-postgres
Version:	1.0.4
Release:	1
License:	Tcl (BSD-like)
Group:		Libraries
Source0:	http://downloads.sourceforge.net/tcl/tdbcpostgres%{version}.tar.gz
# Source0-md5:	14186c69fc829b68805427f66aa78f0b
Patch0:		%{name}-man.patch
URL:		http://tdbc.tcl.tk/
BuildRequires:	tcl-devel >= 8.6
BuildRequires:	tcl-tdbc-devel >= %{version}
Requires:	tcl >= 8.6
Requires:	tcl-tdbc >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tcl TDBC PostgreSQL module is the driver for Tcl Database Connectivity
(TDBC) to access PostgreSQL databases.

%description -l pl.UTF-8
Moduł Tcl TDBC PostgreSQL to sterownik szkieletu Tcl Database
Connectivity (TDBC) służący do dostępu do baz danych PostgreSQL.

%prep
%setup -q -n tdbcpostgres%{version}
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# internal headers
%{__rm} $RPM_BUILD_ROOT%{_includedir}/{fakepq,pqStubs}.h

# allow dependency generation
chmod 755 $RPM_BUILD_ROOT%{_libdir}/tdbcpostgres%{version}/*.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README license.terms
%dir %{_libdir}/tdbcpostgres%{version}
%attr(755,root,root) %{_libdir}/tdbcpostgres%{version}/libtdbcpostgres%{version}.so
%{_libdir}/tdbcpostgres%{version}/*.tcl
%{_mandir}/mann/tdbc_postgres.n*
