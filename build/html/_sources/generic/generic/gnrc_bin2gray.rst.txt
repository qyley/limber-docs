gnrc_bin2gray
------------------------------------------------
| Convert N bit BINARY code to N bit GRAY code.
| for example: 
| 1001 -> 1101
| 1010 -> 1111
| 1011 -> 1110
| 1100 -> 1010


Parameters
````````````````````````````````````````````````

.. csv-table::
   :header: "parameter", "datatype", "range", "description"
   :widths: 2, 2, 2, 4
   
   "N", "int", ">=1", "Binary code bit width"
   


IOs
````````````````````````````````````````````````

.. csv-table::
   :header: "signal", "I/O", "width", "description"
   :widths: 2, 1, 2, 3
   
   "bin_i", "input", "logic [N-1:0]", "binary code input"
   "gray_o", "output", "logic [N-1:0]", "gray code output"
   

