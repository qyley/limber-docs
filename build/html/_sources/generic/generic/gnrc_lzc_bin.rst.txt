gnrc_lzc_bin
------------------------------------------------
| qyley<qyley@foxmail.com>
| find a new way to implement lzc, see also `gnrc_lzc.sv`
|
| This implement firstly convert input vector into a thermometer code style(see `gnrc_lzc_therm.sv`)
| Then convert the thermometer code into binary code(see `gnrc_therm2bin`)
| Finally takes the MSB as the `empty_o` ane the rest as `cnt_o`
|
| NEW lzc description
| A trailing zero counter / leading zero counter (also be a first '1' counter).
| Set MODE to 0 for little-endian => cnt_o is the idx of first '1' from the LSB
| Set MODE to 1 for big-endian  => cnt_o is the idx of first '1' from the MSB
| If the input does not contain a '1', `empty_o` is asserted, and cnt_o is '0' in this case.
| `cnt_o` indicates the idx of first '1', also represents the maximum number of leading zeros.
| Additionally `empty_o` can be seem as a carry bit of `cnt_o` when WIDTH is an integer power of 2.
| For example (in mode = 0):
|   in_i = 0000_0000, empty_o = 1'b1, cnt_o = 3'b000
|   in_i = 0000_0001, empty_o = 1'b0, cnt_o = 3'b000
|   in_i = 0000_1000, empty_o = 1'b0, cnt_o = 3'b011


Parameters
````````````````````````````````````````````````

.. csv-table::
   :header: "parameter", "datatype", "range", "description"
   :widths: 2, 2, 2, 4
   
   "WIDTH", "int unsigned", ">=1", "The width of the input vector."
   "MODE", "bit", "{0,1}", "Mode selection: 0 -> trailing zero, 1 -> leading zero"
   "CNT_WIDTH", "int unsigned", "$clog2(WIDTH)+(WIDTH==1)", "Width of the output signal with the zero count(auto-gen, do **NOT** change)."
   


IOs
````````````````````````````````````````````````

.. csv-table::
   :header: "signal", "I/O", "width", "description"
   :widths: 2, 1, 2, 3
   
   "in_i", "input", "logic [WIDTH-1:0]", "Input vector to be counted."
   "cnt_o", "output", "logic [CNT_WIDTH-1:0]", "Count of the leading / trailing zeros."
   "empty_o", "output", "logic", "Counter is empty: Asserted if all bits in in_i are zero."
   

