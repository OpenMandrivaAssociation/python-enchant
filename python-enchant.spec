Summary:	Python bindings for Enchant spellchecking library
Name:		python-enchant
Version:	1.6.5
Release:	3
Group:		Development/Python
License:	LGPLv2
Url:		http://packages.python.org/pyenchant/
Source0:	http://pypi.python.org/packages/source/p/pyenchant/pyenchant-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	python-setuptools
BuildRequires:	python3-distribute
BuildRequires:	pkgconfig(enchant)
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(python3)
Provides:	PyEnchant = %{version}-%{release}
Requires:	enchant >= 1.5.0

%description
PyEnchant is a spellchecking library for Python, based on the excellent Enchant
library.

PyEnchant combines all the functionality of the underlying Enchant library with
the flexibility of Python and a nice "Pythonic" object-oriented interface.

%package -n python3-enchant
Summary:	Python bindings for Enchant spellchecking library
Group:		Development/Python
Requires:	python3
 
%description -n python3-enchant
PyEnchant is a spellchecking library for Python, based on the excellent Enchant
library.

PyEnchant combines all the functionality of the underlying Enchant library with
the flexibility of Python and a nice "Pythonic" object-oriented interface.

%prep
%setup -q -c

mv pyenchant-%{version} python2
cp -r python2 python3

%build
pushd python2
python setup.py build
popd

pushd python3
python3 setup.py build
popd

%install
pushd python2
python setup.py install -O1 --skip-build --root "%{buildroot}" --single-version-externally-managed
popd

pushd python3
python3 setup.py install -O1 --skip-build --root "%{buildroot}" --single-version-externally-managed
popd

%files
%doc python2/LICENSE.txt python2/README.txt python2/TODO.txt
%{python_sitelib}/enchant
%{python_sitelib}/*.egg-info

%files -n python3-enchant
%doc python3/LICENSE.txt python3/README.txt python3/TODO.txt
%{python3_sitelib}/enchant
%{python3_sitelib}/*.egg-info

