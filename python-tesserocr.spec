# TODO: 2 tests fail (with tesserect 5.3.1)
#
# Conditional build:
%bcond_with	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define		module		tesserocr
%define		egg_name	tesserocr
%define		pypi_name	tesserocr
Summary:	A simple, Pillow-friendly, Python wrapper around tesseract-ocr API using Cython
Summary(pl.UTF-8):	Proste, zgodne z Pillow obudowanie API tesseract-ocr przy użyciu Cythona
Name:		python-%{pypi_name}
Version:	2.6.0
Release:	1
License:	MIT
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/t/tesserocr/%{pypi_name}-%{version}.tar.gz
# Source0-md5:	87582e2fe5d020ebdf0ccd76569c9ed8
URL:		https://github.com/sirfz/tesserocr
BuildRequires:	leptonlib-devel >= 1.71
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	pkgconfig
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	tesseract-devel >= 3.04
%if %{with python2}
BuildRequires:	python-Cython >= 0.23
BuildRequires:	python-devel >= 1:2.7
BuildRequires:	python-pillow
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-Cython >= 0.23
BuildRequires:	python3-devel >= 1:3.4
BuildRequires:	python3-pillow
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

%description -l pl.UTF-8
tesserocr integruje się bezpośrednio z API C++ Tesseracta przy użyciu
Cythona, który pozwala tworzyć prosty, pythonowy, łatwo czytelny kod.
W połączeniu z pythonowym modułem threading umożliwia współbieżne
wykonywanie, zwalniając GIL przy przetwarzaniu obrazu w tesserakcie.

tesserocr jest zaprojektowany jako zgodny z Pillow, ale może być
używany także z plikami obrazów.

%package -n python3-%{pypi_name}
Summary:	A simple, Pillow-friendly, Python wrapper around tesseract-ocr API using Cython
Summary(pl.UTF-8):	Proste, zgodne z Pillow obudowanie API tesseract-ocr przy użyciu Cythona
Group:		Libraries/Python

%description -n python3-%{pypi_name}
tesserocr integrates directly with Tesseract's C++ API using Cython
which allows for a simple Pythonic and easy-to-read source code. It
enables real concurrent execution when used with Python's threading
module by releasing the GIL while processing an image in tesseract.

tesserocr is designed to be Pillow-friendly but can also be used with
image files instead.

%description -n python3-%{pypi_name} -l pl.UTF-8
tesserocr integruje się bezpośrednio z API C++ Tesseracta przy użyciu
Cythona, który pozwala tworzyć prosty, pythonowy, łatwo czytelny kod.
W połączeniu z pythonowym modułem threading umożliwia współbieżne
wykonywanie, zwalniając GIL przy przetwarzaniu obrazu w tesserakcie.

tesserocr jest zaprojektowany jako zgodny z Pillow, ale może być
używany także z plikami obrazów.

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
