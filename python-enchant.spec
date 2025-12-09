Summary:	Python bindings for Enchant spellchecking library
Name:		python-enchant
Version:	3.3.0
Release:	1
Group:		Development/Python
License:	LGPLv2
Url:		https://pypi.org/project/pyenchant/
Source0:	https://files.pythonhosted.org/packages/source/p/pyenchant/pyenchant-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	python
BuildRequires:	pkgconfig(enchant)
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(setuptools)
BuildSystem:	python
Provides:	PyEnchant = %{version}-%{release}
Requires:	enchant2 >= 2.2.0
%rename 	python3-enchant
# Not really a drop-in replacement, but python2 support has to go
Obsoletes:	python2-enchant < %{EVRD}

%description
PyEnchant is a spellchecking library for Python, based on the excellent Enchant
library.

PyEnchant combines all the functionality of the underlying Enchant library with
the flexibility of Python and a nice "Pythonic" object-oriented interface.

%files
%{py_puresitedir}/enchant
%{py_puresitedir}/*.dist-info
