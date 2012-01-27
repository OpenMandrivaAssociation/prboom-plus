Name:		prboom-plus
Version:	2.5.1.1
Release:	5.7
Summary:	Open source port of the DOOM game engine

Group:		Amusements/Games/3D/Shoot
License:	GPLv2+
URL:		http://prboom-plus.sourceforge.net/
Source:		%name-%version+.tar.xz
Patch1:		prboom-nodatetime.diff
Patch2:		prboom-types1.diff
Patch3:		prboom-types2.diff
Patch4:		prboom-protos.diff
Patch5:		prboom-enable-tessellation.diff
Source2:	clean_source.sh

BuildRoot:	%_tmppath/%name-%version-build
BuildRequires:	Mesa-devel, fluidsynth-devel, libSDL_image-devel
BuildRequires:	libSDL_mixer-devel, libSDL_net-devel, libvorbis-devel
BuildRequires:	libpng-devel, pcre-devel, xz

Suggests:	freedoom
Provides:	prboom = 2.5.0+
Obsoletes:	prboom <= 2.5.0

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
%patch -P 1 -P 2 -P 3 -P 4 -P 5 -p1

%build
./bootstrap;
# rpm has its own optimizations, so turn off shipped defaults
%configure --enable-gl --disable-cpu-opt --program-prefix='' \
	--with-waddir=%_datadir/doom --disable-dogs
make %{?_smp_mflags}

%install
b="%buildroot";
make install DESTDIR="$b";
# Will manually package docs (see %%files)
rm -Rf "$b/%_datadir/doc";
mkdir -p "$b/%_bindir";
mv "$b/%_prefix/games"/* "$b/%_bindir/";
# Convenience symlink
ln -s prboom-plus "$b/%_bindir/prboom";

%files
%defattr(-,root,root,-)
%doc NEWS AUTHORS README
%doc doc/MBF.txt doc/MBFFAQ.txt doc/README.compat doc/README.demos doc/boom.txt
%_bindir/*
%_datadir/doom
%_mandir/*/*

