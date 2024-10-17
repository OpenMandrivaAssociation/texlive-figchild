Name:		texlive-figchild
Version:	62945
Release:	2
Summary:	Pictures for creating children's activities
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/figchild
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/figchild.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/figchild.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package was created with the aim of facilitating the work
of Elementary School teachers who need to create colorful and
attractive activities for their students. It is a product of
the Computational Mathematics discipline offered at the Federal
University of Vicosa -- Campus UFV -- Florestal by professor
Fernando de Souza Bastos. It makes use of the TikZ and xcolor
packages.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/figchild
%doc %{_texmfdistdir}/doc/latex/figchild

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
