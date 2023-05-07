gnrc_lzc_therm
------------------------------------------------
| a lzc(leading zero counter) but `cnt_o` is encoded by thermometer code
| It is more simpler to implement a lzc in thermometer code than binary code
|
| For example:
|   vec_i = 0000_0000, therm_o = 1111_1111(overflow)
|   vec_i = 0000_0001, therm_o = 00000_000
|   vec_i = 0000_1010, therm_o = 00000_001
|   vec_i = 0010_1000, therm_o = 00000_111
|   vec_i = 1000_0000, therm_o = 01111_111


Parameters
````````````````````````````````````````````````

.. csv-table::
   :header: "parameter", "datatype", "range", "description"
   :widths: 2, 2, 2, 4
   
   "N", "int unsigned", ">=1", "input vector bit width"
   


IOs
````````````````````````````````````````````````

.. csv-table::
   :header: "signal", "I/O", "width", "description"
   :widths: 2, 1, 2, 3
   
   "vec_i", "input", "logic [N-1:0]", "input vector"
   "therm_o", "output", "logic [N-1:0]", "output leading zero counter by thermometer code"
   

