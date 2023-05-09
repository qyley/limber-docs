gnrc_shift_reg
------------------------------------------------
Simple shift register for arbitrary depth and types


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
 "d_i", "input", "DTYPE", "serial data input"
 "d_o", "output", "DTYPE", "serial data output"
 

