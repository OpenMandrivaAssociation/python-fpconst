%define oname     fpconst
%define name      python-%{oname}
%define dname     %{oname}-%{version}


Summary:       IEEE754 float infinity and NaN for python
Name:          python-%{oname}
Version:       0.7.3
Release:       %mkrel 1
Epoch:         0
URL:           http://cheeseshop.python.org/packages/source/f/%oname/%version
Source0:       http://cheeseshop.python.org/packages/source/f/%oname/%oname-%version.tar.bz2
License:       BSD-like
Group:         Development/Python
BuildRequires: python-devel
BuildArch:     noarch
BuildRoot:     %{_tmppath}/%{name}-buildroot

%description
This module provides constants and functions for handling IEEE754
floating point infinite and NaN values.

This works on any python that uses IEEE754 double values for its float
type (whether big- or little-endian). Although this is not required,
it's unlikely any python would fail to meet this requirement (the code
in both the standard and JPython interpreters assumes IEEE754 double
all over the place).

%prep
%setup -q -n %{dname}

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install --root %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc README PKG-INFO
%defattr(-,root,root)
%{python_sitelib}/*
