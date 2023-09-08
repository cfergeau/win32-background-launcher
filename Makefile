.PHONY: build
build: win32-background-launcher

# win32-background-launcher is compiled as a windows GUI to support backgrounding
.PHONY: win32-background-launcher
win32-background-launcher:
	GOOS=windows go build -ldflags -H=windowsgui -o bin/win32-background-launcher.exe ./
