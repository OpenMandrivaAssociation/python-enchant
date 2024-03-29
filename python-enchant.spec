Summary:	Python bindings for Enchant spellchecking library
Name:		python-enchant
Version:	3.2.2
Release:	2
Group:		Development/Python
License:	LGPLv2
Url:		https://pypi.org/project/pyenchant/
Source0:	https://files.pythonhosted.org/packages/source/p/pyenchant/pyenchant-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	python-setuptools
BuildRequires:	python2-setuptools
BuildRequires:	pkgconfig(enchant)
BuildRequires:	pkgconfig(python2)
BuildRequires:	pkgconfig(python3)
Provides:	PyEnchant = %{version}-%{release}
Requires:	enchant2 >= 2.2.0
%rename 	python3-enchant

%description
PyEnchant is a spellchecking library for Python, based on the excellent Enchant
library.

PyEnchant combines all the functionality of the underlying Enchant library with
the flexibility of Python and a nice "Pythonic" object-oriented interface.

%package -n python2-enchant
Summary:	Python bindings for Enchant spellchecking library
Group:		Development/Python
Requires:	python3
 
%description -n python2-enchant
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
python2 setup.py install -O1 --skip-build --root "%{buildroot}" --single-version-externally-managed
popd

pushd python3
python3 setup.py install -O1 --skip-build --root "%{buildroot}" --single-version-externally-managed
popd

%files
%doc python3/LICENSE.txt
%{py3_puresitedir}/enchant
%{py3_puresitedir}/*.egg-info

%files -n python2-enchant
%doc python2/LICENSE.txt
%{py2_puresitedir}/enchant
%{py2_puresitedir}/*.egg-info
