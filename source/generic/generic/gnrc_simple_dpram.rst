gnrc_simple_dpram
------------------------------------------------
Simple dual-port RAM.

This can be sythesis as BlockRAM primitive automatically in FPGA.


Parameters
````````````````````````````````````````````````

.. csv-table::
   :header: "parameter", "datatype", "range", "description"
   :widths: 2, 2, 2, 4
   
   "DW", "int(default)", ">=1", "Data bit width"
   "DP", "int(default)", ">=1", "RAM depth"
   "DELAY", "int(default)", ">=1", "RAM delay for simulation, It's recommended set DELAY = 1 in synthesis, otherwise a DFF chain of (DELAY-1) length will be implement between BRAM and dout"
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
   
   "wclk_i", "input", "logic", "Write port clock input"
   "wdata_i", "input", "logic [DW-1:0]", "Write port data input"
   "wen_i", "input", "logic", "Write port enable input"
   "we_i", "input", "logic [MW-1:0]", "Write port write enable input"
   "waddr_i", "input", "logic [AW-1:0]", "Write port write address input"
   "rclk_i", "input", "logic", "Read port clock input"
   "ren_i", "input", "logic", "Read port enable input"
   "raddr_i", "input", "logic [AW-1:0]", "Read port read address input"
   "rdata_o", "output", "logic [DW-1:0]", "Read port data output"
   

