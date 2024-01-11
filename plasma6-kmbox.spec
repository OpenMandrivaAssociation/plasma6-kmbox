%define major 6
%define libname %mklibname KPim6Mbox
%define devname %mklibname KPim6Mbox -d

Name: plasma6-kmbox
Version:	24.01.90
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Release:	1
Source0: http://download.kde.org/%{ftpdir}/release-service/%{version}/src/kmbox-%{version}.tar.xz
Summary: KDE library for accessing MBOX mail files
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(KPim6Mime)
BuildRequires: boost-devel
# For QCH format docs
BuildRequires: doxygen
BuildRequires: qt6-qttools-assistant

%description
KDE library for accessing MBOX mail files

%package -n %{libname}
Summary: KDE library for accessing MBOX mail files
Group: System/Libraries

%description -n %{libname}
KDE library for accessing MBOX mail files

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%autosetup -p1 -n kmbox-%{version}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build

%files -n %{libname}
%{_datadir}/qlogging-categories6/kmbox.categories
%{_datadir}/qlogging-categories6/kmbox.renamecategories
%{_libdir}/*.so*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/cmake/*
