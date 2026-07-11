%global tl_name figchild
%global tl_revision 79216

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.1.2
Release:	%{tl_revision}.1
Summary:	Pictures for creating childrens activities
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/figchild
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/figchild.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/figchild.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package was created with the aim of facilitating the work of
Elementary School teachers who need to create colorful and attractive
activities for their students. It is a product of the Computational
Mathematics discipline offered at the Federal University of Vicosa --
Campus UFV -- Florestal by professor Fernando de Souza Bastos. At the
time, professor Fernando was a faculty member at the UFV Florestal
campus. Currently, he is a professor in the Department of Statistics at
the UFV main campus in Vicosa. The package makes use of the TikZ and
xcolor packages.

