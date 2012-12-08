Name:           python-enchant
Version:        1.5.3
%define subrel 1
Release:        %mkrel 4
Summary:        Python bindings for Enchant spellchecking library
Group:          Development/Python
License:        LGPL
URL:            http://www.rfk.id.au/software/pyenchant/
Source0:        http://pypi.python.org/packages/source/p/pyenchant/pyenchant-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch:	noarch
BuildRequires:  enchant-devel python-setuptools
%py_requires -d
Provides:       PyEnchant = %{version}-%{release}
Requires:	enchant >= 1.5.0

%description
PyEnchant is a spellchecking library for Python, based on the Enchant
library by Dom Lachowicz.


%prep
%setup -q -n pyenchant-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT --single-version-externally-managed
rm -rf $RPM_BUILD_ROOT/%{python_sitelib}/*.egg-info

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc LICENSE.txt README.txt TODO.txt
%{python_sitelib}/enchant


%changelog
* Tue Sep 20 2011 Oden Eriksson <oeriksson@mandriva.com> 1.5.3-2.1
- built for updates

* Fri Oct 29 2010 Michael Scherer <misc@mandriva.org> 1.5.3-2mdv2011.0
+ Revision: 590146
- rebuild for python 2.7

* Wed Nov 11 2009 Funda Wang <fwang@mandriva.org> 1.5.3-1mdv2010.1
+ Revision: 464478
- new version 1.5.3

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 1.4.0-4mdv2010.0
+ Revision: 442103
- rebuild

* Thu Dec 25 2008 Funda Wang <fwang@mandriva.org> 1.4.0-3mdv2009.1
+ Revision: 318717
- fix str fmt
- rebuild for new python

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 1.4.0-2mdv2009.0
+ Revision: 269022
- rebuild early 2009.0 package (before pixel changes)

* Thu Jun 05 2008 Funda Wang <fwang@mandriva.org> 1.4.0-1mdv2009.0
+ Revision: 215211
- New version 1.4.0

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Oct 14 2007 Funda Wang <fwang@mandriva.org> 1.3.1-2mdv2008.1
+ Revision: 98308
- BR python-setuptools

* Sun Oct 14 2007 Funda Wang <fwang@mandriva.org> 1.3.1-1mdv2008.1
+ Revision: 98302
- import fedora package
- Created package structure for python-enchant.

