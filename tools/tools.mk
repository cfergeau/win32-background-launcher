TOOLS_BINDIR = $(realpath $(TOOLS_DIR)/bin)

$(TOOLS_BINDIR)/go-winres: $(TOOLS_DIR)/go.mod
	cd $(TOOLS_DIR) && GOBIN="$(TOOLS_BINDIR)" go install github.com/tc-hib/go-winres
