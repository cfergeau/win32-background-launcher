%global goipath         github.com/crc-org/win32-background-launcher
%global goname          crc-win32-background-launcher
Version:                0.0.0.1

%gometa

# debuginfo is not supported on RHEL with Go packages
%global debug_package %{nil}
%global _enable_debug_package 0

%global common_description %{expand:
CRC's win32 background launcher}

%global golicenses    LICENSE
%global godocs        *.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        CRC's windows background launcher
License:        APL 2.0
ExcludeArch:    s390x
URL:            %{gourl}
ExcludeArch:    armv7hl i686 ppc64le
Source0:        %{gosource}

BuildRequires: git-core
BuildRequires: go-srpm-macros
BuildRequires: make

%description
%{common_description}

%gopkg

%prep
# order of these 3 steps is important, build breaks if they are moved around
%global archivename win32-background-launcher-%{version}
%autosetup -S git -n %{archivename}
# with fedora macros: goprep -e -k
install -m 0755 -vd "$(dirname %{gobuilddir}/src/%{goipath})"
ln -fs "$(pwd)" "%{gobuilddir}/src/%{goipath}"

%build
make

%install
# with fedora macros: gopkginstall
install -m 0755 -vd %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/src/%{goipath}/bin/win32-background-launcher.exe %{buildroot}%{_bindir}/

install -d %{buildroot}%{_datadir}/%{name}-redistributable/windows
install -m 0755 -vp %{gobuilddir}/src/%{goipath}/bin/win32-background-launcher.exe %{buildroot}%{_datadir}/%{name}-redistributable/windows/

%files
%license %{golicenses}
%doc
%{_bindir}/*
%{_datadir}/%{name}-redistributable/windows/*

%changelog
* Wed Oct 18 2023 Anjan Nath <anath@redhat.com>
- initial rpm spec
