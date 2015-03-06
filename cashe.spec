%define auto_sitelib 1

%if %{auto_sitelib}
%{!?python_sitelib: %define python_sitelib %(python -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%else
%define python_sitelib /usr/lib/python?.?/site-packages
%endif

Summary: CAShe user program
Name: cashe
Version: 0.99
Release: 1%{dist}
License: LGPL+
URL: https://github.com/james-antill/CAShe
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: python
BuildRequires: libxslt docbook-dtds docbook-style-xsl docbook-style-dsssl
# CheckRequires
BuildRequires: python-nose
# Not sure how far back
Requires: python >= 2.4
Requires: python-cashe = %{version}-%{release}

%description
CAShe is a CAS (Content Addressable Storage) cache for your data/caches.
Everything that is stored in the CAShe can be deleted at any time, although
that will mainly happen when cleanup operations are called or on failures.

%package -n python-cashe
Summary: Python module for CAShe
# Not sure how far back
Requires: python >= 2.4

%description -n python-cashe
CAShe is a CAS (Content Addressable Storage) cache for your data/caches.
Everything that is stored in the CAShe can be deleted at any time, although
that will mainly happen when cleanup operations are called or on failures.

%prep
%setup -q

%build
make

%check
make check

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
mkdir -p $RPM_BUILD_ROOT/var/cache/CAShe

%clean
rm -rf $RPM_BUILD_ROOT


%files -n python-cashe
%defattr(-,root,root,-)
%doc README.md AUTHORS COPYING TODO
%{python_sitelib}/cashe
%dir /var/cache/CAShe
%ghost /var/cache/CAShe/config

%files
%{_mandir}/man*/cashe.*
%{_bindir}/cashe


%changelog
* Wed Feb 25 2015 James Antill <james@and.org> - 0.99-1
- Initial build.

