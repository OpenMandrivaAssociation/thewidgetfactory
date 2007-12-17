Name: 		thewidgetfactory
Summary: 	Test tool for GTK2 theme
Version: 	0.2.1
Release: 	%mkrel 1
License:	GPL
Group: 		Development/Other
Source0: 	http://www.stellingwerff.com/TheWidgetFactory/thewidgetfactory-0.2.1.tar.bz2
# (fc)  add more widgets
Patch0:		thewidgetfactory-0.2.1-newwidgets.patch.bz2
URL:		http://www.stellingwerff.com/?page_id=10
BuildRequires:	gtk2-devel
BuildRequires:  glade2
%if %mdkversion <= 200600
BuildRequires:  XFree86-Xvfb
%else
BuildRequires:  x11-server-xvfb
%endif

%description
TheWidgetFactory is a showcase of GTK2 widgets, 
only useful to theme developers.

%prep
%setup -q
%patch0 -p1 -b .newwidgets

# fix build
aclocal-1.9
autoconf

%build
%configure2_5x 

XDISPLAY=$(i=1; while [ -f /tmp/.X$i-lock ]; do i=$(($i+1)); done; echo $i)
%if %mdkversion <= 200600
%{_prefix}/X11R6/bin/Xvfb :$XDISPLAY &
%else
%{_bindir}/Xvfb -fp /usr/share/fonts/misc :$XDISPLAY &
%endif
export DISPLAY=:$XDISPLAY
glade-2 -w twf.glade
kill $(cat /tmp/.X$XDISPLAY-lock)


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
