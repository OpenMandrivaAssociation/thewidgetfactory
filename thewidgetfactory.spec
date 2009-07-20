Name: 		thewidgetfactory
Summary: 	Test tool for GTK2 theme
Version: 	0.2.1
Release: 	%mkrel 4
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
