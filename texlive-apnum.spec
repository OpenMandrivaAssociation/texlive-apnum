Name:		texlive-apnum
Version:	47510
Release:	2
Summary:	Arbitrary precision numbers implemented by TeX macros
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/apnum
License:	pd
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/apnum.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/apnum.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The basic operations (addition, subtraction, multiplication,
division, power to an integer) are implemented by TeX macros in
this package. Operands may be numbers with arbitrary numbers of
digits; scientific notation is allowed. The expression scanner
is also provided. As of version 1.4 (December 2015) the
calculation of common functions (sqrt, exp, ln, sin, cos, tan,
asin, acos, atan, pi) with arbitrary precision in the result
has been added. Exhaustive documentation (including detailed
TeXnical documentation) is included. The macro includes many
optimizations and uses only TeX primitives (from classic TeX)
and \newcount macro.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/generic/apnum
%doc %{_texmfdistdir}/doc/generic/apnum

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
