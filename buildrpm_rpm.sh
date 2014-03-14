#!/bin/bash

file=$HOME/.rpmmacros
rpmdir=$HOME/rpm
if [ -z $1 ]
then
	echo "no revision given"
	exit 1 
else
	rev=$1
fi
rpm_name=ermis
version=1.0
release=$rev

#backup old .rpmmacros file
if [ -a $file ]
    then `mv $file $file.backup`
fi

#populate .rpmmacros
echo "%_topdir $rpmdir
%_buildroot %{_tmppath}/%{name}-build
%_tmppath $rpmdir
%vendor CERN
%define __os_install_post %{nil}
%debug_package %{nil}" >$file

mkdir -p $rpmdir/{SPECS,RPMS,BUILD,SOURCES,SRPMS}
rm -rf $rpmdir/SPECS/$rpm_name.$version.spec

#Crap way to create spec file

cat > $rpmdir/SPECS/$rpm_name.$version.spec << EOF
Summary: $rpm_name
Name: $rpm_name
Version:$version
Release: $release
License: LGPL
Group: System Environment/Base
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
Packager: $USER
AutoReqProv: no
Requires: Django, MySQL-python, django-piston
BuildRequires: python-markdown


%description
Ermis is Gateway for adding, removing, updating and listing
DNS aliases without the need to use the LBWeb interface.

%prep
markdown $PWD/doc/api.md > content.html
cat $PWD/doc/html/header.html content.html $PWD/doc/html/footer.html > api.html
sed -i -e s/@@ERMISVERSION@@/$version/g api.html
mkdir -p \$RPM_BUILD_ROOT/usr/share/doc/ermis
mv api.html \$RPM_BUILD_ROOT/usr/share/doc/ermis/api.html
cp $PWD/doc/html/style.css \$RPM_BUILD_ROOT/usr/share/doc/ermis

mkdir -p \$RPM_BUILD_ROOT/var/www
touch \$RPM_BUILD_ROOT/var/www/tempdb

mkdir -p \$RPM_BUILD_ROOT/var/log/ermis
touch \$RPM_BUILD_ROOT/var/www/ermis.log

mkdir -p \$RPM_BUILD_ROOT/usr/lib/python2.6/site-packages/ermis/
cp -rf $PWD/src/ermis/* \$RPM_BUILD_ROOT/usr/lib/python2.6/site-packages/ermis/

%files
%defattr(0755,root,root,-)
/usr/lib/python2.6/site-packages/ermis/*

%defattr(0770,root,apache,-)
/usr/share/doc/ermis/api.html
/usr/share/doc/ermis/style.css
/var/www/ermis.log
/var/www/tempdb

%dir
%defattr(0755,root,apache,-)
/var/log/ermis

%clean
rm -rf content
rm -rf  \$RPM_BUILD_ROOT/


%post
ln -sf /usr/share/doc/ermis/api.html  /var/www/html/index.html
ln -sf /usr/share/doc/ermis/style.css  /var/www/html/style.css
ln -sf /usr/lib/python2.6/site-packages/ermis/ /var/www/ermis
ln  -sf /var/www/ermis.log /var/log/ermis/ermis.log
%preun
echo "Nothing in preun"


%postun
rm -rf /usr/lib/python2.6/site-packages/ermis/ /usr/share/doc/ermis/ /var/www/html/index.html /var/www/html/style.css /var/www/ermis /var/log/ermis/ermis.log /var/log/ermis/ 
EOF
rpmbuild -bb $rpmdir/SPECS/$rpm_name.$version.spec

echo "done"
###cat $rpmdir/SPECS/$rpm_name.$version.spec

#restore original .rpmmacros
if [ -a $file.backup ]
    then mv $file.backup $file
fi
