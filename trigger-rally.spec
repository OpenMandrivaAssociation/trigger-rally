%define	oname	trigger

Summary:	Rally racing game
Name:		%{oname}-rally
Version:	0.6.0
Release:	%mkrel 1
Source0:	http://downloads.sourceforge.net/trigger-rally/%{name}-%{version}-src.tar.bz2
Source1:	%{name}.png
Patch0:		trigger-0.5.2.1-nodoc.patch
License:	GPLv2
Group:		Games/Arcade
Url:		http://sourceforge.net/projects/trigger-rally/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	automake1.8
BuildRequires:	jam
BuildRequires:	SDL-devel
BuildRequires:	SDL_image-devel
BuildRequires:	freealut-devel
BuildRequires:	glew-devel
BuildRequires:	mesagl-devel
BuildRequires:	mesaglut-devel
BuildRequires:	mesaglu-devel
BuildRequires:	openal-devel
BuildRequires:	physfs-devel
Requires:	%{name}-data

%description
Trigger is a fast-paced open source rally racing game.

%prep
%setup -q -n %{name}-%{version}-src
%patch0 -p1 -b .nodoc

%build
%configure2_5x --bindir=%{_gamesbindir} --datadir=%{_gamesdatadir}/%{oname}
jam

%install
rm -rf %{buildroot}
DESTDIR=%{buildroot} jam install
# only contains .a files
rm -rf %{buildroot}%{_libdir}

install -D -m 644 %{SOURCE1} %{buildroot}%{_datadir}/icons/%{name}.png

install -d %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Trigger Rally
Comment=%{Summary}
Exec=soundwrapper %{_gamesbindir}/%{oname}
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;ArcadeGame;
EOF

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_gamesbindir}/%{oname}
%{_datadir}/icons/%{name}.png
%{_datadir}/applications/mandriva-%{name}.desktop

