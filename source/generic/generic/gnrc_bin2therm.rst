gnrc_bin2therm
------------------------------------------------
| Convert N bit BINARY code to 2^N-1 bit THERMOMETER code.
| for example: 
| 000 -> 000_0000
| 001 -> 000_0001
| 010 -> 000_0011
| 011 -> 000_0111
| ...
| 111 -> 111_1111


Parameters
````````````````````````````````````````````````

.. csv-table::
   :header: "parameter", "datatype", "range", "description"
   :widths: 2, 2, 2, 4
   
   "N", "int unsigned", ">=1", "binary code bit width"
   "M", "int unsigned", "2^N-1", "thermometer code bit width (auto-gen, do **NOT** change)"
   


IOs
````````````````````````````````````````````````

.. csv-table::
   :header: "signal", "I/O", "width", "description"
   :widths: 2, 1, 2, 3
   
   "bin_i", "input", "logic [N-1:0]", "binary code input"
   "therm_o", "output", "logic [M-1:0]", "thermometer code output"
   

