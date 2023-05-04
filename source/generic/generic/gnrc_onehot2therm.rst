gnrc_onehot2therm
------------------------------------------------
| Convert N bit ONEHOT code to N-1 bit THERMOMETER code.
| for example: 
| 0000_0001 -> 000_0000
| 0000_0010 -> 000_0001
| 0000_0100 -> 000_0011
| 0000_1000 -> 000_0111
| ...
| 1000_0000 -> 111_1111
| For the sake of a simple circuit structure, we don't consider illegal input.
| This module instantiate a `gnrc_lzc_therm`, see more in `gnrc_lzc_therm.sv`


Parameters
````````````````````````````````````````````````

.. csv-table::
   :header: "parameter", "datatype", "range", "description"
   :widths: 2, 2, 2, 4
   
   "N", "int unsigned", ">=1", "one-hot code width"
   "M", "int unsigned", "N-1+(N==1)", "thermometer code bit width (auto-gen, do **NOT** change)"
   


IOs
````````````````````````````````````````````````

.. csv-table::
   :header: "signal", "I/O", "width", "description"
   :widths: 2, 1, 2, 3
   
   "onehot_i", "input", "logic [N-1:0]", "one-hot code input"
   "therm_o", "output", "logic [M-1:0]", "thermometer code output"
   

