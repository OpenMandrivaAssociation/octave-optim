%global octpkg optim

Summary:	Non-linear optimization toolkit
Name:		octave-optim
Version:	1.6.2
Release:	2
License:	GPLv3+ and BSD and Public Domain
Group:		Sciences/Mathematics
Url:		https://packages.octave.org/optim/
Source0:	https://downloads.sourceforge.net/octave/optim-%{version}.tar.gz

BuildRequires:  octave-devel >= 4.0.0
BuildRequires:  octave-statistics >= 1.4.0
BuildRequires:  octave-struct >= 1.0.12

Requires:	octave(api) = %{octave_api}
Requires:  	octave-statistics >= 1.4.0
Requires:  	octave-struct >= 1.0.12

Requires(post): octave
Requires(postun): octave

%description
Non-linear optimization toolkit.

%files
%license COPYING
%doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*
%dir %{octpkglibdir}
%{octpkglibdir}/*
%{_metainfodir}/*.metainfo.xml

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-%{version}

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

