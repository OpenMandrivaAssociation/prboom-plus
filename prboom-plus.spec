%define		Werror_cflags %nil

Name:		prboom-plus
Version:	2.5.1.3
Release:	3
Summary:	Open source port of the DOOM game engine

Group:		Games/Arcade
License:	GPLv2+
URL:		http://prboom-plus.sourceforge.net/
Source0:	%name-%version+.tar.xz
Patch1:		prboom-nodatetime.diff
Patch2:		prboom-types1.diff
Patch3:		prboom-types2.diff
Patch4:		prboom-protos.diff
Patch5:		prboom-enable-tessellation.diff
Source2:	clean_source.sh
BuildRequires:	xz
BuildRequires:	pkgconfig(SDL_image)
BuildRequires:	pkgconfig(libpcre)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(SDL_net)
BuildRequires:	pkgconfig(SDL_mixer)
BuildRequires:	pkgconfig(fluidsynth)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)

Suggests:	freedoom

%description
PrBoom+ is a Doom source port developed from the original PrBoom
project.

prboom is an open-source port of Doom, the classic 3D first-person
shooter game. It totally outclassed any 3D world games that preceded
it, with amazing speed, flexibility, and outstanding gameplay. The
specs to the game were released, and thousands of extra levels were
written by fans of the game; even today new levels are written for
Doom faster then any one person could play them.

The target of the prboom-plus project is to extend the original port
with features that are necessary or useful to the developers and all
those interested in their work. It is worth noting that all changes
introduced in no way break PrBoom's compatibility with the original
Doom/Doom2 engines, and it is possible to be confident this will
never happen in the future since compatibility is as important.

Author(s):
----------
	Andrey "e6y" Budko

%prep
%setup -q
# %patch -P 1 -P 2 -P 3 -P 4 -P 5 -p1

%build
./bootstrap;
# rpm has its own optimizations, so turn off shipped defaults
%configure --enable-gl --disable-cpu-opt --program-prefix='' \
	--with-waddir=%{_gamesdatadir}/doom
%make

%install
%makeinstall_std
# Will manually package docs (see %%files)
rm -Rf %{buildroot}/%{_gamesdatadir}/doc;
mkdir -p %{buildroot}/%{_gamesbindir};


%files
%doc NEWS AUTHORS README
%doc doc/MBF.txt doc/MBFFAQ.txt doc/README.compat doc/README.demos doc/boom.txt
%{_gamesbindir}/*
%{_gamesdatadir}/doom
%{_mandir}/*/*
%{_docdir}/prboom-plus-2.5.1.3/*
