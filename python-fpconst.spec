%define oname     fpconst
%define name      python-%{oname}
%define dname     %{oname}-%{version}


Summary:       IEEE754 float infinity and NaN for python
Name:          python-%{oname}
Version:       0.7.3
Release:       3
Epoch:         0
URL:           https://cheeseshop.python.org/packages/source/f/%oname/%version
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


%changelog
* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0:0.7.3-2mdv2010.0
+ Revision: 442113
- rebuild

* Sun Jan 04 2009 Jérôme Soyer <saispo@mandriva.org> 0:0.7.3-1mdv2009.1
+ Revision: 324270
- New upstream release

* Sun Dec 28 2008 Funda Wang <fwang@mandriva.org> 0:0.7.2-5mdv2009.1
+ Revision: 320140
- rebuild for new python

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 0:0.7.2-4mdv2009.0
+ Revision: 259613
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 0:0.7.2-3mdv2009.0
+ Revision: 247415
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0:0.7.2-1mdv2008.1
+ Revision: 136448
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Dec 09 2006 David Walluck <walluck@mandriva.org> 0.7.2-1mdv2007.0
+ Revision: 93951
- 0.7.2
- Import python-fpconst

* Sat May 14 2005 Michael Scherer <misc@mandriva.org> 0.6.0-6mdk
- from Tigrux <tigrux@ximian.com>
  - Do not require python = 2.5

* Sun Dec 05 2004 Michael Scherer <misc@mandrake.org> 0.6.0-5mdk
- Rebuild for new python

