%define debug_package %{nil}
%define repo github.com/tektoncd/cli
Name:           tkn
Version:        0.1.2
Release:        1%{?dist}
Summary:        A CLI for interacting with Tekton!

License:        Apache 2.0
URL:            https://%{repo}
Source0:        https://%{repo}/archive/v%{version}.tar.gz

BuildRequires:  git golang
%if 0%{?fedora}
BuildRequires: systemd
%endif


%description
The Tekton Pipelines cli project provides a CLI for interacting with Tekton !

%prep
mkdir -p %{_builddir}/src/github.com/tektoncd/
cd %{_builddir}/src/github.com/tektoncd/
tar -xvzf %{_sourcedir}/v%{version}.tar.gz 
mv tkn-%{version} cli

%build
export GOPATH="%{_builddir}"
export PATH=$PATH:"%{_builddir}"/bin
cd %{_builddir}/src/github.com/tektoncd/cli/cmd/tkn
export GO111MODULE=on 
go install -ldflags "-X github.com/tektoncd/cli/pkg/cmd/version.clientVersion=%{version}"

%install
mkdir -p %{buildroot}%{_bindir}

cp %{_builddir}/bin/tkn %{buildroot}%{_bindir}


%files
%{_bindir}/tkn

%changelog
* Thu Jun 20 2019 Khurram Baig <kbaig@redhat.com> 0.12
- Initial version of the rpm


