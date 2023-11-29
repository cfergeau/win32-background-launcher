.PHONY: build
build: win32-background-launcher

TOOLS_DIR := tools
include tools/tools.mk

VERSION := 0.0.0.1

# win32-background-launcher is compiled as a windows GUI to support backgrounding
.PHONY: win32-background-launcher
win32-background-launcher: $(TOOLS_BINDIR)/go-winres
	GOOS=windows ./tools/bin/go-winres simply --file-version $(VERSION) --product-name "Red Hat OpenShift Local Background Launcher"
	GOOS=windows go build -ldflags -H=windowsgui -o bin/crc-background-launcher.exe ./
	
.PHONY: vendor
vendor: vendor-tools
	go mod tidy
	go mod vendor
