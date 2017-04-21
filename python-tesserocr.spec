#
# Conditional build:
%bcond_without	doc	# don't build doc
%bcond_without	tests	# do not perform "make test"
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define 	module		tesserocr
%define 	egg_name	tesserocr
%define		pypi_name	tesserocr
Summary:	A simple, Pillow-friendly, Python wrapper around tesseract-ocr API using Cython
Name:		python-%{pypi_name}
Version:	2.1.3
Release:	1
License:	MIT
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/t/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
# Source0-md5:	9fb6e8e6d1e1a7a5faa660b12d1b18fa
URL:		https://github.com/sirfz/tesserocr
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	tesseract-devel >= 3.04
%if %{with python2}
BuildRequires:	python-devel
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
tesserocr integrates directly with Tesseract's C++ API using Cython
which allows for a simple Pythonic and easy-to-read source code. It
enables real concurrent execution when used with Python's threading
module by releasing the GIL while processing an image in tesseract.

tesserocr is designed to be Pillow-friendly but can also be used with
image files instead.

%package -n python3-%{pypi_name}
Summary:	A simple, Pillow-friendly, Python wrapper around tesseract-ocr API using Cython
Group:		Libraries/Python

%description -n python3-%{pypi_name}
tesserocr integrates directly with Tesseract's C++ API using Cython
which allows for a simple Pythonic and easy-to-read source code. It
enables real concurrent execution when used with Python's threading
module by releasing the GIL while processing an image in tesseract.

tesserocr is designed to be Pillow-friendly but can also be used with
image files instead.

%prep
%setup -q -n %{pypi_name}-%{version}

# Remove bundled egg-info
%{__rm} -r %{egg_name}.egg-info

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT
%if %{with python2}
%py_install
%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.rst
%attr(755,root,root) %{py_sitedir}/%{module}.so
%{py_sitedir}/%{egg_name}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{pypi_name}
%defattr(644,root,root,755)
%doc README.rst
%attr(755,root,root) %{py3_sitedir}/%{module}.*.so
%{py3_sitedir}/%{egg_name}-%{version}-py*.egg-info
%endif