gnrc_therm2onehot
------------------------------------------------
| Convert N bit THERMOMETER code to N+1 bit ONEHOT code.
| for example: 
| 000_0000 -> 0000_0001
| 000_0001 -> 0000_0010
| 000_0011 -> 0000_0100
| 000_0111 -> 0000_1000
| ...
| 111_1111 -> 1000_0000
| For the sake of a simple circuit structure, we don't consider illegal input.
| onehot_o is given by {1'b0, therm_i} ^ {therm_i, 1'b1}.


Parameters
````````````````````````````````````````````````

.. csv-table::
   :header: "parameter", "datatype", "range", "description"
   :widths: 2, 2, 2, 4
   
   "N", "int unsigned", ">=1", "thermometer code width"
   "M", "int unsigned", "N+1", "onehot code bit width (auto-gen, do **NOT** change)"
   


IOs
````````````````````````````````````````````````

.. csv-table::
   :header: "signal", "I/O", "width", "description"
   :widths: 2, 1, 2, 3
   
   "therm_i", "input", "logic [N-1:0]", "thermometer code input"
   "onehot_o", "output", "logic [M-1:0]", "onehot code output"
   

