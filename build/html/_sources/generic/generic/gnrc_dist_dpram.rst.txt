gnrc_dist_dpram
------------------------------------------------
Configurable Distribution Simple dual-port RAM.

This can be sythesis as LUT RAM automatically in FPGA.


Parameters
````````````````````````````````````````````````

.. csv-table::
   :header: "parameter", "datatype", "range", "description"
   :widths: 2, 2, 2, 4
   
   "DW", "int(default)", ">=1", "Data bit width"
   "DP", "int(default)", ">=1", "RAM depth"
   "IBUF", "int(default)", "{0,1}", "Set 1 to implement a register in input."
   "OBUF", "int(default)", "{0,1}", "Set 1 to implement a register in output."
   "INIT_BY_ZERO", "int(default)", "{0,1}", "Set 1 to initialize ram by zero"
   "INIT_BY_FILE", "int(default)", "file path", "Initialize ram by a hex file, the initial value can also be downloaded to FPGA. Leave this empty to disable."
   "AW", "int(default)", "$clog2(DP)", "Address bit width (auto-gen, do **NOT** change)"
   


IOs
````````````````````````````````````````````````

.. csv-table::
   :header: "signal", "I/O", "width", "description"
   :widths: 2, 1, 2, 3
   
   "clk_i", "input", "logic", "clock input"
   "din_i", "input", "logic [DW-1:0]", "data input"
   "we_i", "input", "logic", "write enable input"
   "addr_i", "input", "logic [AW-1:0]", "address"
   "addrb_i", "input", "logic [AW-1:0]", "dual port address"
   "dout_o", "output", "logic [DW-1:0]", "data output"
   "doutb_o", "output", "logic [DW-1:0]", "dual port data output"
   

