%define gitdate 20131224

Summary:	Music player for Enlightenment
Name:		enjoy
Version:	0.1.0
Release:	1.%{gitdate}.1
License:	LGPLv3+
Group:		Graphical desktop/Enlightenment
Url:		http://enlightenment.org/
Source0: 	%{name}-%{gitdate}.tar.bz2
BuildRequires:	edje
BuildRequires:	elementary
BuildRequires:	embryo
BuildRequires:	evas
BuildRequires:	gettext-devel
BuildRequires:	pkgconfig(ecore)
BuildRequires:	pkgconfig(ecore-evas)
BuildRequires:	pkgconfig(ecore-file)
BuildRequires:	pkgconfig(eina)
BuildRequires:	pkgconfig(eldbus)
BuildRequires:	pkgconfig(elementary)
BuildRequires:	pkgconfig(emotion)
BuildRequires:	pkgconfig(evas)
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

%files
%{_bindir}/*
%{_libdir}/enjoy_ql.so
%{_libdir}/%{name}/*.so
%{_iconsdir}/*.png
%{_datadir}/%{name}/*.edj
%{_datadir}/applications/*.desktop

#----------------------------------------------------------------------------

%prep
%setup -qn %{name}

%build
autoreconf -fi
%configure2_5x \
	--disable-static

%make

%install
%makeinstall_std


