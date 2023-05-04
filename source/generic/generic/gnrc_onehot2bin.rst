gnrc_onehot2bin
------------------------------------------------
| Convert N bit ONEHOT code to log2(N) bit BINARY code.
| for example: 
| 0000_0001 -> 000
| 0000_0010 -> 001
| 1000_0000 -> 111
| For the sake of a simple circuit structure, we don't consider illegal input.
| If input code is not a ONEHOT code, this module also give an output
| It will seem input as a bitwise-or of several discrete ONEHOT code
| And the output will be a bitwise-or of BINARY code converted from
  those discrete ONEHOT code
| for example:
| 0001_0010 can be seem as (0001_0000 | 0000_0010)
| so the output will be (100 | 001) = 101
| And if input is all zero, the output is 0.
| In simulation, input a non ONEHOT code to this module will assert an fatal issue.


Parameters
````````````````````````````````````````````````

.. csv-table::
   :header: "parameter", "datatype", "range", "description"
   :widths: 2, 2, 2, 4
   
   "N", "int unsigned", ">=1", "one-hot code width"
   "M", "int unsigned", "$clog2(N)+(N==1)", "binary code bit width (auto-gen, do **NOT** change)"
   


IOs
````````````````````````````````````````````````

.. csv-table::
   :header: "signal", "I/O", "width", "description"
   :widths: 2, 1, 2, 3
   
   "onehot_i", "input", "logic [N-1:0]", "one-hot code input"
   "bin_o", "output", "logic [M-1:0]", "binary code output"
   

