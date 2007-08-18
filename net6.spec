%define name   net6  
%define major   1.3
%define libname %mklibname net6_ %major
%define libname_devel %mklibname net6_ %major -d

Summary:    A library to ease the development of network-based applications
Name:       %{name}
Version:    1.3.5
Release:    %mkrel 1
URL:        http://gobby.0x539.de/
License:    GPL
Source0:    http://releases.0x539.de/%{name}/%{name}-%{version}.tar.bz2
Group:      System/Libraries
BuildRequires: sigc++2.0-devel
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
%description 
net6 is a library which eases the development of network-based applications
as it provides a TCP protocol abstraction for C++. It is portable to both
the Windows and Unix-like platforms.

%package -n %libname
Summary:    A library to ease the development of network-based applications
Group:      System/Libraries

%description -n %libname
net6 is a library which eases the development of network-based applications
as it provides a TCP protocol abstraction for C++. It is portable to both
the Windows and Unix-like platforms.



%package -n %libname_devel
Summary:    Development files for %libname
Group:      System/Libraries
Provides:   lib%{name}-devel
Requires:   %libname = %version
%description -n %libname_devel
Development files, header and includes for %libname.

net6 is a library which eases the development of network-based applications
as it provides a TCP protocol abstraction for C++. It is portable to both
the Windows and Unix-like platforms.


%prep
%setup -q 

%build
%configure
%make

%install
rm -Rf $RPM_BUILD_ROOT
%makeinstall_std
# remove translation, do not know where to place it 
rm -Rf $RPM_BUILD_ROOT/%_datadir/ 

%clean
rm -Rf $RPM_BUILD_ROOT

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%files -n %libname
%defattr(-,root,root,-)
%doc ChangeLog README NEWS AUTHORS 
%_libdir/*.so.*

%files -n %libname_devel
%defattr(-,root,root,-)
%_includedir/%name/
%_libdir/*.so
%_libdir/*.la
%_libdir/*.a
%_libdir/pkgconfig/*
