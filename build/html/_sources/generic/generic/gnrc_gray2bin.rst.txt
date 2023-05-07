gnrc_gray2bin
------------------------------------------------
| Convert N bit GRAY code to N bit BINARY code.
| for example: 
| 1101 -> 1001
| 1111 -> 1010
| 1110 -> 1011
| 1100 -> 1010


Parameters
````````````````````````````````````````````````

.. csv-table::
   :header: "parameter", "datatype", "range", "description"
   :widths: 2, 2, 2, 4
   
   "N", "int", ">=1", "gray code bit width"
   


IOs
````````````````````````````````````````````````

.. csv-table::
   :header: "signal", "I/O", "width", "description"
   :widths: 2, 1, 2, 3
   
   "gray_i", "input", "logic [N-1:0]", "gray code input"
   "bin_o", "output", "logic [N-1:0]", "binary code output"
   

