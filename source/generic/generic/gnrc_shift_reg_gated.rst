gnrc_shift_reg_gated
------------------------------------------------
A Simple shift register with ICG for arbitrary depth and types.


Parameters
````````````````````````````````````````````````


.. csv-table::
 :header: "parameter", "datatype", "range", "description"
 :widths: 2, 2, 2, 4
 
 "DEPTH", "int unsigned", ">=1", "the number of FF"
 "DTYPE", "type", "logic(default)", "data type"
 


IOs
````````````````````````````````````````````````

.. csv-table::
 :header: "signal", "I/O", "width", "description"
 :widths: 2, 1, 2, 3
   
 "clk_i", "input", "logic", "Clock"
 "rst_ni", "input", "logic", "Asynchronous reset active low"
 "valid_i", "input", "logic", "valid in"
 "data_i", "input", "DTYPE", "data in"
 "valid_o", "output", "logic", "valid out"
 "data_o", "output", "DTYPE", "data out"
 

