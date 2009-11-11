Name:           python-enchant
Version:        1.5.3
Release:        %mkrel 1
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
