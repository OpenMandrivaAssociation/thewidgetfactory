Name: 		thewidgetfactory
Summary: 	Test tool for GTK2 theme
Version: 	0.2.1
Release: 	%mkrel 6
License:	GPL
Group: 		Development/Other
Source0: 	http://www.stellingwerff.com/TheWidgetFactory/thewidgetfactory-0.2.1.tar.bz2
# (fc)  add more widgets
Patch0:		thewidgetfactory-0.2.1-newwidgets.patch.bz2
# (fc) 0.2.1-3mdv port to libglade
Patch1:		thewidgetfactory-0.2.1-libglade.patch
URL:		http://www.stellingwerff.com/?page_id=10
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildRequires:	gtk2-devel
BuildRequires:  libglade2.0-devel

%description
TheWidgetFactory is a showcase of GTK2 widgets, 
only useful to theme developers.

%prep
%setup -q
%patch0 -p1 -b .newwidgets
%patch1 -p1 -b .libglade

# needed by patch1
autoreconf -fi

%build
%configure2_5x 

%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT


%files 
%defattr(-, root, root)
%doc README ChangeLog AUTHORS
%{_bindir}/*
%{_datadir}/thewidgetfactory


%changelog
* Wed Jul 27 2011 Götz Waschk <waschk@mandriva.org> 0.2.1-6mdv2012.0
+ Revision: 691855
- rebuild

* Mon Jul 26 2010 Götz Waschk <waschk@mandriva.org> 0.2.1-5mdv2011.0
+ Revision: 560817
- rebuild

* Mon Jul 20 2009 Götz Waschk <waschk@mandriva.org> 0.2.1-4mdv2010.0
+ Revision: 398119
- fix autoreconf call

* Fri Jul 18 2008 Frederic Crozat <fcrozat@mandriva.com> 0.2.1-3mdv2009.0
+ Revision: 238156
- Patch1: port to libglade and remove dependency on glade2
- Import thewidgetfactory

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot



* Fri Aug 25 2006 Frederic Crozat <fcrozat@mandriva.com> 0.2.1-1mdv2007.0
- Initial package
