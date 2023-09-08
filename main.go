package main

import (
	"os"
	"os/exec"
	"path/filepath"
)

func argv() []string {
	if len(os.Args) > 0 {
		return os.Args[1:]
	}
	return []string{}
}

func absolutePath(path string) (string, error) {
	absPath, err := exec.LookPath(path)
	if err != nil {
		return "", err
	}
	absPath, err = filepath.Abs(absPath)
	if err != nil {
		return "", err
	}
	return absPath, nil
}

func main() {
	binaryPath, err := absolutePath("./gvproxy-windows.exe")
	if err != nil {
		panic(err.Error())
	}
	cmd := exec.Command(binaryPath, argv()...)
	cmd.Stdout = os.Stdout
	cmd.Stdout = os.Stderr
	err = cmd.Run()
	if err != nil {
		panic(err.Error())
	}
}
