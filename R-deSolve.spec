#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-deSolve
Version  : 1.20
Release  : 6
URL      : https://cran.r-project.org/src/contrib/deSolve_1.20.tar.gz
Source0  : https://cran.r-project.org/src/contrib/deSolve_1.20.tar.gz
Summary  : Solvers for Initial Value Problems of Differential Equations
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-deSolve-lib
BuildRequires : clr-R-helpers

%description
of first-order ordinary differential equations ('ODE'), of
        partial differential equations ('PDE'), of differential
        algebraic equations ('DAE'), and of delay differential
        equations.  The functions provide an interface to the FORTRAN
        functions 'lsoda', 'lsodar', 'lsode', 'lsodes' of the 'ODEPACK'
        collection, to the FORTRAN functions 'dvode', 'zvode' and 'daspk'
	and a C-implementation of solvers of the 'Runge-Kutta' family with
        fixed or variable time steps.  The package contains routines
        designed for solving 'ODEs' resulting from 1-D, 2-D and 3-D
        partial differential equations ('PDE') that have been converted
        to 'ODEs' by numerical differencing.

%package lib
Summary: lib components for the R-deSolve package.
Group: Libraries

%description lib
lib components for the R-deSolve package.


%prep
%setup -q -c -n deSolve

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523300167

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1523300167
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library deSolve
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library deSolve
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library deSolve
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library deSolve|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/deSolve/CITATION
/usr/lib64/R/library/deSolve/DESCRIPTION
/usr/lib64/R/library/deSolve/INDEX
/usr/lib64/R/library/deSolve/Meta/Rd.rds
/usr/lib64/R/library/deSolve/Meta/data.rds
/usr/lib64/R/library/deSolve/Meta/demo.rds
/usr/lib64/R/library/deSolve/Meta/features.rds
/usr/lib64/R/library/deSolve/Meta/hsearch.rds
/usr/lib64/R/library/deSolve/Meta/links.rds
/usr/lib64/R/library/deSolve/Meta/nsInfo.rds
/usr/lib64/R/library/deSolve/Meta/package.rds
/usr/lib64/R/library/deSolve/Meta/vignette.rds
/usr/lib64/R/library/deSolve/NAMESPACE
/usr/lib64/R/library/deSolve/NEWS
/usr/lib64/R/library/deSolve/R/deSolve
/usr/lib64/R/library/deSolve/R/deSolve.rdb
/usr/lib64/R/library/deSolve/R/deSolve.rdx
/usr/lib64/R/library/deSolve/data/Rdata.rdb
/usr/lib64/R/library/deSolve/data/Rdata.rds
/usr/lib64/R/library/deSolve/data/Rdata.rdx
/usr/lib64/R/library/deSolve/demo/CCL4model.R
/usr/lib64/R/library/deSolve/demo/odedim.R
/usr/lib64/R/library/deSolve/doc/compiledCode.R
/usr/lib64/R/library/deSolve/doc/compiledCode.Rnw
/usr/lib64/R/library/deSolve/doc/compiledCode.pdf
/usr/lib64/R/library/deSolve/doc/deSolve.R
/usr/lib64/R/library/deSolve/doc/deSolve.Rnw
/usr/lib64/R/library/deSolve/doc/deSolve.pdf
/usr/lib64/R/library/deSolve/doc/dynload-dede/dedeUtils.c
/usr/lib64/R/library/deSolve/doc/dynload-dede/dede_lv.R
/usr/lib64/R/library/deSolve/doc/dynload-dede/dede_lv.c
/usr/lib64/R/library/deSolve/doc/dynload-dede/dede_lv2.R
/usr/lib64/R/library/deSolve/doc/dynload-dede/dede_lv2.c
/usr/lib64/R/library/deSolve/doc/dynload-dede/dede_lv2F.f
/usr/lib64/R/library/deSolve/doc/dynload-dede/dede_lvF.f
/usr/lib64/R/library/deSolve/doc/dynload-dede/dedesimple.R
/usr/lib64/R/library/deSolve/doc/dynload-dede/dedesimple.c
/usr/lib64/R/library/deSolve/doc/dynload-dede/dedesimpleF.f
/usr/lib64/R/library/deSolve/doc/dynload/Aquaphy.f
/usr/lib64/R/library/deSolve/doc/dynload/AquaphyEvent.R
/usr/lib64/R/library/deSolve/doc/dynload/AquaphyForcing.R
/usr/lib64/R/library/deSolve/doc/dynload/AquaphyForcing.f
/usr/lib64/R/library/deSolve/doc/dynload/CCL4model.f
/usr/lib64/R/library/deSolve/doc/dynload/ChemicalDAE.f
/usr/lib64/R/library/deSolve/doc/dynload/Forcing_lv.R
/usr/lib64/R/library/deSolve/doc/dynload/Forcing_lv.c
/usr/lib64/R/library/deSolve/doc/dynload/SCOC.f
/usr/lib64/R/library/deSolve/doc/dynload/daspkdll.R
/usr/lib64/R/library/deSolve/doc/dynload/daspkfor.f
/usr/lib64/R/library/deSolve/doc/dynload/ex_Aquaphy.c
/usr/lib64/R/library/deSolve/doc/dynload/ex_Aquaphy.f
/usr/lib64/R/library/deSolve/doc/dynload/ex_CCL4model.c
/usr/lib64/R/library/deSolve/doc/dynload/ex_CCL4model.f
/usr/lib64/R/library/deSolve/doc/dynload/ex_SCOC.c
/usr/lib64/R/library/deSolve/doc/dynload/ex_SCOC.f
/usr/lib64/R/library/deSolve/doc/dynload/intakes.RData
/usr/lib64/R/library/deSolve/doc/dynload/lsodardll.R
/usr/lib64/R/library/deSolve/doc/dynload/lsodarfor.f
/usr/lib64/R/library/deSolve/doc/dynload/odeband.R
/usr/lib64/R/library/deSolve/doc/dynload/odeband.f
/usr/lib64/R/library/deSolve/doc/dynload/odec.c
/usr/lib64/R/library/deSolve/doc/dynload/odedll.R
/usr/lib64/R/library/deSolve/doc/dynload/odefor.f
/usr/lib64/R/library/deSolve/doc/dynload/odefor2.f
/usr/lib64/R/library/deSolve/doc/dynload/radaudae.f
/usr/lib64/R/library/deSolve/doc/dynload/radaudaedll.R
/usr/lib64/R/library/deSolve/doc/dynload/satres.R
/usr/lib64/R/library/deSolve/doc/dynload/satres.f
/usr/lib64/R/library/deSolve/doc/dynload/satresC.c
/usr/lib64/R/library/deSolve/doc/dynload/zvodedll.R
/usr/lib64/R/library/deSolve/doc/dynload/zvodedll.f
/usr/lib64/R/library/deSolve/doc/examples/Arenstorf.R
/usr/lib64/R/library/deSolve/doc/examples/Daphnia_event.R
/usr/lib64/R/library/deSolve/doc/examples/Nand.R
/usr/lib64/R/library/deSolve/doc/examples/Pollution.R
/usr/lib64/R/library/deSolve/doc/examples/Schelde_DSA.R
/usr/lib64/R/library/deSolve/doc/examples/Schelde_FKA.R
/usr/lib64/R/library/deSolve/doc/examples/Schelde_FNA.R
/usr/lib64/R/library/deSolve/doc/examples/Schelde_OSA.R
/usr/lib64/R/library/deSolve/doc/examples/Schelde_pars.R
/usr/lib64/R/library/deSolve/doc/examples/ballode.R
/usr/lib64/R/library/deSolve/doc/examples/examples_paper.R
/usr/lib64/R/library/deSolve/doc/index.html
/usr/lib64/R/library/deSolve/doc/mymod.c
/usr/lib64/R/library/deSolve/doc/mymod.f
/usr/lib64/R/library/deSolve/doc/source/ddaspkcomments.txt.gz
/usr/lib64/R/library/deSolve/doc/source/opkdmain.f.gz
/usr/lib64/R/library/deSolve/doc/source/opkdmaincomments.txt.gz
/usr/lib64/R/library/deSolve/doc/source/vodecomments.txt.gz
/usr/lib64/R/library/deSolve/help/AnIndex
/usr/lib64/R/library/deSolve/help/aliases.rds
/usr/lib64/R/library/deSolve/help/deSolve.rdb
/usr/lib64/R/library/deSolve/help/deSolve.rdx
/usr/lib64/R/library/deSolve/help/paths.rds
/usr/lib64/R/library/deSolve/html/00Index.html
/usr/lib64/R/library/deSolve/html/R.css
/usr/lib64/R/library/deSolve/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/deSolve/libs/deSolve.so
/usr/lib64/R/library/deSolve/libs/deSolve.so.avx2
/usr/lib64/R/library/deSolve/libs/deSolve.so.avx512
