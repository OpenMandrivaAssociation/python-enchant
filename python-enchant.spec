Name:		python-enchant
Version:	1.6.5
Release:	2
Summary:	Python bindings for Enchant spellchecking library
Group:		Development/Python
License:	LGPL
URL:		http://packages.python.org/pyenchant/
Source0:	http://pypi.python.org/packages/source/p/pyenchant/pyenchant-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	pkgconfig(enchant) python-setuptools
Provides:	PyEnchant = %{version}-%{release}
Requires:	enchant >= 1.5.0

%description
PyEnchant is a spellchecking library for Python, based on the excellent Enchant
library.

PyEnchant combines all the functionality of the underlying Enchant library with
the flexibility of Python and a nice "Pythonic" object-oriented interface.

%prep
%setup -q -n pyenchant-%{version}

%build
python setup.py build


%install
python setup.py install -O1 --skip-build --root "%{buildroot}" --single-version-externally-managed
rm -rf %{buildroot}/%{python_sitelib}/*.egg-info

%files
%doc LICENSE.txt README.txt TODO.txt
%{python_sitelib}/enchant
