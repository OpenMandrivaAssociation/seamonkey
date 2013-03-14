%define homepage http://mib.pianetalinux.org/

%define default_bookmarks_file %{_datadir}/bookmarks/default-bookmarks.html
#define Werror_cflags %nil

%define minimum_build_nspr_version 4.8.8
%define minimum_build_nss_version 3.12.10

%define build_langpacks 1

%define builddir %{_builddir}/%{name}-%{version}
%define mozdir %{_libdir}/%{name}-%{version}
%define sources_subdir comm-release
#beta
#release

%if %{_use_internal_dependency_generator}
%define __noautoprov '(.*)\\.so(.*)'
%define __noautoreq 'libldap60.\\.so(.*)|libldif60\\.so(.*)|libmozalloc\\.so(.*)|libplc4\\.so(.*)|libplds4\\.so(.*)|libprldap60\\.so(.*)|libxpcom\\.so(.*)|libxul\\.so(.*)'
%endif

Name:		seamonkey
Summary:	Web browser, e-mail, news, IRC client, HTML editor
Version:	2.16.2
Release:	1
URL:		http://www.mozilla.org/projects/seamonkey/
License:	MPLv1.1
Group:		Networking/WWW

Source0:	%{name}-%{version}.source.tar.bz2
Source1:	%{name}-langpacks-%{version}.tar.bz2
Source2:	%{name}.png
Source3:	%{name}.sh.in
Source7:	%{name}-make-package.pl
Source8:	bookmarks.html
Source10:	%{name}-2.9.1-mozconfig
Source17:	mozilla-psm-exclude-list
Source18:	mozilla-xpcom-exclude-list
Source20:	%{name}-mandriva-default-prefs.js
Patch2:		mozilla-2.16-prefer_plugin_pref.patch
Patch3:		mozilla-2.16-shared-nss-db.patch
Patch6:		mozilla-gstreamer.patch
Patch8:		mozilla-2.14-ntlm-full-path.patch

Patch12:	mozilla-2.16-nongnome-proxies.patch
Patch13:	mozilla-MIB-2.0.5-homepage.patch

Patch21:	seamonkey-2.16-shared-nss-db.patch

Patch47:	autocomplete.patch

Patch510:	wip-17.0.patch

BuildRequires:	autoconf2.1
BuildRequires:	coreutils
BuildRequires:	desktop-file-utils
BuildRequires:	doxygen
BuildRequires:	gcc-c++
BuildRequires:	imagemagick
BuildRequires:	java-rpmbuild
BuildRequires:	makedepend
BuildRequires:	perl
BuildRequires:	python
BuildRequires:	python-setuptools
BuildRequires:	python-simplejson
BuildRequires:	python-virtualenv >= 1.7.2
BuildRequires:	rootcerts
BuildRequires:	unzip
BuildRequires:	valgrind
BuildRequires:	wget
BuildRequires:	yasm
BuildRequires:	zip


BuildRequires:	jpeg-devel
BuildRequires:	krb5-devel
BuildRequires:	libiw-devel
BuildRequires:	nss-static-devel

BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gnome-vfs-2.0)
BuildRequires:	pkgconfig(gstreamer-0.10)
BuildRequires:	pkgconfig(gstreamer-plugins-base-0.10)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(hunspell)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(libevent)
BuildRequires:	pkgconfig(libgnome-2.0)
BuildRequires:	pkgconfig(libgnomeui-2.0)
BuildRequires:	pkgconfig(libIDL-2.0)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	pkgconfig(libpng15)
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
%setup -q -c
chmod +x %{SOURCE7}
cd %{sources_subdir}
mkdir mozilla/js/src/.deps
%patch47 -p1

%patch13 -p1

# mozilla patches
pushd mozilla
# mozilla-nongnome-proxies
%patch12 -p1
%patch2 -p1
# mozilla-shared-nss-db.patch
%patch3 -p1
%patch6 -p1
%patch8 -p1

%patch510 -p1
popd
##
# seamonkey-shared-nss-db.patch
%patch21 -p1

rm -f .mozconfig
cp %{SOURCE10} .mozconfig

%build
cd %{sources_subdir}

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

MOZ_SMP_FLAGS=-j1
%ifnarch ppc ppc64 s390 s390x
[ -z "$RPM_BUILD_NCPUS" ] && \
     RPM_BUILD_NCPUS="`/usr/bin/getconf _NPROCESSORS_ONLN`"
[ "$RPM_BUILD_NCPUS" -gt 1 ] && MOZ_SMP_FLAGS=-j2
%endif

make -f client.mk build STRIP="/bin/true" MOZ_MAKE_FLAGS="$MOZ_SMP_FLAGS" MOZ_PKG_FATAL_WARNINGS=0


%install
cd %{sources_subdir}

DESTDIR=%{buildroot} make install

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

# build all of the default browser components 
# base Seamonkey package (seamonkey.list) 
%{SOURCE7} --package xpcom --output-file %{builddir}/seamonkey.list \
    --package-file suite/installer/package-manifest \
    --install-dir %{buildroot}/%{mozdir} \
    --install-root %{mozdir} \
    --exclude-file=%{SOURCE18}

%{SOURCE7} --package browser --output-file %{builddir}/seamonkey.list \
    --package-file suite/installer/package-manifest \
    --install-dir %{buildroot}/%{mozdir} \
    --install-root %{mozdir}

%{SOURCE7} --package spellcheck --output-file %{builddir}/seamonkey.list \
    --package-file suite/installer/package-manifest \
    --install-dir %{buildroot}/%{mozdir} \
    --install-root %{mozdir}

%{SOURCE7} --package psm --output-file %{builddir}/seamonkey.list \
    --package-file suite/installer/package-manifest \
    --install-dir %{buildroot}/%{mozdir} \
    --install-root %{mozdir} \
    --exclude-file=%{SOURCE17}

%{SOURCE7} --package mail --output-file %{builddir}/seamonkey.list \
    --package-file suite/installer/package-manifest \
    --install-dir %{buildroot}/%{mozdir} \
    --install-root %{mozdir}

%{SOURCE7} --package chatzilla --output-file %{builddir}/seamonkey.list \
    --package-file suite/installer/package-manifest \
    --install-dir %{buildroot}/%{mozdir} \
    --install-root %{mozdir}

%{SOURCE7} --package venkman --output-file %{builddir}/seamonkey.list \
    --package-file suite/installer/package-manifest \
    --install-dir %{buildroot}/%{mozdir} \
    --install-root %{mozdir}

%{SOURCE7} --package inspector --output-file %{builddir}/seamonkey.list \
    --package-file suite/installer/package-manifest \
    --install-dir %{buildroot}/%{mozdir} \
    --install-root %{mozdir}

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
convert %{buildroot}%{_miconsdir}/%{name}.png -resize 16x16 %{buildroot}%{_miconsdir}/%{name}.png
convert %{buildroot}%{_iconsdir}/%{name}.png -resize 32x32 %{buildroot}%{_iconsdir}/%{name}.png


#Link to existing plugins
if [ -d %{buildroot}/%{mozdir}/plugins ]; then
rm -rf %{buildroot}/%{mozdir}/plugins
fi
ln -s %{_libdir}/mozilla/plugins %{buildroot}/%{mozdir}/plugins

# install our seamonkey.sh file
rm -rf %{buildroot}/usr/bin/%{name}
cat %{SOURCE3} | sed -e 's/MOZILLA_VERSION/%{version}/g' \
		     -e 's,LIBDIR,%{_libdir},g' > \
  %{buildroot}%{_bindir}/%{name}

chmod 0755 %{buildroot}%{_bindir}/%{name}

# fix unstripped-binary-or-object rpmlint error (needed in 2.16.2)
chmod 0755 %{buildroot}/%{mozdir}/libxpcom.so

# set up our default preferences
cat %{SOURCE20} | %{__sed} -e 's,SEAMONKEY_RPM_VR,%{version}-%{release},g' > \
        %{buildroot}/mdv-default-prefs
cp %{buildroot}/mdv-default-prefs %{buildroot}/%{mozdir}/defaults/pref/all-mandriva.js
rm %{buildroot}/mdv-default-prefs

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
%{mozdir}
%{_datadir}/applications/*.desktop
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png

