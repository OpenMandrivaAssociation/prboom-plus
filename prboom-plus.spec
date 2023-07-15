%global optflags %{optflags} -Wno-incompatible-function-pointer-types

%define		Werror_cflags %nil

Name:		prboom-plus
Version:	2.6.66
Release:	1
Summary:	Open source port of the DOOM game engine

Group:		Games/Arcade
License:	GPLv2+
URL:		http://prboom-plus.sourceforge.net/
Source0:	https://github.com/coelckers/prboom-plus/archive/refs/tags/v%{version}um/%{name}-%{version}.tar.gz

BuildRequires:	cmake
BuildRequires:	xz
BuildRequires:	pkgconfig(libpcre)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:  pkgconfig(SDL2_image)
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(SDL2_net)
BuildRequires:  pkgconfig(sdl2)
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
%setup -q -n %{name}-%{version}
%autopatch -p1

%build
cd prboom2
%cmake
%make_build

%install
cd prboom2
%make_install -C build

# Will manually package docs (see %%files)
rm -Rf %{buildroot}/%{_gamesdatadir}/doc;
mkdir -p %{buildroot}/%{_gamesbindir};


%files
%doc %{_datadir}/doc/prboom-plus/
%{_bindir}/prboom-plus
%{_bindir}/prboom-plus-game-server
%{_datadir}/prboom-plus/prboom-plus.wad
%{_mandir}/*/*
