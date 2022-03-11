%global octpkg optim

Summary:	Non-linear optimization toolkit
Name:		octave-%{octpkg}
Version:	1.6.1
Release:	1
Source0:	http://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
License:	GPLv3+ and BSD and Public Domain
Group:		Sciences/Mathematics
Url:		https://octave.sourceforge.io/%{octpkg}/

BuildRequires:	octave-devel >= 4.0.0
BuildRequires:	octave-statistics >= 1.4.0
BuildRequires:	octave-struct >= 1.0.12

Requires:	octave(api) = %{octave_api}
Requires:	octave-statistics >= 1.4.0
Requires:	octave-struct >= 1.0.12

Requires(post): octave
Requires(postun): octave

%description
Non-linear optimization toolkit.

This package is part of community Octave-Forge collection.

%files
%license COPYING
%doc NEWS
%dir %{octpkglibdir}
%{octpkglibdir}/*
%dir %{octpkgdir}
%{octpkgdir}/*
%{_metainfodir}/*.metainfo.xml

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-%{version}

# remove backup files
#find . -name \*~ -delete

%build
%set_build_flags
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

