package main

import (
	"os"
	"os/exec"
	"syscall"
)

func binaryAndArgs() (string, []string) {
	// os.Args[0] is 'win32-background-launcher.exe' and needs to be dropped
	// os.Args[1] is the name of the binary we want to start in the background
	// os.Args[2:] are the arguments of our binary
	switch {
	case len(os.Args) == 0:
		return "", []string{}
	case len(os.Args) == 1:
		return os.Args[1], []string{}
	default:
		return os.Args[1], os.Args[2:]
	}
}

func main() {
	binaryPath, args := binaryAndArgs()
	if binaryPath == "" {
		panic("missing binary name")
	}
	cmd := exec.Command(binaryPath, args...)
	cmd.SysProcAttr = &syscall.SysProcAttr{CreationFlags: 0x08000000}
	cmd.Stdout = os.Stdout
	cmd.Stdout = os.Stderr
	err := cmd.Run()
	if err != nil {
		panic(err.Error())
	}
}
