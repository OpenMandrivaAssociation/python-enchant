Name:           python-enchant
Version:        1.4.0
Release:        %mkrel 2
Summary:        Python bindings for Enchant spellchecking library
Group:          Development/Python
License:        LGPL
URL:            http://pyenchant.sourceforge.net/
Source0:        http://dl.sourceforge.net/sourceforge/pyenchant/pyenchant-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:  enchant-devel python-setuptools
%py_requires -d
Provides:       PyEnchant = %{version}-%{release}

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
rm -rf $RPM_BUILD_ROOT/%{python_sitearch}/*.egg-info

 
%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc ChangeLog LICENSE.txt README.txt TODO.txt
%{python_sitearch}/enchant
