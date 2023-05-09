gnrc_fifo
------------------------------------------------
|
| Synchronous Normal FIFO
|
| Vivado can decide to implement this FIFO by DistRAM or BlockRAM **automatically**
  according to its scale of parameter DW and DP


Parameters
````````````````````````````````````````````````


.. csv-table::
 :header: "parameter", "datatype", "range", "description"
 :widths: 2, 2, 2, 4
 
 "DW", "int(default)", ">=1", "Data bit width"
 "DP", "int(default)", ">=2", "FIFO depth"
 "FWFT", "bit", "{0,1}", "1 to enable First Word Fall Through FIFO, 0 for Standard FIFO."
 "CW", "int(default)", "$clog2(DP+1)", "data counter bit width (auto-gen, do **NOT** change)"
 


IOs
````````````````````````````````````````````````

.. csv-table::
 :header: "signal", "I/O", "width", "description"
 :widths: 2, 1, 2, 3
   
 "clk_i", "input", "logic", "Clock, positive edge triggered."
 "rst_ni", "input", "logic", "Asynchronous reset, active low."
 "flush_i", "input", "logic", "Clears all data in FIFO."
 "data_i", "input", "logic [DW-1:0]", "data input"
 "wen_i", "input", "logic", "write enable (push)"
 "ren_i", "input", "logic", "read enable (pop)"
 "full_o", "output", "logic", "FIFO full"
 "empty_o", "output", "logic", "FIFO empty"
 "data_o", "output", "logic [DW-1:0]", "data output"
 "data_cnt_o", "output", "logic [CW-1:0]", "number of data in FIFO , it may be **NOT** accurate in `FWFT` mode"


Detail
````````````````````````````````````````````````

此模块是由 `gnrc_mem2fifo` 加上 `gnrc_simple_dpram` 拼成的，具体详情请查看这两个模块的介绍。
 

