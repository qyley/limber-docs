gnrc_therm2bin
------------------------------------------------
| Convert N bit THERMOMETER code to log2(N+1) bit BINARY code.
| for example: 
| 000_0000 -> 000
| 000_0001 -> 001
| 000_0011 -> 010
| 000_0111 -> 011
| ...
| 111_1111 -> 111
| For the sake of a simple circuit structure, we don't consider illegal input.
| This module first convert THERMOMETER code to ONEHOT code using a `gnrc_therm2onehot`
| Then convert the ONEHOT code to BINARY code using a `gnrc_onehot2bin`
| See more in `gnrc_therm2onehot.sv` and `gnrc_onehot2bin.sv`


Parameters
````````````````````````````````````````````````

.. csv-table::
   :header: "parameter", "datatype", "range", "description"
   :widths: 2, 2, 2, 4
   
   "N", "int unsigned", ">=1", "thermometer code width"
   "M", "int unsigned", "$clog2(N+1)+(N==1)", "binary code bit width (auto-gen, do **NOT** change)"
   


IOs
````````````````````````````````````````````````

.. csv-table::
   :header: "signal", "I/O", "width", "description"
   :widths: 2, 1, 2, 3
   
   "therm_i", "input", "logic [N-1:0]", "thermometer code input"
   "bin_o", "output", "logic [M-1:0]", "binary code output"
   

