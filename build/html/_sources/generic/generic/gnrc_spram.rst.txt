gnrc_spram
------------------------------------------------
Single-port RAM.

This can be sythesis as BlockRAM primitive automatically in FPGA.


Parameters
````````````````````````````````````````````````

.. csv-table::
   :header: "parameter", "datatype", "range", "description"
   :widths: 2, 2, 2, 4
   
   "DW", "int(default)", ">=1", "Data bit width"
   "DP", "int(default)", ">=1", "RAM depth"
   "DELAY", "int(default)", ">=1", "RAM delay for simulation, It's recommended set DELAY = 1 in synthesis, otherwise a DFF chain of (DELAY-1) length will be implement between BRAM and dout"
   "OP_MODE", "int(default)", "{0,1,2}", "Operationg Mode, 0 for Write-First, 1 for Read-First, 2 for No-Change. **ONLY** support Read-First when BYTE_WRITE enable"
   "BYTE_WRITE", "int(default)", "{0,1}", "Set 1 to enable byte write"
   "INIT_BY_ZERO", "int(default)", "{0,1}", "Set 1 to initialize ram by zero"
   "INIT_BY_FILE", "int(default)", "file path", "Initialize ram by a hex file, the initial value can also be downloaded to FPGA. Leave this empty to disable."
   "AW", "int(default)", "$clog2(DP)", "Address bit width (auto-gen, do **NOT** change)"
   "MW", "int(default)", "$ceil(DW/8) if BYTE_WRITE, 1 otherwise", "Write enable bit width (auto-gen, do **NOT** change)"
   


IOs
````````````````````````````````````````````````

.. csv-table::
   :header: "signal", "I/O", "width", "description"
   :widths: 2, 1, 2, 3
   
   "clk_i", "input", "logic", "clock input"
   "din_i", "input", "logic [DW-1:0]", "data input"
   "en_i", "input", "logic", "enable input"
   "we_i", "input", "logic [MW-1:0]", "write enable input"
   "addr_i", "input", "logic [AW-1:0]", "write/read address input"
   "dout_o", "output", "logic [DW-1:0]", "data output"
   

