gnrc_lzc
------------------------------------------------
| OLD lzc description
| A trailing zero counter / leading zero counter.
| Set MODE to 0 for trailing zero counter => cnt_o is the number of trailing zeros (from the LSB)
| Set MODE to 1 for leading zero counter  => cnt_o is the number of leading zeros  (from the MSB)
| If the input does not contain a zero, `empty_o` is asserted. Additionally `cnt_o` contains
| the maximum number of zeros - 1. For example:
|   in_i = 000_0000, empty_o = 1, cnt_o = 6 (mode = 0)
|   in_i = 000_0001, empty_o = 0, cnt_o = 0 (mode = 0)
|   in_i = 000_1000, empty_o = 0, cnt_o = 3 (mode = 0)
| Furthermore, this unit contains a more efficient implementation for Verilator (simulation only).
| This speeds up simulation significantly.

| modify by qyley<qyley@foxmail.com>
| find the unmodified code in https://github.com/qyley/common_cells

- fix the bug that all zero in_i will cause an non-corresponding cnt_o result when WIDTH align/misalign 
  an integer power of 2. now cnt_o will always be 0 when in_i is all zero no matter what WIDTH be.
- since the leading zero counter's input must contain at least 1 bit of digit '1',
  otherwise empty_o will be assert, so the cnt_o actually indicates the bit location
  (i.e. the idx) of first "1", and the empty_o indicates there is no '1' exists in
  in_i, when empty_o = 1, cnt_o ought to be zero.
- so the modified gnrc_lzc's function described as follow:

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
   

