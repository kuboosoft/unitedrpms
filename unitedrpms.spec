Name:           unitedrpms
Version:        %{fedora}
Release:        3
Summary:        UnitedRPMs Repository Configuration

Group:          System Environment/Base
License:        GPLv3
URL:            https://unitedrpms.github.io/
Source1:        https://raw.githubusercontent.com/UnitedRPMs/unitedrpms.github.io/master/unitedrpms.repo
Source2:        https://raw.githubusercontent.com/UnitedRPMs/unitedrpms.github.io/master/URPMS-GPG-PUBLICKEY-Fedora-%{fedora}
BuildArch:      noarch


%description
UnitedRPMs is the solution for people with unstable Fedora distributions, 
increase technical skills, create a Copr-like build system for package with
licensing problems. UnitedRPMs it's not a branch maintenance of other projects,
it is only a road to give the user a fast solution without fool bureaucracy 
where everyone can help.

This package contains the UnitedRPMs GPG key, which holds
software that is not considered as Open Source Software according to the
Fedora packaging guidelines. 


%prep
echo "Nothing to prep"

%build
echo "Nothing to build"

%install

# Create dirs
install -d -m755 \
  $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg  \
  $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d

# GPG Key
%{__install} -Dp -m644 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg


# Yum .repo files
%{__install} -p -m644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d


%files
%{_sysconfdir}/pki/rpm-gpg/*
%config(noreplace) %{_sysconfdir}/yum.repos.d/*

%changelog

* Mon May 15 2017 David Vásquez <davidjeremias82 AT gmail DOT com> 
- Added local gpg keys

* Fri Jun 24 2016 David Vásquez <davidjeremias82 AT gmail DOT com> - 24-2
- Added local gpg keys

* Tue Jun 07 2016 David Vásquez <davidjeremias82 AT gmail DOT com> - 24-1
- Initial build

