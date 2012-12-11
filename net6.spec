%define name   net6
%define api    1.3
%define major  0
%define libname %mklibname net6- %api %major
%define libname_devel %mklibname net6- %api -d

Summary:    A library to ease the development of network-based applications
Name:       %{name}
Version:    1.3.14
Release:    1
URL:        http://gobby.0x539.de/
License:    GPLv2+
Source0:    http://releases.0x539.de/%{name}/%{name}-%{version}.tar.gz
Group:      System/Libraries
BuildRequires: pkgconfig(sigc++-2.0)
BuildRequires: pkgconfig(gnutls)
BuildRequires: gettext-devel

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

%build
%configure2_5x
%make

%install
rm -Rf $RPM_BUILD_ROOT
%makeinstall_std
# remove translation, do not know where to place it 
rm -Rf $RPM_BUILD_ROOT/%_datadir/ 

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
%_libdir/*.a
%_libdir/pkgconfig/*


%changelog
* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 1.3.12-2mdv2011.0
+ Revision: 613011
- the mass rebuild of 2010.1 packages

* Thu Feb 11 2010 Michael Scherer <misc@mandriva.org> 1.3.12-1mdv2010.1
+ Revision: 504040
- new version 1.3.12
- remove patch0, applied upstream

* Thu Jun 04 2009 Funda Wang <fwang@mandriva.org> 1.3.9-2mdv2010.0
+ Revision: 382609
- BR gettext-devel
- autoreconf
- build with gnutls 2.8

* Fri Mar 06 2009 Michael Scherer <misc@mandriva.org> 1.3.9-1mdv2009.1
+ Revision: 349848
- update to 1.3.9

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 1.3.6-3mdv2009.0
+ Revision: 253738
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Mon Jan 21 2008 Funda Wang <fwang@mandriva.org> 1.3.6-1mdv2008.1
+ Revision: 155565
- New version 1.3.6

* Mon Jan 21 2008 Funda Wang <fwang@mandriva.org> 1.3.5-2mdv2008.1
+ Revision: 155487
- correct libname

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Aug 18 2007 Michael Scherer <misc@mandriva.org> 1.3.5-1mdv2008.0
+ Revision: 66425
- fix buildrequires
- new version 1.3.5
- Import net6



* Mon Sep 04 2006 Michael Scherer <misc@mandriva.org> 1.3.1-1mdv2007.0
- New version 1.3.1

* Thu Dec 15 2005 Michael Scherer <misc@mandriva.org> 1.2.2-1mdk
- New release 1.2.2

* Mon Nov 28 2005 Michael Scherer <misc@mandriva.org> 1.2.1-1mdk
- New release 1.2.1, and new major

* Fri Nov 04 2005 Michael Scherer <misc@mandriva.org> 1.1.0-1mdk
- first package 
