%define name   net6
%define api    1.3
%define major  0
%define libname %mklibname net6- %api %major
%define libname_devel %mklibname net6- %api -d

Summary:    A library to ease the development of network-based applications
Name:       %{name}
Version:    1.3.9
Release:    %mkrel 2
URL:        http://gobby.0x539.de/
License:    GPLv2+
Source0:    http://releases.0x539.de/%{name}/%{name}-%{version}.tar.gz
Patch0:     net6-1.3.9-gnutls-2.8.patch
Group:      System/Libraries
BuildRequires: sigc++2.0-devel
BuildRequires: pkgconfig(gnutls)
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
%description 
net6 is a library which eases the development of network-based applications
as it provides a TCP protocol abstraction for C++. It is portable to both
the Windows and Unix-like platforms.

%package -n %libname
Summary:    A library to ease the development of network-based applications
Group:      System/Libraries
Obsoletes:  %mklibname net6_ 1.3

%description -n %libname
net6 is a library which eases the development of network-based applications
as it provides a TCP protocol abstraction for C++. It is portable to both
the Windows and Unix-like platforms.

%package -n %libname_devel
Summary:    Development files for %libname
Group:      System/Libraries
Provides:   lib%{name}-devel
Obsoletes:  %mklibname -d net6_ 1.3
Requires:   %libname = %version

%description -n %libname_devel
Development files, header and includes for %libname.

net6 is a library which eases the development of network-based applications
as it provides a TCP protocol abstraction for C++. It is portable to both
the Windows and Unix-like platforms.

%prep
%setup -q
%patch0 -p0

%build
autoreconf -fi
%configure2_5x
%make

%install
rm -Rf $RPM_BUILD_ROOT
%makeinstall_std
# remove translation, do not know where to place it 
rm -Rf $RPM_BUILD_ROOT/%_datadir/ 

%clean
rm -Rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files -n %libname
%defattr(-,root,root,-)
%doc ChangeLog README NEWS AUTHORS 
%_libdir/*%{api}.so.%{major}*

%files -n %libname_devel
%defattr(-,root,root,-)
%_includedir/%name/
%_libdir/*.so
%_libdir/*.la
%_libdir/*.a
%_libdir/pkgconfig/*
