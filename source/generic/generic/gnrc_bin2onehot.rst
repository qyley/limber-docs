gnrc_bin2onehot
------------------------------------------------
| Convert N bit BINARY code to 2^N bit ONEHOT code.
| for example: 
| 1001 -> 0000_0010_0000_0000
| 0000 -> 0000_0000_0000_0001
| 1111 -> 1000_0000_0000_0000


Parameters
````````````````````````````````````````````````

.. csv-table::
   :header: "parameter", "datatype", "range", "description"
   :widths: 2, 2, 2, 4
   
   "N", "int unsigned", ">=1", "binary code bit width"
   "M", "int unsigned", "2^N", "onehot code bit width (auto-gen, do **NOT** change)"
   


IOs
````````````````````````````````````````````````

.. csv-table::
   :header: "signal", "I/O", "width", "description"
   :widths: 2, 1, 2, 3
   
   "bin_i", "input", "logic [N-1:0]", "binary code input"
   "onehot_o", "output", "logic [M-1:0]", "one-hot code output"
   

