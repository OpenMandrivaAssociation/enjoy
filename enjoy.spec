#Tarball of svn snapshot created as follows...
#Cut and paste in a shell after removing initial #

#svn co http://svn.enlightenment.org/svn/e/trunk/enjoy enjoy; \
#cd enjoy; \
#SVNREV=$(LANGUAGE=C svn info | grep "Last Changed Rev:" | cut -d: -f 2 | sed "s@ @@"); \
#v_maj=$(cat configure.ac | grep 'm4_define(\[v_maj\],' | cut -d' ' -f 2 | cut -d[ -f 2 | cut -d] -f 1); \
#v_min=$(cat configure.ac | grep 'm4_define(\[v_min\],' | cut -d' ' -f 2 | cut -d[ -f 2 | cut -d] -f 1); \
#v_mic=$(cat configure.ac | grep 'm4_define(\[v_mic\],' | cut -d' ' -f 2 | cut -d[ -f 2 | cut -d] -f 1); \
#PKG_VERSION=$v_maj.$v_min.$v_mic.$SVNREV; \
#cd ..; \
#tar -Jcf enjoy-$PKG_VERSION.tar.xz enjoy/ --exclude .svn --exclude .*ignore

%define svnrev  66124

Summary: 	Enjoy is a music player
Name:		enjoy
Version:	0.1.0
Release:	0.%{svnrev}.1
License:	LGPL,GPL
Group:		Graphical desktop/Enlightenment
URL:		http://enlightenment.org/
Source0: 	%{name}-%{version}.%{svnrev}.tar.xz

BuildRequires:	edje 
BuildRequires:	elementary 
BuildRequires:	embryo 
BuildRequires:	evas 
BuildRequires:	gettext-devel
BuildRequires:	pkgconfig(ecore)
BuildRequires:	pkgconfig(edbus)
BuildRequires:	pkgconfig(elementary)
BuildRequires:	pkgconfig(emotion)
BuildRequires:	pkgconfig(lightmediascanner)
BuildRequires:	pkgconfig(sqlite3)

%description
Enjoy is a music player written using Enlightenment Foundation Libraries (EFL) 
with focus on speed and mobile usability, yet should be usable on desktops as 
well.

Enjoy is modeled around a media database constructed by LightMediaScanner, it 
is not meant to play single files from disk, instead it will recursively index 
directories for music files and then list them by artist, album, genre and so 
on. Playlists are also supported, as well as random or filter playlists can be 
dynamically generated.

Feature highlight:

    * Fast database scanning
    * Efficient handling of huge collections
    * MPRIS compliant
    * mobile usability
    * Search for covers in Last.FM internet service 

%prep
%setup -qn %{name}

%build
NOCONFIGURE=yes ./autogen.sh
%configure2_5x

%make

%install
rm -rf %{buildroot}
%makeinstall_std
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

%files
%{_bindir}/*
%{_libdir}/%{name}/*.so
%{_iconsdir}/*.png
%{_datadir}/%{name}/*.edj
%{_datadir}/applications/*.desktop

