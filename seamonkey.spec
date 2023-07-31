%define homepage https://www.openmandriva.org/

%define _disable_lto 1
%define default_bookmarks_file %{_datadir}/bookmarks/default-bookmarks.html
#define Werror_cflags %nil

%define minimum_build_nspr_version 4.12
%define minimum_build_nss_version 3.25

%define build_langpacks 0

%define builddir %{_builddir}/%{name}-%{version}
%define mozdir %{_libdir}/%{name}-%{version}
#beta
#release

%if %{_use_internal_dependency_generator}
%define __noautoprov '(.*)\\.so(.*)'
%define __noautoreq 'libldap60.\\.so(.*)|libldif60\\.so(.*)|libmozalloc\\.so(.*)|libplc4\\.so(.*)|libplds4\\.so(.*)|libprldap60\\.so(.*)|libxpcom\\.so(.*)|libxul\\.so(.*)'
%endif

Summary:	Web browser, e-mail, news, IRC client, HTML editor
Name:		seamonkey
Version:	2.53.10.2
Release:	2
License:	MPLv1.1
Group:		Networking/WWW
Url:		http://http://www.seamonkey-project.org/
Source0:	https://archive.mozilla.org/pub/seamonkey/releases/%{version}/source/seamonkey-%{version}.source.tar.xz
Source1:	https://archive.mozilla.org/pub/seamonkey/releases/%{version}/source/seamonkey-%{version}.source-l10n.tar.xz
#Source1:	%{name}-langpacks-%{version}.tar.xz
Source2:	%{name}.png
Source3:	%{name}.sh.in
Source7:	%{name}-make-package.pl
Source8:	bookmarks.html
Source17:	mozilla-psm-exclude-list
Source18:	mozilla-xpcom-exclude-list
# No more config for Mandriva
#Source20:	%{name}-mandriva-default-prefs.js

BuildRequires:	autoconf2.1
BuildRequires:	cargo
BuildRequires:	coreutils
BuildRequires:	desktop-file-utils
BuildRequires:	doxygen
BuildRequires:	gcc-c++
BuildRequires:	imagemagick
BuildRequires:	makedepend
BuildRequires:	perl
BuildRequires:	python
BuildRequires:	pkgconfig(python2)
BuildRequires:	python2-setuptools
BuildRequires:	python-setuptools
BuildRequires:	python-virtualenv >= 1.7.2
BuildRequires:	rootcerts
BuildRequires:	unzip
BuildRequires:	valgrind
BuildRequires:	wget
BuildRequires:	nasm
BuildRequires:	yasm
BuildRequires:	zip

BuildRequires:	jpeg-devel
BuildRequires:	krb5-devel
#BuildRequires:	libiw-devel
BuildRequires:	nss-static-devel

BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(gconf-2.0)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gstreamer-1.0)
BuildRequires:	pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(hunspell)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(libevent)
BuildRequires:	pkgconfig(libIDL-2.0)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libproxy-1.0)
BuildRequires:	pkgconfig(libstartup-notification-1.0)
BuildRequires:	pkgconfig(nspr)
BuildRequires:	pkgconfig(nss)
BuildRequires:	pkgconfig(pango)
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	pkgconfig(vpx)
BuildRequires:	pkgconfig(xinerama)
BuildRequires:	pkgconfig(xrender)
BuildRequires:	pkgconfig(xscrnsaver)
BuildRequires:	pkgconfig(xt)
BuildRequires:	pkgconfig(zlib)

Requires:	nspr >= %{minimum_build_nspr_version}
Requires:	nss >= %{minimum_build_nss_version}
Obsoletes:	%{name}-devel < %{version}
Obsoletes:	%{name}-dom-inspector < %{version}
Obsoletes:	%{name}-enigmail  < %{version}
Obsoletes:	%{name}-enigmime < %{version}
Obsoletes:	%{name}-irc < %{version}
Obsoletes:	%{name}-js-debugger < %{version}
Obsoletes:	%{name}-mail < %{version}
Obsoletes:	%{name}-spellchecker < %{version}

%description
SeaMonkey is an all-in-one Internet application suite. It includes 
a browser, mail/news client, IRC client, JavaScript debugger, and 
a tool to inspect the DOM for web pages. It is derived from the 
application formerly known as Mozilla Application Suite.


%prep
%setup -q
chmod +x %{SOURCE7}

rm -f .mozconfig

%autopatch -p1

%build

MOZ_OPT_FLAGS='%{optflags}'
export CFLAGS=$MOZ_OPT_FLAGS
export CXXFLAGS=$MOZ_OPT_FLAGS
export LDFLAGS="-Wl,--no-keep-memory"
export BUILD_OFFICIAL=1
export MOZILLA_OFFICIAL=1
echo "mk_add_options BUILD_OFFICIAL=1" >> .mozconfig
echo "mk_add_options MOZILLA_OFFICIAL=1" >> .mozconfig
echo "mk_add_options MOZ_MAKE_FLAGS=%{_smp_mflags}" >> .mozconfig
echo "mk_add_options MOZ_OBJDIR=../obj-@CONFIG_GUESS@" >> .mozconfig
echo "ac_add_options --host=%{_host}" >> .mozconfig
echo "ac_add_options --prefix=%{_prefix}" >> .mozconfig
echo "ac_add_options --libdir=%{_libdir}" >> .mozconfig
echo "ac_add_options --enable-application=comm/suite" >> .mozconfig
echo "ac_add_options --enable-optimize=-O2" >> .mozconfig
echo "ac_add_options --enable-release" >> .mozconfig
echo "ac_add_options --enable-default-toolkit=cairo-gtk3" >> .mozconfig 
echo "ac_add_options --disable-updater" >> .mozconfig
echo "ac_add_options --disable-crashreporter" >> .mozconfig
echo "ac_add_options --with-irc" >> .mozconfig
echo "ac_add_options --with-dominspector" >> .mozconfig
echo "ac_add_options --enable-calendar" >> .mozconfig
echo "ac_add_options --with-system-nspr" >> .mozconfig
echo "ac_add_options --with-system-nss" >> .mozconfig
echo "ac_add_options --with-system-zlib" >> .mozconfig
echo "ac_add_options --disable-tests" >> .mozconfig
echo "ac_add_options --disable-install-strip" >> .mozconfig
echo "ac_add_options --enable-js-shell" >> .mozconfig
echo "ac_add_options --enable-calendar" >> .mozconfig
echo "ac_add_options --enable-dominspector" >> .mozconfig
echo "ac_add_options --enable-irc" >> .mozconfig
# Not ready yet
#echo "ac_add_options --with-l10n-base=$RPM_BUILD_DIR/seamonkey-%{version}/l10n" >> .mozconfig


export CC=%__cc
export CXX=%__cxx

# Mozilla builds with -Wall with exception of a few warnings which show up
# everywhere in the code; so, don't override that.
#
# Disable C++ exceptions since Mozilla code is not exception-safe
#
MOZ_OPT_FLAGS=$(echo %{optflags} | \
                     sed -e 's/-Wall//' -e 's/-fexceptions/-fno-exceptions/g')
export CFLAGS=$MOZ_OPT_FLAGS
export CXXFLAGS=$MOZ_OPT_FLAGS

export PREFIX='%{_prefix}'
export LIBDIR='%{_libdir}'

MOZ_SMP_FLAGS=%{_smp_mflags}

./mach build

%install

pushd ../obj-*
%make_install
popd

# create a list of all of the different package and the files that
# will hold them

echo %defattr\(-,root,root\) > %{builddir}/%{name}.list

# we don't want to ship mozilla's default sidebar components
rm -f %{buildroot}/%{mozdir}/searchplugins/bugzilla.gif
rm -f %{buildroot}/%{mozdir}/searchplugins/bugzilla.src
rm -f %{buildroot}/%{mozdir}/searchplugins/dmoz.gif
rm -f %{buildroot}/%{mozdir}/searchplugins/dmoz.src
rm -f %{buildroot}/%{mozdir}/searchplugins/lxrmozilla.gif
rm -f %{buildroot}/%{mozdir}/searchplugins/lxrmozilla.src
rm -f %{buildroot}/%{mozdir}/searchplugins/mozilla.gif
rm -f %{buildroot}/%{mozdir}/searchplugins/mozilla.src
rm -f %{buildroot}/%{mozdir}/plugins/libnullplugin.so

# the %%makeinstall_std macro also install files that we don't need (yet?)
rm -rf %{buildroot}%{_datadir}/idl

echo > ../%{name}.lang
%if %{build_langpacks}
# Install langpacks
mkdir -p %{buildroot}%{mozdir}/extensions
tar xf %{SOURCE1}
for langpack in `ls seamonkey-langpacks/*.xpi`; do
  language=$(basename $langpack .xpi | sed 's/^seamonkey-//' | sed 's/\.langpack$//' | sed 's/\([0-9]\{1,2\}\.\)*//')
  extensiondir=%{buildroot}%{mozdir}/extensions/langpack-$language@seamonkey.mozilla.org
  mkdir -p $extensiondir
  unzip $langpack -d $extensiondir
  find $extensiondir -type f | xargs chmod 644

  jarfile=$extensiondir/chrome/$language.jar

  sed -i -e "s|browser.startup.homepage.*$|browser.startup.homepage=%{homepage}|g;" \
         $extensiondir/chrome/$language/locale/$language/navigator-region/region.properties

  pushd $extensiondir/chrome/$language
  zip -r -D $jarfile locale
  popd

  language=`echo $language | sed -e 's/-/_/g'`
  extensiondir=`echo $extensiondir | sed -e "s,^%{buildroot},,"`
  echo "%%lang($language) $extensiondir" >> ../%{name}.lang
done
rm -rf firefox-langpacks
%endif # build_langpacks


# set up our desktop files
install -m 755 -d %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=SeaMonkey Navigator
Comment=Seamonkey Navigator web browser
Exec=%{_bindir}/%{name} %u
Icon=%{name}.png
Terminal=false
Type=Application
StartupNotify=true
Categories=GTK;Network;WebBrowser;X-MandrivaLinux-Internet-WebBrowsers;
MimeType=text/html;text/xml;application/xhtml+xml;application/vnd.mozilla.xul+xml;text/mml;
StartupWMClass=Seamonkey-bin
EOF

cat > %{buildroot}%{_datadir}/applications/%{name}-mail.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=SeaMonkey Mail
Comment=Seamonkey Mail & Newsgroups e-mail client
Exec=%{_bindir}/%{name} -mail
Icon=%{name}.png
Terminal=false
Type=Application
StartupNotify=true
Categories=GTK;X-MandrivaLinux-Internet-Mail;Office;Network;Email;
MimeType=x-scheme-handler/mailto;
StartupWMClass=Seamonkey-bin
EOF

#Icons
mkdir -p %{buildroot}%{_datadir}/pixmaps/
install -c -m 644 %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/%{name}.png

mkdir -p %{buildroot}{%{_liconsdir},%{_iconsdir},%{_miconsdir}}
install -m 644 %{SOURCE2} %{buildroot}%{_miconsdir}/%{name}.png
install -m 644 %{SOURCE2} %{buildroot}%{_iconsdir}/%{name}.png
install -m 644 %{SOURCE2} %{buildroot}%{_liconsdir}/%{name}.png
#convert %{buildroot}%{_miconsdir}/%{name}.png -resize 16x16 %{buildroot}%{_miconsdir}/%{name}.png
#convert %{buildroot}%{_iconsdir}/%{name}.png -resize 32x32 %{buildroot}%{_iconsdir}/%{name}.png


#Link to existing plugins
#if [ -d %{buildroot}/%{mozdir}/plugins ]; then
#rm -rf %{buildroot}/%{mozdir}/plugins
#fi
#ln -s %{_libdir}/mozilla/plugins %{buildroot}/%{mozdir}/plugins

# install our seamonkey.sh file
rm -rf %{buildroot}/usr/bin/%{name}
cat %{SOURCE3} | sed -e 's/MOZILLA_VERSION/%{version}/g' \
		     -e 's,LIBDIR,%{_libdir},g' > \
  %{buildroot}%{_bindir}/%{name}

chmod 0755 %{buildroot}%{_bindir}/%{name}

# set up our default preferences
#cat %{SOURCE20} | %{__sed} -e 's,SEAMONKEY_RPM_VR,%{version}-%{release},g' > \
#        %{buildroot}/mdv-default-prefs
#cp %{buildroot}/mdv-default-prefs %{buildroot}/%{mozdir}/defaults/pref/all-mandriva.js
#rm %{buildroot}/mdv-default-prefs

# set up our default bookmarks
rm -f %{buildroot}/%{mozdir}/defaults/profile/bookmarks.html
#
#install -m 0644 %{SOURCE8} %{buildroot}%{mozdir}/defaults/profile/bookmarks.html

#remove unneeded files
rm -f %{buildroot}%{mozdir}/.autoreg
rm -f %{buildroot}%{mozdir}/removed-files
rm -f %{buildroot}%{mozdir}/update.locale
rm -f %{buildroot}%{mozdir}/updater.ini

rm -rf %{buildroot}%{_libdir}/%{name}-devel-%{version}
rm -rf %{buildroot}%{_includedir}

%files
%{_bindir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_libdir}/seamonkey/
%{_datadir}/applications/*.desktop
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png

